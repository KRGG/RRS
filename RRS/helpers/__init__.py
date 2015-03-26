from django.test import TestCase, Client
from django.core.urlresolvers import resolve, reverse

class LinkSanityTestCase(TestCase):
        
    def assert_valid_link(
            self,
            expected_url='',
            url_name='',
            **kwargs):
        reversed_url = reverse(url_name, **kwargs)
        self.assertEqual(expected_url, reversed_url)
        resolver = resolve(reversed_url)
        self.assertEqual(url_name, resolver.view_name)