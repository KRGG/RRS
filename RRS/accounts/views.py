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
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["confirm_password"] == form.cleaned_data["password"]:
                print "Yay"
            else:
                context["error"] = "Passwords do not match."
        else:
            context["error"] = "Please check the details you submitted."
    context["form"] = form
    return render(request, 'accounts/signup.html', context)