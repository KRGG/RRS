from django.db import models
from django.contrib.auth.models import User

class ExtendedUser(User):
    class Meta:
        proxy = True

    def is_customer(self):
        return self.groups.filter(name='Customer').exists()
    
    def is_restaurant_staff(self):
        return self.groups.filter(name='Staff').exists()
    
class BaseProfile(models.Model):
    class Meta:
        abstract = True
        
    user = models.OneToOneField(ExtendedUser, primary_key=True)
    
    def __unicode__(self):
        return self.user.username

class CustomerProfile(BaseProfile):
    class Meta:
        permissions = (
            ("make_reservation", "Can make personal reservations"),
        )

    def clean(self):
        if hasattr(self.user, 'staffprofile'):
            raise ValidationError('User already has a staff profile')


class StaffProfile(BaseProfile):
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
