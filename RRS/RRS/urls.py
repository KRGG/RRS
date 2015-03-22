from django.conf.urls import patterns, include, url
from django.contrib import admin

from customer import views as customer_views


urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = customer_views.index,
        name  = 'index'
    ),
    
    url(r'^', include('customer.urls', namespace='customer')),
    url(r'^staff/', include('staff.urls', namespace='staff')),
    url(r'^admin/', include(admin.site.urls)),
)
