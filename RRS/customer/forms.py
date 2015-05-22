from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit
from django import forms

from base import models as base_models


class SearchForm(forms.Form):
        
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'search-form'
        self.helper.add_input(Submit('search', 'Search', css_class='btn btn-primary form-element'))
        
    restaurant_property = forms.CharField(
        required=False, widget=forms.TextInput(attrs={
            'id': 'restaurant-property-input',
            'class': 'form-element',
            'placeholder': 'Restaurant, Cuisine, or Location'}))
    party_size = forms.CharField(
        required=False, widget=forms.TextInput(attrs={
            'id': 'party-size-input',
            'class': 'form-element with-trigger',
            'placeholder': 'People'}))
    date = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'id': 'date-input',
        'class': 'form-element with-trigger',
        'placeholder': 'Date'}))
    time = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'id': 'time-input',
        'class': 'form-element with-trigger',
        'placeholder': 'Time'}))
