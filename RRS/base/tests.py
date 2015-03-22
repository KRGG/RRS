from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class LinksSanityTests(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test__required_links__are_alive(self):
        self._check_if_online(reverse('index'))
        self._check_if_online(reverse(
            'customer:view-restaurant',
            args=[1]))
        
    def _check_if_online(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)