from django.core.urlresolvers import reverse
from django.test import TestCase


class CustomerUrlsTests(TestCase):
    
    def test_index_view(self):
        response = self.client.get(reverse('view:index'))
        self.assertEqual(response.status_code, 200)