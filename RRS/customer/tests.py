from helpers import LinkSanityTestCase

class CustomerLinksSanityTests(LinkSanityTestCase):
    
    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/restaurant/1/',
            url_name='customer:restaurant',
            args=[1]
        )
        