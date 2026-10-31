import copy
import json
from unittest.mock import patch
from django.test import TestCase, override_settings
from django.utils import timezone
from .models import Submission, AutomationRun, Verification
from .verification import digest, inventory, validate_report, step, require_verified
from .article_validation import InvalidArticle

SOURCE = '''---
title: Example
ticker: None
category: Concept
written_by: test-writer high
status: draft
updated: 2026-10-31
---

# Example

Example launched in 2009.[^1]

| Date | Event |
|---|---|
| 2009 | Example launched.[^1] |

## References

[^1]: [Official history](https://example.com/history)
'''
URL = 'https://example.com/history'


def evidence(text='Example launched in 2009.', url=URL):
    return [{'stop_reason':'end_turn', 'content':[
        {'type':'web_search_tool_result','content':[{'type':'web_search_result','url':url}]},
        {'type':'web_fetch_tool_result','content':{'type':'web_fetch_result','url':url,
            'content':{'source':{'type':'text','data':text}}}},
    ]}]


def report(source=SOURCE):
    units,_=inventory(source)
    results=[]
    for unit in units:
        structural = unit['text'].startswith(('#','category:','ticker: None')) or unit['text']=='| Date | Event |'
        results.append({'id':unit['id'],'verdict':'nonfactual' if structural else 'supported',
            'claims':[] if structural else [{'claim':unit['text'],'url':URL,'quote':'Example launched in 2009.', 'explanation':'The official source establishes this fact.'}]})
    return {'source_hash':digest(source),'as_of':timezone.localdate().isoformat(),'verdict':'pass',
            'source_rules_met':True,'freshness_checked':True,'issues':[],'units':results}


class VerificationTests(TestCase):
    def setUp(self):
        self.run=AutomationRun.objects.create(submission=Submission.objects.create(kind='request'))
        self.check=Verification.objects.create(run=self.run, source=SOURCE, source_hash=digest(SOURCE))

    def test_complete_evidence_passes_and_each_table_row_is_covered(self):
        units,_=inventory(SOURCE)
        self.assertTrue(any('2009 |' in u['text'] for u in units))
        self.assertEqual(validate_report(self.check,report(),evidence())[0],[])

    def test_missing_wrong_and_unopened_evidence_fail(self):
        for responses in ([],evidence('Example launched in 2010.'), evidence(url='https://example.com/other')):
            self.assertTrue(validate_report(self.check,report(),responses)[0])
        incomplete=report();incomplete['units'].pop()
        self.assertIn('incomplete_claim_coverage',validate_report(self.check,incomplete,evidence())[0])
        unchecked=report();unchecked['verdict']='revise'
        self.assertIn('checker_did_not_pass',validate_report(self.check,unchecked,evidence())[0])

    def test_prose_cannot_be_labelled_nonfactual(self):
        result=report()
        for unit in result['units']:
            unit.update(verdict='nonfactual',claims=[])
        self.assertTrue(validate_report(self.check,result,evidence())[0])

    def test_hash_freshness_and_source_rules_are_enforced(self):
        for key,value in [('source_hash','0'*64),('as_of','2000-01-01'),('source_rules_met',False),('freshness_checked',False),('issues',['Fix the date before publishing'])]:
            result=report();result[key]=value
            self.assertTrue(validate_report(self.check,result,evidence())[0])

    @patch('submissions.ai_providers.call')
    def test_independent_checker_and_exact_publication_hash(self,call):
        response=evidence()[0]
        response['model']='checker-model-v1'
        response['content'].append({'type':'text','text':'```json\n'+json.dumps(report())+'\n```'})
        call.return_value=response
        step(self.check)
        self.assertEqual(self.check.state,'passed')
        self.assertEqual(self.check.checker,'checker-model-v1 (high effort)')
        args=call.call_args.args
        self.assertEqual(args[2],'fact_check')
        self.assertNotIn('writer_research',json.dumps(args[3]))
        from types import SimpleNamespace
        record=SimpleNamespace(run_id=self.run.pk,markdown=self.check.approved_source)
        require_verified(record)
        record.markdown=record.markdown.replace('2009','2010')
        with self.assertRaises(InvalidArticle):require_verified(record)

    @patch('submissions.ai_providers.call')
    def test_paused_check_resumes_with_saved_tools_and_never_approves_partial(self,call):
        call.return_value={'stop_reason':'pause_turn','content':[],'usage':{}}
        step(self.check)
        self.assertEqual(self.check.state,'pending')
        self.assertEqual(self.check.approved_hash,'')
        step(self.check)
        self.assertEqual(len(call.call_args.args[3]['messages']),2)
        self.assertEqual(len(call.call_args.args[3]['tools']),2)
        step(self.check)
        self.assertEqual(self.check.state,'pending')
        self.assertEqual(self.check.session['mode'],'report')

    def test_local_reference_is_rejected(self):
        with self.assertRaises(InvalidArticle):inventory(SOURCE.replace(URL,'http://127.0.0.1/secret'))


class ResponseFormatTests(TestCase):
    def test_only_complete_json_or_one_enclosing_fence_is_accepted(self):
        from .article_validation import extract_draft
        for text in ('{"edits": []}', '```json\n{"edits": []}\n```'):
            self.assertEqual(extract_draft({'stop_reason':'end_turn','content':[{'type':'text','text':text}]}),{'edits':[]})
        for text in ('Explanation before\n```json\n{"edits": []}\n```', '```json\n{"edits": []}\n```\nExtra prose', '```json\n{"edits": ['):
            with self.assertRaises(InvalidArticle):
                extract_draft({'stop_reason':'end_turn','content':[{'type':'text','text':text}]})
        with self.assertRaises(InvalidArticle):
            extract_draft({'stop_reason':'max_tokens','content':[{'type':'text','text':'{"edits": []}'}]})
