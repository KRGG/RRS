
from django.conf.urls import patterns, include, url
from django.contrib import admin

from customer import views as customer_views
from accounts import views as accounts_views

urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = customer_views.index,
        name  = 'index'
    ),
    
    url(
        regex = r'admin/login/$',
        view = admin.site.login,
         ),
    
    url(
        regex = r'login/$',
        view = accounts_views.login,
        name = 'login'
    ),
    
    url(
        regex = r'signup/$',
        view = accounts_views.signup,
        name = 'signup'
    ),
    
    
    # Remove view/ namespace on deployment
    url(r'^view/', include('customer.urls', namespace='view')),
    url(r'^staff/', include('staff.urls', namespace='staff')),
    url(r'^admin/', include(admin.site.urls)),
)
