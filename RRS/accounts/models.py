from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    permissions = (
        ("make_reservation", "Can make personal reservations"),
        ("make_manual_reservation", "Can make manual reservations"),
        ("edit_restaurant", "Can edit restaurant's details"),
        ("edit_menus", "Can edit restaurant's menus"),
        ("manage_staff", "Can manage restaurant's staff accounts"),
        ("customer_list", "Can view a list of restaurant's customers"),
        ("previous_reservations",
         "Can view a restaurant's reservation history"),
    )
    CUSTOMER= 1
    STAFF= 2
    PROFILE_TYPES= (
        (CUSTOMER, 'Customer'),
        (STAFF, 'Staff'),
    )
    user = models.OneToOneField(User, primary_key=True, related_name='user_profile')
    type = models.IntegerField(choices=PROFILE_TYPES, default=CUSTOMER)
    restaurant = models.ForeignKey('base.Restaurant', blank=True, null=True)

    def is_customer(self):
        return self.type == self.CUSTOMER
    
    def is_restaurant_staff(self):
        return self.type == self.STAFF
    
    def __unicode__(self):
        return self.user.username
