from helpers import LinkSanityTestCase

class BaseLinksSanityTests(LinkSanityTestCase):
    
    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/',
            url_name='index'
        )
        