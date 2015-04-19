from django.test import TestCase, Client
from django.core.urlresolvers import resolve, reverse

from helpers import status

class LinkSanityTestCase(TestCase):
        
    def assert_valid_link(
            self,
            expected_url='',
            url_name='',
            status_code = status.HTTP_200_OK,
            **kwargs):
        reversed_url = reverse(url_name, **kwargs)
        self.assertEqual(expected_url, reversed_url)
        resolver = resolve(reversed_url)
        self.assertEqual(url_name, resolver.view_name)
        response = self.client.get(reversed_url)
        self.assertEqual(response.status_code, status_code)