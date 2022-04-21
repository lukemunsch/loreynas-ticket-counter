from django.shortcuts import render
from .models import Destination


def all_destinations(request):
    """set up our index view"""
    destinations = Destination.objects.all()

    context = {
        'destinations': destinations,
    }
    return render(request, 'destinations/destinations.html', context)
