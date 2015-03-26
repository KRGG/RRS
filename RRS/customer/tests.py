from django.test import TestCase

from helpers import LinkSanityTestCase


class CustomerLinksSanityTests(LinkSanityTestCase):
    
    def test__required_links__are_alive(self):
        sample_restaurant_id = 1
        
        self.assert_valid_link(
            expected_url='/restaurant/{}/'.format(sample_restaurant_id),
            url_name='customer:restaurant',
            args=[sample_restaurant_id]
        )
        
