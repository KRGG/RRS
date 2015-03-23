from django.test import TestCase


        self.assertEqual(response.status_code, 200)

class CustomerUrlsTests(TestCase):
    
    def test_index_view(self):
        response = self.client.get(reverse('view:index'))