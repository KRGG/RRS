import django.test as django_test
from django.core.urlresolvers import reverse

class LinksSanityTests(django_test.TestCase):
    
    def test__base_templates__are_alive(self):
        c = django_test.Client()
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)