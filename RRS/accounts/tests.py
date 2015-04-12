from django.test import TestCase
from django.contrib.auth.models import Group
from accounts import models

class UserProfileTests(TestCase):
    fixtures = ['db.json']
    CUSTOMER_GROUP = 'Customer'
    STAFF_GROUP = 'Staff'

    def setUp(self):
        USER_ID = 0
        self.test_user = models.ExtendedUser(USER_ID)
        self.test_user.save()

    def test__user_profile__returns_true_on_is_customer_if_part_of_customers_group(self): 
        self._add_to_group(self.CUSTOMER_GROUP)
        self.assertEqual(self.test_user.is_customer(), True)
        
    def test__staff_profile__returns_true_on_is_staff_if_part_of_staff_group(self): 
        self._add_to_group(self.STAFF_GROUP)
        self.assertEqual(self.test_user.is_restaurant_staff(), True)

    def test__user_profile__returns_false_on_is_customer_if_not_part_of_customers_group(self):
        self._assert_not_in_group(self.CUSTOMER_GROUP)
        self.assertEqual(self.test_user.is_customer(), False)
        
    def test__user_profile__returns_false_on_is_staff_if_part_of_staff_group(self):
        self._assert_not_in_group(self.STAFF_GROUP)
        self.assertEqual(self.test_user.is_restaurant_staff(), False)
        
    def _add_to_group(self, group_name):
        customers = Group.objects.get(name=group_name)
        customers.user_set.add(self.test_user)
        
    def _assert_not_in_group(self, group):
        return self.assertTrue(len(self.test_user.groups.filter(name=group)) == 0)
