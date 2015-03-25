from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class LinkSanityTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()

    def check_if_online(self, url, **kwargs):
        response = self.client.get(reverse(url, **kwargs))
        self.assertEqual(response.status_code, 200)