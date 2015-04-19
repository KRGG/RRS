import json

from allauth.account import signals as allauth_signals
from allauth.socialaccount import models as allauth_models
from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from accounts import views, forms, receivers
from helpers import LinkSanityTestCase, status


NEW_RECORD = 0
FIRST_NAME = 'Firstname'
LAST_NAME = 'Lastname'
FULL_NAME = FIRST_NAME + ' ' + LAST_NAME


def assert_view_response_to_user(test_case, url_name, user, response_code):
    reversed_url = reverse('accounts:signup')
    request = RequestFactory().get(reversed_url)
    request.user = user
    response = views.signup(request)
    test_case.assertEqual(response.status_code, response_code)


def test_social_signed_up_signal(test_case, provider, user):
    if provider == receivers.PROVIDER_FACEBOOK:
        extra_data = {receivers.FACEBOOK_FIRST_NAME_DATA: FIRST_NAME,
                      receivers.FACEBOOK_LAST_NAME_DATA: LAST_NAME}
    elif provider == receivers.PROVIDER_GOOGLE:
        extra_data = {receivers.GOOGLE_FIRST_NAME_DATA: FIRST_NAME,
                      receivers.GOOGLE_LAST_NAME_DATA: LAST_NAME}
    elif provider == receivers.PROVIDER_TWITTER:
        extra_data = {receivers.FULL_NAME_DATA: FULL_NAME}

    socialAccount = allauth_models.SocialAccount(
        user=user, provider=provider, extra_data=json.dumps(extra_data))
    social_login = allauth_models.SocialLogin(
        user=user, account=socialAccount)

    allauth_signals.user_signed_up.connect(
        receiver=receivers.user_signed_up, sender='test')
    allauth_signals.user_signed_up.send(
        sender='test', request=None, user=user, social_login=social_login)

    test_case.assertEqual(user.first_name, FIRST_NAME)
    test_case.assertEqual(user.last_name, LAST_NAME)


class SignUpTestCase(LinkSanityTestCase):

    def setUp(self):
        self.url_name = 'accounts:signup'
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'customer_username', 'customer@example.com', 'customer_password')
        self.user.save()

    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/signup/',
            url_name=self.url_name,
        )

    def test__logged_in_user_redirect(self):
        '''A logged in user should be redirected'''
        assert_view_response_to_user(
            self, self.url_name, self.user, status.HTTP_302_FOUND)

    def test__anonymous_user_ok(self):
        '''User that is not logged in should be able to view this page'''
        assert_view_response_to_user(
            self, self.url_name, AnonymousUser(), 200)

    def test__form_complete_data(self):
        complete_form_data = {'email': 'email@example.com',
                              'first_name': 'firstname',
                              'last_name': 'lastname',
                              'password1': 'password',
                              'password2': 'password'}

        form = forms.SignUpForm(data=complete_form_data)
        self.assertTrue(form.is_valid())

    def test__form_missing_required_data(self):
        required_form_fields = [
            'email', 'first_name', 'last_name', 'password1', 'password2']

        reverse_url = reverse(self.url_name)
        response = self.client.post(reverse_url)

        for field in required_form_fields:
            self.assertFormError(
                response, 'form', field, 'This field is required.')

    def test__form_wrong_data(self):
        wrong_form_data = {'email': 'not an email',
                           'first_name': '',
                           'last_name': '',
                           'password1': 'password1',
                           'password2': 'password2'}

        form = forms.SignUpForm(data=wrong_form_data)
        self.assertFalse(form.is_valid())

    def test__user_signed_up_signal_facebook(self):
        test_social_signed_up_signal(
            test_case=self, provider=receivers.PROVIDER_FACEBOOK, user=self.user)

    def test__user_signed_up_signal_google(self):
        test_social_signed_up_signal(
            test_case=self, provider=receivers.PROVIDER_GOOGLE, user=self.user)

    def test__user_signed_up_signal_twitter(self):
        test_social_signed_up_signal(
            test_case=self, provider=receivers.PROVIDER_TWITTER, user=self.user)


class LoginTestCase(LinkSanityTestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            'customer_username', 'customer@example.com', 'customer_password')
        self.user.save()
        self.url_name = 'accounts:login'

    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/login/',
            url_name=self.url_name,
        )

    def test__logged_in_user_redirect(self):
        '''A logged in user should be redirected'''
        assert_view_response_to_user(
            self, self.url_name, User(NEW_RECORD), status.HTTP_302_FOUND)

    def test__anonymous_user_ok(self):
        '''User that is not logged in should be able to view this page'''
        assert_view_response_to_user(
            self, self.url_name, AnonymousUser(), status.HTTP_200_OK)

    def test__form_valid_data(self):
        valid_form_data = {'login': 'customer@example.com',
                           'password': 'customer_password'}

        form = forms.LoginForm(data=valid_form_data)
        self.assertTrue(form.is_valid())

    def test__form_missing_required_data(self):
        required_form_fields = ['login', 'password']

        reverse_url = reverse(self.url_name)
        response = self.client.post(reverse_url)

        for field in required_form_fields:
            self.assertFormError(
                response, 'form', field, 'This field is required.')

    def test__form_wrong_data(self):
        wrong_form_data = {'login': 'email@example.com',
                           'password': 'password'}

        form = forms.LoginForm(data=wrong_form_data)
        self.assertFalse(form.is_valid())


class LogoutTestCase(LinkSanityTestCase):

    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/logout/',
            url_name='accounts:logout',
            status_code=status.HTTP_302_FOUND
        )
