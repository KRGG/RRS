from django.db import models
from django.contrib.auth.models import User

class UserProfile(User):
    class Meta:
        proxy = True

    def is_customer(self):
        return hasattr(self, 'customerprofile')
    
    def is_restaurant_staff(self):
        return hasattr(self, 'staffprofile')
    
class UserTypeProfile(models.Model):
    class Meta:
        abstract = True
        
    user = models.OneToOneField(UserProfile, primary_key=True)
    
    def __unicode__(self):
        return self.user.username

class CustomerProfile(UserTypeProfile):
    class Meta:
        permissions = (
            ("make_reservation", "Can make personal reservations"),
        )

    def clean(self):
        if hasattr(self.user, 'staffprofile'):
            raise ValidationError('User already has a staff profile')


class StaffProfile(UserTypeProfile):
    class Meta:
        permissions = (
            ("make_manual_reservation", "Can make manual reservations"),
            ("edit_restaurant", "Can edit restaurant's details"),
            ("edit_menus", "Can edit restaurant's menus"),
            ("manage_staff", "Can manage restaurant's staff accounts"),
            ("customer_list", "Can view a list of restaurant's customers"),
            ("previous_reservations",
             "Can view a restaurant's reservation history"),
        )

    restaurant = models.ForeignKey('base.Restaurant')

    def clean(self):
        if hasattr(self.user, 'customerprofile'):
            raise ValidationError('User already has a customer profile')
