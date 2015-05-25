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
    
    form_type='general'
    if request.GET.get('form_type'):
        form_type = request.GET['form_type']

    # TODO(noelsison2): Get current user's associated restaurant
    restaurant = get_object_or_404(Restaurant, pk=1)

    if request.method == 'POST':
        if form_type == 'location':
            form = forms.RestaurantLocationForm(
                request.POST, instance=restaurant.location)
        elif form_type == 'extras':
            form = forms.RestaurantExtrasForm(
                request.POST, instance=restaurant)
        else:
            form = forms.RestaurantGeneralForm(
                request.POST, instance=restaurant)

        if form.is_valid():
            form.save()
    else:
        if form_type == 'location':
            form = forms.RestaurantLocationForm(instance=restaurant.location)
        elif form_type == 'extras':
            form = forms.RestaurantExtrasForm(instance=restaurant)
        else:
            form = forms.RestaurantGeneralForm(instance=restaurant)

    context = {'form': form, 'form_type': form_type}
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
