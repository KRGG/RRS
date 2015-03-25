from helpers import LinkSanityTestCase

class BaseLinksSanityTests(LinkSanityTestCase):
    
    def test__required_links__are_alive(self):
        self.check_if_online('index')
        