from django.test import TestCase

from helpers import LinkSanityTestCase

        
class SignUpTestCase(LinkSanityTestCase):
    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/signup/',
            url_name='accounts:signup',
        )
        
class LoginTestCase(LinkSanityTestCase):
    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/login/',
            url_name='accounts:login',
        )
    
class LogoutTestCase(LinkSanityTestCase):
    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/logout/',
            url_name='accounts:logout',
            status_code = 302
        )
    