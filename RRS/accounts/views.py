from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from accounts import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

   
def signup(request):
    context = {}
    if request.method == "GET":
        form = forms.SignUpForm()
    elif request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data["username"], form.cleaned_data["email"], 
                                            form.cleaned_data["password1"])
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()
            return HttpResponseRedirect(reverse('index'))
        context["error"] = "Please check the details you submitted."
    context["form"] = form
    return render(request, 'accounts/signup.html', context)