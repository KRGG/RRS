from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput())
    
class SignUpForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput())
    confirm_password = forms.CharField(widget= forms.PasswordInput())
    mobile = forms.CharField()