from django.db import models
from django.contrib.auth.models import User

class UserProfile(User):
    class Meta:
        proxy = True

    def is_customer(self):
        return len(self.groups.filter(name='Customer')) > 0
    
    def is_restaurant_staff(self):
        return len(self.groups.filter(name='Staff')) > 0
    
class UserTypeProfile(models.Model):
    class Meta:
        abstract = True
        
    user = models.OneToOneField(UserProfile)
    
    def __unicode__(self):
        return self.user.username

class CustomerProfile(UserTypeProfile):
    pass

class StaffProfile(UserTypeProfile):
    class Meta:
        permissions = (
            ("edit_restaurant", "Can edit a restaurant's details"),
        )
    restaurant = models.ForeignKey('base.Restaurant')
