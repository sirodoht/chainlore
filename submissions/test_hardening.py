import importlib.util
import json
import os
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

from django.conf import settings
from django.core import mail
from django.test import SimpleTestCase, TestCase, override_settings

from . import ai_providers as ai
from . import catalog, notify
from .git_publication import git_env, minimal_env
from .limits import client_network
from .models import Submission

spec = importlib.util.spec_from_file_location('chainlore_build_gate', settings.BASE_DIR / 'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class RenderGateTests(SimpleTestCase):
    def render(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'page.md'
            path.write_text(text)
            with patch.object(build, 'ROOT', Path(directory)), patch.dict(build.ROUTES, {'page.md': '/p/page/'}):
                return build.render(path)

    def test_ordinary_articles_render(self):
        page = self.render('Lead with a citation.[^1]\n\n| A | B |\n|:--|--:|\n| 1 | 2 |\n\n'
                           '## Section\n\nSee <https://example.com/a> and `code`.\n\n[^1]: [Source](https://example.com/s)\n')
        self.assertEqual(page['toc'], [('section', 'Section')])

    def test_active_content_fails_the_build(self):
        for text in ('<script>alert(1)</script>', '<img src=x onerror=alert(1)>', '<iframe src="https://example.com"></iframe>',
                     '<p onclick="alert(1)">text</p>', '<p style="position:fixed">text</p>',
                     '[link](javascript:alert(1))', '[link](JaVaScript:alert(1))', '[link](data:text/html,x)',
                     '[link]: vbscript:x\n\n[link]', '<a href="java&#9;script:alert(1)">x</a>',
                     '<form action="https://example.com"><input name="q"/></form>', '<svg><a href="#x">x</a></svg>'):
            with self.subTest(text=text), self.assertRaises((ValueError, ET.ParseError)):
                self.render(text)


class RateLimitKeyTests(SimpleTestCase):
    def test_ipv6_clients_share_their_prefix(self):
        self.assertEqual(client_network('2001:db8:1:2:aaaa::1'), client_network('2001:db8:1:2:bbbb::2'))
        self.assertNotEqual(client_network('2001:db8:1:2::1'), client_network('2001:db8:1:3::1'))

    def test_ipv4_and_mapped_addresses_match(self):
        self.assertEqual(client_network('203.0.113.9'), '203.0.113.9')
        self.assertEqual(client_network('::ffff:203.0.113.9'), '203.0.113.9')

    def test_unparseable_values_share_one_bucket(self):
        self.assertEqual(client_network(''), 'unknown')
        self.assertEqual(client_network('not an address'), client_network('203.0.113.9, 10.0.0.1'))


class CatalogCacheTests(SimpleTestCase):
    def test_a_new_publication_replaces_the_cached_catalog(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, title in (('one', 'First'), ('two', 'Second release')):
                (root / name).mkdir()
                (root / name / 'article-catalog.json').write_text(json.dumps({'page': {'title': title}}))
            (root / 'current').symlink_to(root / 'one')
            with override_settings(ARTICLE_CATALOG=root / 'current/article-catalog.json'):
                self.assertEqual(catalog.articles()['page']['title'], 'First')
                self.assertIs(catalog.articles(), catalog.articles())
                (root / 'next').symlink_to(root / 'two')
                os.replace(root / 'next', root / 'current')
                self.assertEqual(catalog.articles()['page']['title'], 'Second release')


class SubprocessEnvironmentTests(SimpleTestCase):
    def test_secrets_are_not_inherited(self):
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'secret', 'TYPESAFE_API_KEY': 'secret', 'SSH_AUTH_SOCK': '/agent'}):
            for env in (minimal_env(), git_env()):
                self.assertFalse({'ANTHROPIC_API_KEY', 'TYPESAFE_API_KEY', 'SSH_AUTH_SOCK'} & env.keys())
                self.assertIn('PATH', env)


class ProviderTransportTests(SimpleTestCase):
    def test_redirects_are_refused(self):
        handler = ai.NoRedirect()
        request = urllib.request.Request('https://api.anthropic.com/v1/messages', headers={'x-api-key': 'secret'}, data=b'{}')
        self.assertIsNone(handler.redirect_request(request, None, 302, 'Found', {}, 'https://elsewhere.example/'))
        # With no follow-up request, urllib reports the 3xx as an HTTPError instead.
        self.assertIsNone(handler.http_error_302(request, None, 302, 'Found', {'location': 'https://elsewhere.example/'}))


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class DecisionEmailTests(TestCase):
    def test_submitter_wording_is_not_relayed_to_the_unverified_address(self):
        record = Submission.objects.create(kind='request', title='Claim your airdrop at https://evil.example',
                                           email='victim@example.com', status='declined')
        notify.notify(record)
        self.assertNotIn('evil.example', mail.outbox[0].body)
        self.assertIn('Thank you for your article request.', mail.outbox[0].body)

    def test_published_title_is_named(self):
        record = Submission.objects.create(kind='request', title='lightning', public_title='Lightning Network',
                                           email='reader@example.com', status='resolved')
        notify.notify(record)
        self.assertIn('about "Lightning Network"', mail.outbox[0].body)
