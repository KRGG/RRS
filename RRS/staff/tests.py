from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from base import models as base_models
from helpers import LinkSanityTestCase
from staff.forms import RestaurantForm


def get_user_model():
    return User

class EditRestaurantTestCase(LinkSanityTestCase):

    def setUp(self):
        # Create user
        self.user = get_user_model().objects.create_user(
            'staff_username', 'staff@example.com', 'staff_password')
        
        # Create test restaurant
        area = base_models.Area.objects.create(name='area')
        location = base_models.Location.objects.create(address='address')
        menu = base_models.Menu.objects.create(
            name='menu name', description='menu description')
        cuisine = base_models.Cuisine.objects.create(name='cuisine')
        price_range = base_models.PriceRange.objects.create(name='price range')
        dress_code = base_models.DressCode.objects.create(name='dress code')
        payment_options = base_models.PaymentOption.objects.create(name='payment option')
        restaurant = base_models.Restaurant.objects.create(name='restaurant name', description='restaurant description', area=area, location=location, price_range=price_range, dress_code=dress_code,
                                               operating_hours='operating hours', contact_info='contact info', parking_info='parking info', additional_info='additional info', website='website')
        restaurant.cuisine.add(cuisine)
        restaurant.menu.add(menu)
        restaurant.payment_options.add(payment_options)
        restaurant.save()

        self.restaurant = restaurant
        
        # TODO(noelsison2) Associate user with restaurant

    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/staff/edit-restaurant/',
            url_name='staff:edit-restaurant',
        )

    def test__form_complete_data(self):
        complete_form_data = {'name': 'new restaurant name',
                     'description': 'new restaurant description',
                     'area': 1,
                     'location': 1,
                     'price_range': 1,
                     'dress_code': 1,
                     'cuisine': [1],
                     'payment_options': [1],
                     'menu': [1],
                     'operating_hours': 'new operating hours',
                     'contact_info': 'new_contact_info',
                     'parking_info': 'new parking info',
                     'additional_info': 'new additional info',
                     'website': 'new website'}
        
        form = RestaurantForm(data=complete_form_data)
        self.assertTrue(form.is_valid())

    def test__form_missing_required_data(self):
        required_form_fields = ['name', 'area', 'location', 'price_range', 'dress_code',
                                'cuisine', 'payment_options', 'operating_hours']
        
        response = self.client.post(reverse('staff:edit-restaurant'))
        
        for field in required_form_fields:
            self.assertFormError(
                response, 'form', field, 'This field is required.')

    def test__form_missing_optional_data(self):
        required_form_data = {'name': 'new restaurant name',
                     'area': 1,
                     'location': 1,
                     'price_range': 1,
                     'dress_code': 1,
                     'cuisine': [1],
                     'payment_options': [1],
                     'operating_hours': 'new operating hours'}
        
        form = RestaurantForm(data=required_form_data)
        self.assertTrue(form.is_valid())
