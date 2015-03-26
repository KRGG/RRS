from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from base.models import Restaurant
from staff.forms import RestaurantForm


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
    
    # TODO(noelsison2): Get current user's associated restaurant
    restaurant = get_object_or_404(Restaurant, pk=1)
    
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
    else:
        form = RestaurantForm(instance=restaurant)
        
    context = {'form': form}
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
