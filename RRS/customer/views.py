from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, customer. This is the index page.")

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