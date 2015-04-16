from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.core.urlresolvers import reverse

from forms import LoginForm, SignUpForm

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            user = authenticate(username=user.username, 
                                password=form.cleaned_data['password1'])
            django_login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SignUpForm()
        
    context = { 'form': form }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return form.login(request, reverse('index'))
    else:
        form = LoginForm()
        
    context = { 'form': form }
    return render(request, 'accounts/login.html', context)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('index'))