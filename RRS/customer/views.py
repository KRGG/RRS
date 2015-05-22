from django.http import HttpResponse
from django.shortcuts import render

from .forms import SearchForm

def index(request):
    
    context = {'search_form': SearchForm()}
    return render(request, 'customer/index.html', context)

def restaurant(request, restaurant_id):
    
    context = {}
    return render(request, 'customer/restaurant.html', context)

def reservations(request):
    
    context = {}
    return render(request, 'customer/reservations.html', context)

def search(request):
    
    context = {}
    return render(request, 'customer/search.html', context)


# For functions with multiple context elements
def generic_response(request):
    one = 1
    two = 2
    three = 3
    context = {
        'one': one,
        'two': two,
        'tres': three,
    }
    return render(request, '', context)