import copy
from unittest.mock import patch

from django.test import TestCase, override_settings
from django.utils import timezone

from . import editorial, salvage
from .article_validation import InvalidArticle
from .budgets import BudgetExceeded
from .improvements import apply_patch
from .models import ArticleRevision, AutomationRun, Submission, Verification
from .verification import (approve_confirmed, check_inventory, close_unchecked, confirmed_units, digest,
                           require_verified, split_article)

HISTORY = 'https://example.com/history'
ACQUIRED = 'https://example.com/acquired'
FRONT = '---\ntitle: Example\nticker: EXM\ncategory: Concept\nstatus: draft\nupdated: 2026-11-01\nwritten_by: test-writer\n---\n\n'
BODY = '''Example is a protocol launched in 2009.[^1]

| | |
|---|---|
| Launch | 2009[^1] |
| Owner | Acme[^2] |

## History

Example launched in 2009.[^1]

## Acquisition

Example was acquired by Acme in 2015.[^2]

## Timeline

| Date | Event |
|---|---|
| 2009 | Example launched.[^1] |
| 2015 | Acme acquired Example.[^2] |

## References

[^1]: [Official history](https://example.com/history)
[^2]: [Acquisition](https://example.com/acquired)
'''
ARTICLE = FRONT + BODY


def opened(*urls):
    blocks = [{'type': 'web_search_tool_result', 'content': [{'type': 'web_search_result', 'url': url} for url in (HISTORY, ACQUIRED)]}]
    blocks += [{'type': 'web_fetch_tool_result', 'content': {'type': 'web_fetch_result', 'url': url,
                'content': {'source': {'type': 'text', 'data': 'Example launched in 2009.'}}}} for url in urls]
    return [{'stop_reason': 'end_turn', 'content': blocks}]


def checked(check, supported=lambda text: 'Acme' not in text, size=4, skip=()):
    """Save one group report per batch, as the checker would, without calling a model."""
    units = check_inventory(check)[0]
    check.session['batches'] = []
    for start in range(0, len(units), size):
        group = units[start:start + size]
        batch = {'ids': [unit['id'] for unit in group], 'responses': []}
        if start // size not in skip:
            results, errors = [], []
            for unit in group:
                if unit.get('table_header') or unit['text'].startswith(('#', 'category:')) or unit['text'] == '| | |':
                    results.append({'id': unit['id'], 'verdict': 'nonfactual', 'claims': []})
                elif supported(unit['text']):
                    results.append({'id': unit['id'], 'verdict': 'supported', 'claims': [{
                        'claim': unit['text'], 'url': HISTORY, 'quote': 'Example launched in 2009.', 'explanation': 'Stated.'}]})
                else:
                    results.append({'id': unit['id'], 'verdict': 'unsupported', 'claims': []})
                    errors.append('unsupported_unit_' + unit['id'])
            if errors:
                errors += ['unresolved_checker_issues', 'checker_did_not_pass', 'unopened_references']
            batch.update(report={'verdict': 'revise' if errors else 'pass', 'units': results, 'source_rules_met': True,
                                 'issues': ['The acquisition source could not be opened.'] if errors else []},
                         errors=errors, checker='test-checker')
        check.session['batches'].append(batch)
    check.state = 'failed'
    check.completed_at = timezone.now()
    check.save()
    return check


class NewArticleTests(TestCase):
    def setUp(self):
        self.run = AutomationRun.objects.create(
            submission=Submission.objects.create(kind='request', title='Example', status='reviewing'), state='checking',
            research=opened(HISTORY)[0],
            draft={'title': 'Example', 'slug': 'example', 'ticker': 'EXM', 'category': 'Concept', 'markdown': BODY, '_written_by': 'test-writer'})
        self.check = Verification.objects.create(run=self.run, source=ARTICLE, source_hash=digest(ARTICLE),
                                                 session={'scope': 'draft', 'responses': opened(HISTORY), 'mode': 'report'})
        self.run.editorial = {'stage': 'check', 'check_id': self.check.pk, 'candidate': ARTICLE, 'fulfillment': 'complete'}
        self.run.save()

    def test_confirmed_passages_are_published_and_the_rest_left_out(self):
        checked(self.check)
        with patch('submissions.editorial.publish_checked') as publish:
            editorial.publish_confirmed(self.run, self.check)
        approved = publish.call_args.args[1]
        source = approved.approved_source
        self.assertEqual(approved.state, 'passed')
        self.assertEqual(approved.session['confirmed_subset_of'], self.check.pk)
        self.assertIn('Example is a protocol launched in 2009.[^1]', source)
        self.assertIn('| 2009 | Example launched.[^1] |', source)
        self.assertIn('| Launch | 2009[^1] |', source)
        # Unconfirmed paragraph, rows, its emptied heading and its orphaned footnote are gone.
        for removed in ('Acme', '## Acquisition', '[^2]', ACQUIRED):
            self.assertNotIn(removed, source)
        self.assertIn('## History', source)
        self.assertIn('status: draft', source)
        self.assertNotIn('checked_by', source)
        self.run.refresh_from_db()
        self.assertEqual(self.run.editorial['fulfillment'], 'partial')
        self.assertEqual(self.run.editorial['left_out'], 3)
        self.assertIn('Example was acquired by Acme in 2015.', self.run.editorial['follow_up'])
        self.assertIn('could not be opened', self.run.editorial['follow_up'])
        self.assertNotIn('Acme', self.run.draft['markdown'])
        # The approval is bound to exactly this text, like any other passed check.
        self.assertEqual(digest(source), approved.approved_hash)
        self.check.refresh_from_db()
        self.assertEqual(self.check.state, 'failed')
        self.assertEqual(self.check.approved_hash, '')

    def test_unconfirmed_ticker_is_withheld(self):
        checked(self.check, supported=lambda text: 'Acme' not in text and 'ticker' not in text)
        with patch('submissions.editorial.publish_checked') as publish:
            editorial.publish_confirmed(self.run, self.check)
        self.assertEqual(split_article(publish.call_args.args[1].approved_source)[0]['ticker'], 'None')

    def test_nothing_confirmed_ends_with_a_clear_outcome(self):
        checked(self.check, supported=lambda text: False)
        with patch('submissions.editorial.publish_checked') as publish:
            editorial.publish_confirmed(self.run, self.check)
        publish.assert_not_called()
        self.run.refresh_from_db(); self.run.submission.refresh_from_db()
        self.assertEqual(self.run.state, 'insufficient')
        self.assertIn('No article was created', self.run.submission.public_summary)
        self.assertFalse(self.run.verifications.filter(state='passed').exists())

    def test_a_group_without_a_report_is_unconfirmed(self):
        self.check.session['responses'] = opened(HISTORY, ACQUIRED)
        self.run.research = opened(HISTORY, ACQUIRED)[0]
        checked(self.check, supported=lambda text: True, skip=(2,))
        kept, rejected, unchecked = confirmed_units(self.check)
        self.assertEqual(rejected, [])
        self.assertTrue(unchecked)
        with patch('submissions.editorial.publish_checked') as publish:
            editorial.publish_confirmed(self.run, self.check)
        source = publish.call_args.args[1].approved_source
        for unit in unchecked:
            self.assertNotIn(unit['text'], source)

    def test_a_supported_claim_citing_an_unopened_reference_is_unconfirmed(self):
        # The checker says everything is supported, but the acquisition page was never opened.
        checked(self.check, supported=lambda text: True)
        rejected = {unit['text'] for unit in confirmed_units(self.check)[1]}
        self.assertEqual(rejected, {'| Owner | Acme[^2] |', 'Example was acquired by Acme in 2015.[^2]', '| 2015 | Acme acquired Example.[^2] |'})

    def test_issues_without_a_failing_unit_leave_the_whole_group_unconfirmed(self):
        checked(self.check, supported=lambda text: True)
        batch = self.check.session['batches'][0]
        batch['errors'] = ['unresolved_checker_issues', 'checker_did_not_pass']
        self.assertTrue({'title: Example', 'ticker: EXM'} <= {unit['text'] for unit in confirmed_units(self.check)[1]})

    def test_approval_rejects_any_text_the_check_did_not_confirm(self):
        checked(self.check)
        with self.assertRaisesMessage(InvalidArticle, 'unconfirmed_unit_in_subset'):
            approve_confirmed(self.check, ARTICLE)
        with self.assertRaisesMessage(InvalidArticle, 'unconfirmed_unit_in_subset'):
            approve_confirmed(self.check, ARTICLE.replace('Example was acquired by Acme in 2015.[^2]', 'Example is worth billions.[^1]')
                              .replace('| Owner | Acme[^2] |\n', '').replace('| 2015 | Acme acquired Example.[^2] |\n', ''))

    def test_budget_exhaustion_mid_check_publishes_what_finished_groups_confirmed(self):
        checked(self.check, skip=(2, 3))
        self.check.state = 'pending'; self.check.completed_at = None; self.check.save()
        with patch('submissions.editorial.check_step', side_effect=BudgetExceeded('run_token_budget', 2, 1)), \
                patch('submissions.editorial.publish_checked') as publish:
            editorial.process(self.run)
        self.check.refresh_from_db()
        self.assertEqual(self.check.state, 'failed')
        self.assertEqual(self.check.session['batches'][3]['errors'], ['run_token_budget'])
        self.assertIn('Example is a protocol launched in 2009.[^1]', publish.call_args.args[1].approved_source)
        self.assertNotIn('## Timeline', publish.call_args.args[1].approved_source)

    def test_budget_exhaustion_before_any_group_stays_an_operational_block(self):
        self.check.session['batches'] = [{'ids': ['1'], 'responses': []}]; self.check.save()
        self.assertFalse(close_unchecked(self.check, 'run_token_budget'))
        with patch('submissions.editorial.check_step', side_effect=BudgetExceeded('run_token_budget', 2, 1)):
            with self.assertRaises(BudgetExceeded):
                editorial.process(self.run)
        with patch('submissions.editorial.check_step', side_effect=BudgetExceeded('daily_token_budget', 2, 1)):
            with self.assertRaises(BudgetExceeded):
                editorial.process(self.run)


ORIGINAL = FRONT + '''Example is a protocol launched in 2009.[^1]

## History

Example launched in 2009.[^1]

It was the first of its kind.[^1]

## References

[^1]: [Official history](https://example.com/history)
'''
PATCH = {'_written_by': 'test-writer', 'references': '[^1]: [Official history](https://example.com/history)\n[^2]: [Acquisition](https://example.com/acquired)',
         'edits': [
             {'anchor': 'Example launched in 2009.[^1]', 'position': 'after',
              'markdown': 'Its public release followed in 2009.[^1]\n\nAcme funded the release.[^2]'},
             {'anchor': '## References', 'position': 'before', 'markdown': '## Acquisition\n\nAcme acquired Example in 2015.[^2]'},
             {'anchor': 'It was the first of its kind.[^1]', 'position': 'replace', 'markdown': 'Acme calls it the first of its kind.[^2]'},
             {'anchor': '## History', 'position': 'replace', 'markdown': '## Origins'}]}


class EditTests(TestCase):
    def setUp(self):
        self.run = AutomationRun.objects.create(
            submission=Submission.objects.create(kind='improvement', article='example', status='reviewing'), state='checking',
            research=opened(HISTORY)[0], draft=copy.deepcopy(PATCH))
        self.record = ArticleRevision.objects.create(run=self.run, slug='example', title='Example', original_markdown=ORIGINAL,
                                                     base_content_hash=digest(ORIGINAL), base_revision='a' * 40)
        candidate = apply_patch(self.record, PATCH, ORIGINAL)
        self.check = Verification.objects.create(run=self.run, source=candidate, source_hash=digest(candidate), session={
            'scope': 'edit', 'original_source': ORIGINAL, 'base_hash': digest(ORIGINAL), 'responses': opened(HISTORY), 'mode': 'report'})
        self.run.editorial = {'stage': 'check', 'check_id': self.check.pk, 'candidate': candidate}
        self.run.save()

    def test_confirmed_edits_are_published_and_unconfirmed_ones_dropped(self):
        checked(self.check)
        with patch('submissions.editorial.publish_checked') as publish:
            editorial.publish_confirmed(self.run, self.check)
        approved = publish.call_args.args[1]
        source = approved.approved_source
        self.assertIn(f'Its public release followed in 2009.[^imp-{self.run.pk}-1]', source)
        self.assertIn('## Origins', source)
        # The unconfirmed paragraph, the whole unconfirmed section and the unconfirmed
        # replacement are dropped; the paragraph it would have replaced is untouched.
        for removed in ('Acme', '## Acquisition', ACQUIRED):
            self.assertNotIn(removed, source)
        self.assertIn('It was the first of its kind.[^1]', source)
        self.run.refresh_from_db()
        self.assertEqual([edit['position'] for edit in self.run.draft['edits']], ['after', 'replace'])
        self.assertEqual(self.run.editorial['left_out'], 3)
        self.assertEqual(approved.session['base_hash'], digest(ORIGINAL))
        # The publisher's exact-source gate accepts this approval and nothing else.
        self.record.markdown = source
        require_verified(self.record)
        self.record.markdown = self.check.source
        with self.assertRaises(InvalidArticle):
            require_verified(self.record)

    def test_no_confirmed_edit_leaves_the_article_unchanged(self):
        checked(self.check, supported=lambda text: False)
        self.run.draft['edits'] = self.run.draft['edits'][:3]
        self.run.save()
        with patch('submissions.editorial.publish_checked') as publish:
            editorial.publish_confirmed(self.run, self.check)
        publish.assert_not_called()
        self.run.refresh_from_db(); self.run.submission.refresh_from_db()
        self.assertEqual(self.run.state, 'insufficient')
        self.assertIn('existing article is unchanged', self.run.submission.public_summary)

    def test_follow_up_is_queued_once_and_stops_after_two_rounds(self):
        self.run.editorial['follow_up'] = 'Passages left out:\n- Acme acquired Example in 2015.'
        first = salvage.queue_follow_up(self.run, self.record)
        self.assertEqual((first.kind, first.article, first.status), ('improvement', 'example', 'new'))
        self.assertEqual(first.maintenance_key, f'followup:1:{self.run.pk}')
        self.assertEqual(salvage.queue_follow_up(self.run, self.record).pk, first.pk)
        self.assertIn('Acme acquired Example', first.details)
        second_run = AutomationRun.objects.create(submission=first, editorial={'follow_up': 'more'})
        second = salvage.queue_follow_up(second_run, self.record)
        self.assertEqual(second.maintenance_key, f'followup:2:{second_run.pk}')
        third_run = AutomationRun.objects.create(submission=second, editorial={'follow_up': 'more'})
        self.assertIsNone(salvage.queue_follow_up(third_run, self.record))
        self.run.editorial['follow_up'] = ''
        self.assertIsNone(salvage.queue_follow_up(AutomationRun.objects.create(
            submission=Submission.objects.create(kind='improvement'), editorial={'follow_up': ''}), self.record))


class FullCheckTests(TestCase):
    def setUp(self):
        self.run = AutomationRun.objects.create(
            submission=Submission.objects.create(kind='maintenance', article='example', status='reviewing'), state='checking')
        self.record = ArticleRevision.objects.create(run=self.run, slug='example', title='Example', original_markdown=ARTICLE,
                                                     base_content_hash=digest(ARTICLE), base_revision='a' * 40)
        self.check = Verification.objects.create(run=self.run, source=ARTICLE, source_hash=digest(ARTICLE),
                                                 session={'scope': 'full', 'responses': opened(HISTORY, ACQUIRED), 'mode': 'report'})
        self.run.editorial = {'stage': 'check', 'check_id': self.check.pk, 'candidate': ARTICLE}
        self.run.save()

    def test_findings_never_delete_published_text_and_become_one_targeted_repair(self):
        checked(self.check)
        with patch('submissions.editorial.publish_checked') as publish:
            editorial.publish_confirmed(self.run, self.check)
            editorial.publish_confirmed(AutomationRun.objects.get(pk=self.run.pk), self.check)
        publish.assert_not_called()
        self.run.refresh_from_db(); self.run.submission.refresh_from_db()
        self.assertEqual(self.run.state, 'insufficient')
        self.assertIn('could not confirm 3 passages', self.run.submission.public_summary)
        self.assertFalse(self.run.verifications.filter(state='passed').exists())
        repair = Submission.objects.get(maintenance_key__startswith='repair:example:')
        self.assertEqual((repair.kind, repair.article, repair.public_title), ('improvement', 'example', 'Repair: Example'))
        self.assertIn('Example was acquired by Acme in 2015.', repair.details)

    def test_partial_approval_is_never_a_full_article_certification(self):
        checked(self.check)
        with self.assertRaisesMessage(InvalidArticle, 'partial_approval_requires_draft_scope'):
            approve_confirmed(self.check, ARTICLE)


@override_settings(AUTOMATION_ENABLED=True, IDEAS_ENABLED=False, MAINTENANCE_ENABLED=False)
class SchedulingTests(TestCase):
    def test_follow_ups_yield_to_readers_and_do_not_preempt_work_in_progress(self):
        from .autonomous_worker import schedule
        idea = AutomationRun.objects.create(state='checking', editorial={'stage': 'check'},
            submission=Submission.objects.create(kind='request', status='reviewing', maintenance_key='idea:2026-11-15:1'))
        follow_up = Submission.objects.create(kind='improvement', article='example', maintenance_key='followup:1:7')
        # A queued follow-up is not a waiting reader, so the editor's pick in progress continues.
        self.assertEqual(schedule().pk, idea.pk)
        idea.state = 'published'; idea.save()
        reader = Submission.objects.create(kind='request', title='Reader request')
        self.assertEqual(schedule().submission_id, reader.pk)
        AutomationRun.objects.filter(submission=reader).update(state='published')
        self.assertEqual(schedule().submission_id, follow_up.pk)
