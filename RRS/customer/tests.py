import django.test as django_test

class LinksSanityTests(django_test.TestCase):
    
    def test__view_restaurant__is_alive(self):
        c = django_test.Client()
        response = c.get('/view/1/')
        self.assertEqual(response.status_code, 200)