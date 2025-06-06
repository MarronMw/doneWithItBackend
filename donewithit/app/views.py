from django.shortcuts import render

from .models import Listings

# Create your views here.


def trial(request):
    listings = Listings.objects.all()
    context = {"listings": listings}
    return render(request, "index.html", context)
