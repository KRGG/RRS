from django.contrib import admin
from base.models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    

admin.site.register(Area)
admin.site.register(Location)
admin.site.register(Menu)
admin.site.register(Cuisine)
admin.site.register(PriceRange)
admin.site.register(DressCode)
admin.site.register(PaymentOption)
admin.site.register(Restaurant, RestaurantAdmin)