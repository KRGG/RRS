from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit, Fieldset, Layout
from crispy_forms.bootstrap import TabHolder, Tab
from django import forms

from base import models as base_models


class RestaurantGeneralForm(forms.ModelForm):

    class Meta:
        model = base_models.Restaurant
        fields = ('name', 'description', 'price_range',
                  'dress_code', 'cuisine', 'payment_options',
                  'menu', 'operating_hours')

    def __init__(self, *args, **kwargs):
        super(RestaurantGeneralForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-restaurant-form'
        self.helper.add_input(Submit(
            'submit', 'Submit', css_class='btn btn-lg btn-primary inline-block pull-right'))
        self.helper.add_input(Button(
            'cancel', 'Cancel', css_class="btn btn-lg btn-default inline-block", onclick="window.location.reload();"))

    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 3}))
    operating_hours = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    dress_code = forms.ModelChoiceField(
        base_models.DressCode.objects.all(), empty_label=None)
    price_range = forms.ModelChoiceField(
        base_models.PriceRange.objects.all(), empty_label=None)


class RestaurantLocationForm(forms.ModelForm):

    class Meta:
        model = base_models.Location
        fields = ('area', 'address', 'longitude', 'latitude')

    def __init__(self, *args, **kwargs):
        super(RestaurantLocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-restaurant-form'
        self.helper.add_input(Submit(
            'submit', 'Submit', css_class='btn btn-lg btn-primary inline-block pull-right'))
        self.helper.add_input(Button(
            'cancel', 'Cancel', css_class="btn btn-lg btn-default inline-block", onclick="window.location.reload();"))

    area = forms.ModelChoiceField(
        base_models.Area.objects.all(), empty_label=None)


class RestaurantExtrasForm(forms.ModelForm):

    class Meta:
        model = base_models.Restaurant
        fields = ('contact_info', 'parking_info',
                  'additional_info', 'website')

    def __init__(self, *args, **kwargs):
        super(RestaurantExtrasForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-restaurant-form'
        self.helper.add_input(Submit(
            'submit', 'Submit', css_class='btn btn-lg btn-primary inline-block pull-right'))
        self.helper.add_input(Button(
            'cancel', 'Cancel', css_class="btn btn-lg btn-default inline-block", onclick="window.location.reload();"))

    contact_info = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 3}))
    parking_info = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 3}))
    additional_info = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 3}))
