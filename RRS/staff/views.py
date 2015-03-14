from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    context = {}
    return render(request, 'staff/index.html', context)

def reservations(request):
    
    context = {}
    return render(request, 'staff/reservations.html', context)

def create_reservation(request):
    
    context = {}
    return render(request, 'staff/create_reservation.html', context)

def edit_restaurant(request):
    
    context = {}
    return render(request, 'staff/edit_restaurant.html', context)

def create_restaurant(request):
    
    context = {}
    return render(request, 'staff/create_restaurant.html', context)

def manage_accounts(request):
    
    context = {}
    return render(request, 'staff/manage_accounts.html', context)

def create_account(request):
    
    context = {}
    return render(request, 'staff/create_account.html', context)
