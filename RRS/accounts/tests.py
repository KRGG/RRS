from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from accounts import views
from helpers import LinkSanityTestCase


def assert_view_response_to_user(test_case, url_name, user, response_code):
    reversed_url = reverse('accounts:signup')
    request = RequestFactory().get(reversed_url)
    request.user = user
    response = views.signup(request)
    test_case.assertEqual(response.status_code, response_code)


class SignUpTestCase(LinkSanityTestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/signup/',
            url_name='accounts:signup',
        )

    def test__logged_in_user_redirect(self):
        """A logged in user should be redirected"""
        assert_view_response_to_user(self, 'accounts:signup', User(0), 302)

    def test__anonymous_user_ok(self):
        """User that is not logged in should be able to view this page"""
        assert_view_response_to_user(
            self, 'accounts:signup', AnonymousUser(), 200)


class LoginTestCase(LinkSanityTestCase):

    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/login/',
            url_name='accounts:login',
        )

    def test__logged_in_user_redirect(self):
        """A logged in user should be redirected"""
        assert_view_response_to_user(self, 'accounts:signup', User(0), 302)

    def test__anonymous_user_ok(self):
        """User that is not logged in should be able to view this page"""
        assert_view_response_to_user(
            self, 'accounts:signup', AnonymousUser(), 200)


class LogoutTestCase(LinkSanityTestCase):

    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/logout/',
            url_name='accounts:logout',
            status_code=302
        )
