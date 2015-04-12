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
        
    user = models.OneToOneField(ExtendedUser)
    
    def __unicode__(self):
        return self.user.username

class CustomerProfile(BaseProfile):
    pass

class StaffProfile(BaseProfile):
    class Meta:
        permissions = (
            ("edit_restaurant", "Can edit a restaurant's details"),
        )
    restaurant = models.ForeignKey('base.Restaurant')
