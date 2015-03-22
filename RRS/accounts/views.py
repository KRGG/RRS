from django.shortcuts import render
from accounts import forms

# Create your views here.
def login(request):
    context={}
    if request.method =="GET":
        form = forms.LoginForm()
    context["form"] = form
    return render(request, 'accounts/login.html', context)

    
def signup(request):
    context = {}
    if request.method == "GET":
        form = forms.SignUpForm()
    context["form"] = form
    return render(request, 'accounts/signup.html', context)