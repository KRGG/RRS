from helpers import LinkSanityTestCase

class CustomerLinksSanityTests(LinkSanityTestCase):
    
    def test__required_links__are_alive(self):
        self.check_if_online(
            'customer:restaurant',
            args=[1])
        