from allauth.account.forms import LoginForm as BaseLoginForm
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Field, Fieldset, HTML, Layout, Submit
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class SignUpForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_id = 'id-signup-form'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2'
            ),
            ButtonHolder(
                Submit('submit', 'Sign up now!',
                       css_class='btn btn-lg btn-primary btn-block')
            ))
        self.helper['email'].wrap(
            Field, placeholder='Email', css_class='form-input-top')
        self.helper['first_name'].wrap(Field, css_class='form-input-middle')
        self.helper['last_name'].wrap(Field, css_class='form-input-middle')
        self.helper['password1'].wrap(Field, css_class='form-input-middle')
        self.helper['password2'].wrap(
            Field, placeholder='Confirm Password', css_class='form-input-bottom')


class LoginForm(BaseLoginForm):
    remember = forms.BooleanField(label="Remember Me?", initial=False,
                                  required=False,
                                  widget=forms.CheckboxInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('login', placeholder='Email', css_class='form-input-top'),
                Field('password', placeholder='Password', css_class='form-input-bottom'),
                HTML("""
                    <div id="div_id_remember" class="checkbox">
                        <label>
                            <input id="id_remember" type="checkbox"> Remember me?
                        </label>
                    </div>
                    """)
            ),
            ButtonHolder(
                Submit(
                    'submit', 'Log in', css_class='btn btn-lg btn-primary btn-block')
            ))
