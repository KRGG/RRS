from django.conf.urls import patterns, url

from customer import views

urlpatterns = patterns(
   '',
    url(
        regex = r'^$',
        view  = views.index,
        name  = 'index'
    ),
    url(
        regex = r'^restaurant/(\d+)/$',
        view = views.restaurant,
        name="restaurant"
    )
)
