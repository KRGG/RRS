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
    
    url(r'^', include('customer.urls', namespace='customer')),
    
    url(r'^staff/', include('staff.urls', namespace='staff')),
    url(r'^admin/', include(admin.site.urls)),
    #url('^', include('django.contrib.auth.urls'), {'template_name': 'accounts/login.html'}),
    url(r'^allauth/', include('allauth.urls')),
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^test-dedicated/', include('test_dedicated.urls', namespace='test_dedicated')),
)
