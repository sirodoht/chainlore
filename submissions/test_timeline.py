import importlib.util
import xml.etree.ElementTree as ET
from datetime import date
from unittest.mock import patch

from django.conf import settings
from django.test import SimpleTestCase

spec = importlib.util.spec_from_file_location('chainlore_build', settings.BASE_DIR / 'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


def event(value, text, slug='bitcoin', title='Bitcoin', table=1, draft=False, category='Layer 1'):
    return {'date': build.timeline_date(value), 'html': text, 'words': text, 'table': table,
            'views': build.event_views(text, category), 'sources': {slug: (title, f'/p/{slug}/#timeline', draft)}}


class TimelineDateTests(SimpleTestCase):
    def test_labels_keep_the_stated_precision(self):
        for value, label in (('2018', '2018'), ('2018-09', 'September 2018'), ('2018-09-26', '26 September 2018'),
                             ('2023-03-10–13', '10–13 March 2023')):
            self.assertEqual(build.timeline_date(value)['label'], label)

    def test_year_and_month_rows_sort_before_exact_days(self):
        dates = [build.timeline_date(value) for value in ('2018-09-26', '2018', '2018-09', '2018-01-01')]
        self.assertEqual([item['value'] for item in sorted(dates, key=lambda item: item['order'])],
                         ['2018', '2018-01-01', '2018-09', '2018-09-26'])

    def test_only_exact_dates_have_days(self):
        self.assertEqual(build.timeline_date('2018')['days'], [])
        self.assertEqual(build.timeline_date('2018-09')['days'], [])
        self.assertEqual(len(build.timeline_date('2023-03-10–13')['days']), 4)

    def test_unusable_dates_are_skipped_not_raised(self):
        for value in ('March 2018', 'c. 2018', '2018-13', '2018-02-30', '2018-09-26–20', ''):
            self.assertIsNone(build.timeline_date(value))


class TimelineRowTests(SimpleTestCase):
    def test_removing_a_citation_keeps_the_text_after_it(self):
        cell = ET.fromstring('<td>First.<sup id="a"><a href="#fn">1</a></sup> Second.<sup id="b">2</sup></td>')
        self.assertEqual(build.inline_html(cell, '/p/x/'), 'First. Second.')

    def test_rows_without_a_usable_date_do_not_stop_the_build(self):
        table = ET.fromstring('<div><h2 id="timeline">Timeline</h2><div><table><thead><tr><th>Date</th><th>Event</th></tr></thead><tbody>'
                              '<tr><td>2018</td><td>Launch</td></tr><tr><td>Spring 2019</td><td>Undated</td></tr></tbody></table></div></div>')
        rows = list(build.article_events('x', {'tree': table, 'title': 'X', 'meta': {'category': 'Other', 'status': 'draft'}}))
        self.assertEqual(rows[1], None)
        self.assertEqual(rows[0]['sources'], {'x': ('X', '/p/x/#timeline', True)})

    def test_only_tables_headed_date_are_read(self):
        table = ET.fromstring('<div><table><thead><tr><th>Halving</th></tr></thead><tbody><tr><td>2012</td></tr></tbody></table></div>')
        self.assertEqual(list(build.article_events('x', {'tree': table, 'title': 'X', 'meta': {}})), [])


class TimelineMergeTests(SimpleTestCase):
    def test_one_event_in_two_articles_is_merged_with_both_links(self):
        merged = build.merge_events([event('2025-07-18', 'GENIUS Act signed', 'tether', 'Tether'),
                                     event('2025-07-18', 'GENIUS Act signed into law', 'usdc', 'USDC')])
        self.assertEqual(len(merged), 1)
        self.assertEqual(set(merged[0]['sources']), {'tether', 'usdc'})
        self.assertEqual(merged[0]['words'], 'GENIUS Act signed into law')

    def test_related_events_on_one_day_stay_separate(self):
        merged = build.merge_events([event('2026-07-01', 'Robinhood Chain mainnet', 'arbitrum', 'Arbitrum'),
                                     event('2026-07-01', 'Uniswap deployed on Robinhood Chain', 'uniswap', 'Uniswap')])
        self.assertEqual(len(merged), 2)

    def test_rows_of_one_table_are_never_merged(self):
        merged = build.merge_events([event('2026-04-10', 'FDIC: Prudential standards'), event('2026-04-10', 'FDIC: Prudential standards')])
        self.assertEqual(len(merged), 2)

    def test_one_article_month_rows_merge_only_when_alike(self):
        merged = build.merge_events([event('2017-12', 'Reaches roughly US$19,200', table=1), event('2017-12', 'Bitcoin futures launch', table=2)])
        self.assertEqual(len(merged), 2)
        merged = build.merge_events([event('2020-03-12', 'Black Thursday', table=1), event('2020-03-12', 'Auctions cleared near zero', table=2)])
        self.assertEqual(len(merged), 1)

    def test_draft_wording_gives_way_to_checked_wording(self):
        merged = build.merge_events([event('2009-01-03', 'Genesis block mined in January', 'satoshi', 'Satoshi', draft=True),
                                     event('2009-01-03', 'Genesis block mined')])
        self.assertEqual(merged[0]['words'], 'Genesis block mined')


class TimelineViewTests(SimpleTestCase):
    def test_views_match_the_row(self):
        self.assertEqual(build.event_views('Bitfinex hack', 'Exchange'), {'hacks'})
        self.assertEqual(build.event_views('Celsius files for Chapter 11', 'Layer 1'), {'collapses'})
        self.assertEqual(build.event_views('GENIUS Act signed', 'Stablecoin'), {'laws'})
        self.assertEqual(build.event_views('Mainnet launches', 'Layer 1'), set())

    def test_regulation_articles_are_law_except_market_events_and_hacks(self):
        self.assertEqual(build.event_views('Provisional agreement', 'Regulation'), {'laws'})
        self.assertEqual(build.event_views('Coinbase Europe delists USDT', 'Regulation'), set())
        self.assertEqual(build.event_views('Coincheck hack', 'Regulation'), {'hacks'})


class OnThisDayTests(SimpleTestCase):
    def test_only_exact_past_dates_get_pages(self):
        events = [event('2023-03-10–13', 'USDC depegs'), event('2022-11', 'Month only'), event('2018', 'Year only'),
                  event('2027-01-18', 'Takes effect')]
        with patch.object(build, 'write_page') as write:
            routes = build.on_this_day(events, date(2026, 10, 31))
        self.assertEqual(routes, ['/on-this-day/', '/on-this-day/march-10/', '/on-this-day/march-11/',
                                  '/on-this-day/march-12/', '/on-this-day/march-13/'])
        index = write.call_args.args[2]
        self.assertIn('data-day="3-13"', index)
        self.assertNotIn('data-day="1-18"', index)

    def test_leap_day_is_a_day(self):
        with patch.object(build, 'write_page'):
            routes = build.on_this_day([event('2024-02-29', 'Consultation closes')], date(2026, 10, 31))
        self.assertIn('/on-this-day/february-29/', routes)

    def test_no_events(self):
        with patch.object(build, 'write_page'):
            self.assertEqual(build.on_this_day([], date(2026, 10, 31)), ['/on-this-day/'])
