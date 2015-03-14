from django.conf.urls import patterns, url

from staff import views

urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = views.index,
        name  = 'index'
    ),
)
