from django.conf.urls import patterns, url

from test_dedicated import views

urlpatterns = patterns(
   '',
    url(
        regex = r'overflow/$',
        view = views.overflow,
        name="overflow"
    )
)
