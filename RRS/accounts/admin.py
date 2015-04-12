from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import *

class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_restaurant_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')

admin.site.unregister(User)
admin.site.register(ExtendedUser, UserProfileAdmin)
admin.site.register(CustomerProfile)
admin.site.register(StaffProfile)
