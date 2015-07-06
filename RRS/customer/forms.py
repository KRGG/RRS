from django import forms

from crispy_forms.bootstrap import InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit

from base import models as base_models


class SearchForm(forms.Form):
        
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_id = 'search-form'
        self.helper.layout = Layout(
            InlineField('restaurant_property', id='restaurant-property-input'),
            InlineField('party_size', id='party-size-input'),
            InlineField('date', id='date-input'),
            InlineField('time', id='time-input'),
            Div(Submit('search', 'Search', css_id='submit-button')))
        
    restaurant_property = forms.CharField(
        required=False,
        label='Restaurant, Cuisine, or Location')
    
    party_size = forms.CharField(
        required=False,
        label='People')
    
    date = forms.CharField(
        required=False)
    
    time = forms.CharField(
        required=False)
