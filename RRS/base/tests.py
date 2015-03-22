import django.test as django_test
from django.core.urlresolvers import reverse

class LinksSanityTests(django_test.TestCase):
    
    def test__required_links__are_alive(self):
        self._check_if_online(reverse('index'))
        self._check_if_online(reverse(
            'customer:view-restaurant',
            args=[1]))
        
    def _check_if_online(self, url):
        c = django_test.Client()
        response = c.get(url)
        self.assertEqual(response.status_code, 200)