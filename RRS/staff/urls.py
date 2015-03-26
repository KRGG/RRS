from django.conf.urls import patterns, url

from staff import views

urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = views.index,
        name  = 'index'
    ),
    url(
        regex = r'^edit-restaurant/$',
        view  = views.edit_restaurant,
        name  = 'edit-restaurant'
    ),
)
