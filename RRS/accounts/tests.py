from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, Group
from accounts.models import UserProfile

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

class UserProfileTests(TestCase):
    fixtures = ['db.json']
    CUSTOMER_GROUP = 'Customer'
    STAFF_GROUP = 'Staff'

    def setUp(self):
        USER_ID = 0
        self.test_user = User(USER_ID)
        self.test_profile = UserProfile(user = self.test_user)
        self.test_user.save()

    def test__user_profile__returns_true_on_is_customer_if_part_of_customers_group(self): 
        self.test_profile.type = UserProfile.CUSTOMER
        self.assertEqual(self.test_profile.is_customer(), True)
        
    def test__staff_profile__returns_true_on_is_staff_if_part_of_staff_group(self): 
        self.test_profile.type = UserProfile.STAFF
        self.assertEqual(self.test_profile.is_restaurant_staff(), True)

    def test__user_profile__returns_false_on_is_customer_if_not_part_of_customers_group(self):
        self.test_profile.type = UserProfile.STAFF
        self.assertEqual(self.test_profile.is_customer(), False)
        
    def test__user_profile__returns_false_on_is_staff_if_part_of_staff_group(self):
        self.test_profile.type = UserProfile.CUSTOMER
        self.assertEqual(self.test_profile.is_restaurant_staff(), False)
        
    def _add_to_group(self, group_name):
        customers = Group.objects.get(name=group_name)
        customers.user_set.add(self.test_user)
        
    def _assert_not_in_group(self, group):
        return self.assertTrue(len(self.test_user.groups.filter(name=group)) == 0)