from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from accounts import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from staff import utils
from django.core.urlresolvers import reverse

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
                    #redirect
                else:
                    context["error"] = "Username and password combination is invalid."
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
            if utils.username_present(form.cleaned_data["username"]):
                context["error"] = "User already exists."
            elif utils.email_present(form.cleaned_data["email"]):
                context["error"] = "Email is already in use."
            elif form.cleaned_data["confirm_password"] != form.cleaned_data["password"]:
                context["error"] = "Passwords do not match."
            else:
                user = User.objects.create_user(form.cleaned_data["username"], form.cleaned_data["email"], 
                                                form.cleaned_data["password"])
                user.first_name = form.cleaned_data["first_name"]
                user.last_name = form.cleaned_data["last_name"]
                user.save()
                return HttpResponseRedirect(reverse('index'))
        else:
            context["error"] = "Please check the details you submitted."
    context["form"] = form
    return render(request, 'accounts/signup.html', context)