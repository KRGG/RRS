from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from base.models import Restaurant
from staff import forms


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


def edit_restaurant(request):

    # TODO(noelsison2): Get current user's associated restaurant
    restaurant = get_object_or_404(Restaurant, pk=1)

    if request.method == 'POST':
        form_general = forms.RestaurantGeneralForm(
            request.POST, instance=restaurant)
        form_location = forms.RestaurantLocationForm(
            request.POST, instance=restaurant.location)
        form_extras = forms.RestaurantExtrasForm(
            request.POST, instance=restaurant)

        if form_general.is_valid():
            form_general.save()
        if form_location.is_valid():
            form_location.save()
        if form_extras.is_valid():
            form_extras.save()

    else:
        form_general = forms.RestaurantGeneralForm(instance=restaurant)
        form_location = forms.RestaurantLocationForm(
            instance=restaurant.location)
        form_extras = forms.RestaurantExtrasForm(instance=restaurant)

    context = {'form_general': form_general,
               'form_location': form_location,
               'form_extras': form_extras}
    
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
