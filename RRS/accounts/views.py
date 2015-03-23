from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from accounts import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

from staff import utils

# Create your views here.
def login(request):
    context={}
    if request.method =="GET":
        form = forms.LoginForm()
    if request.method =="POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print "TODO: authenticate and login user"
            #authenticate user
            user = authenticate(user=form.cleaned_data["username"],
                                password=form.cleaned_data["password"])
            if user is not None:
                print "TODO: authenticate and login user2"
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    context["error"] = "Username and password combination is invalid."
            else:
                context["error"] = "User does not exist."
        else:
            context["error"] = "Invalid login."
    context["form"] = form
    return render(request, 'accounts/login.html', context)
   
def signup(request):
    context = {}
    if request.method == "GET":
        form = forms.SignUpForm()
        print form
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data["username"], form.cleaned_data["email"], 
                                            form.cleaned_data["password1"])
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context["error"] = "Please check the details you submitted."
    context["form"] = form
    return render(request, 'accounts/signup.html', context)