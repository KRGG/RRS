from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from accounts import models as accounts_models
from base import models as base_models
from helpers import LinkSanityTestCase

from staff.forms import RestaurantGeneralForm, RestaurantLocationForm, RestaurantExtrasForm


def get_user_model():
    return User


class EditRestaurantTestCase(LinkSanityTestCase):

    def setUp(self):
        # Create user
        self.user = get_user_model().objects.create_user(
            'staff_username', 'staff@example.com', 'staff_password')

        # Create test restaurant
        area = base_models.Area.objects.create(name='area')
        area.save()
        location = base_models.Location.objects.create(
            area=area, address='address', longitude=0, latitude=0)
        location.save()
        menu = base_models.Menu.objects.create(
            name='menu name', description='menu description')
        cuisine = base_models.Cuisine.objects.create(name='cuisine')
        price_range = base_models.PriceRange.objects.create(name='price range')
        dress_code = base_models.DressCode.objects.create(name='dress code')
        payment_options = base_models.PaymentOption.objects.create(
            name='payment option')
        restaurant = base_models.Restaurant.objects.create(name='restaurant name', description='restaurant description', location=location, price_range=price_range, dress_code=dress_code,
                                                           operating_hours='operating hours', contact_info='contact info', parking_info='parking info', additional_info='additional info', website='website')
        restaurant.cuisine.add(cuisine)
        restaurant.menu.add(menu)
        restaurant.payment_options.add(payment_options)
        restaurant.save()

        self.restaurant = restaurant

        # Form data
        self.complete_general_form_data = {
            'name': 'new restaurant name',
            'description': 'new restaurant description',
            'price_range': 1,
            'dress_code': 1,
            'cuisine': [1],
            'payment_options': [1],
            'menu': [1],
            'operating_hours': 'restaurant operating hours'
        }
        self.complete_location_form_data = {
            'area': 1,
            'address': 'address',
            'longitude': 0,
            'latitude': 0
        }
        self.complete_extras_form_data = {
            'contact_info': 'new_contact_info',
            'parking_info': 'new parking info',
            'additional_info': 'new additional info',
            'website': 'new website'
        }

        user_profile = accounts_models.UserProfile.objects.create(user=self.user, type=2, restaurant=restaurant)
        user_profile.save()
        
        self.client.login(email=self.user.email,password='staff_password')
        
    def test__required_links__are_alive(self):
        self.assert_valid_link(
            expected_url='/staff/edit-restaurant/',
            url_name='staff:edit-restaurant',
        )

    def test__general_form_complete_data(self):
        form = RestaurantGeneralForm(data=self.complete_general_form_data)
        self.assertTrue(form.is_valid())

    def test__location_form_complete_data(self):
        form = RestaurantLocationForm(data=self.complete_location_form_data)
        self.assertTrue(form.is_valid())

    def test__extras_form_complete_data(self):
        form = RestaurantExtrasForm(data=self.complete_extras_form_data)
        self.assertTrue(form.is_valid())

    def test__form_missing_required_data(self):
        required_restaurant_form_fields = [
            'name', 'price_range', 'dress_code',
            'cuisine', 'payment_options', 'operating_hours'
        ]
        required_area_form_fields = [
            'area', 'address', 'longitude', 'latitude'
        ]

        response = self.client.post(reverse('staff:edit-restaurant'))

        for field in required_restaurant_form_fields:
            self.assertFormError(
                response, 'form_general', field, 'This field is required.')

        for field in required_area_form_fields:
            self.assertFormError(
                response, 'form_location', field, 'This field is required.')

    def test__form_missing_optional_data(self):
        required_form_data = {
            'name': 'new restaurant name',
            'price_range': 1,
            'dress_code': 1,
            'cuisine': [1],
            'payment_options': [1],
            'operating_hours': 'new operating hours'
        }

        form = RestaurantGeneralForm(data=required_form_data)
        self.assertTrue(form.is_valid())

        form = RestaurantExtrasForm(data={})
        self.assertTrue(form.is_valid())
