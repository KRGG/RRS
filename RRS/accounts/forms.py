from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput())
    
class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput())
    conf_password = forms.CharField(widget= forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()