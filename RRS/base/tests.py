import django.test as django_test

# Create your tests here.

class LinksSanityTests(django_test.TestCase):
    
    def test__base_templates__are_alive(self):
        c = django_test.Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)