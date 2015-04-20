from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse

from accounts import views


urlpatterns = patterns(
   '',
    url(
        regex = r'signup/$',
        view = views.signup,
        name="signup"
    ),
    url(
        regex = r'login/$',
        view = views.login,
        name="login"
    ),
    url(
        regex = r'logout/$',
        view = views.logout,
        name="logout"
    )
)