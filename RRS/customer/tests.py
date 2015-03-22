from django.core.urlresolvers import reverse
from django.test import TestCase

import django.test as django_test
from django.core.urlresolvers import reverse

class LinksSanityTests(django_test.TestCase):
    
    def test__view_restaurant__is_alive(self):
        c = django_test.Client()
        response = c.get(
            reverse(
                'customer:view-restaurant',
                args=[1]))
        self.assertEqual(response.status_code, 200)