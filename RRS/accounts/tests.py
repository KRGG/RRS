from django.test import TestCase
from django.contrib.auth.models import User, Group
from accounts.models import UserProfile

class UserProfileTests(TestCase):
    fixtures = ['db.json']

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
