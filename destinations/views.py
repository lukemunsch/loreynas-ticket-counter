from django.shortcuts import render
from .models import Destination, Area, District


def all_destinations(request):
    """set up our index view"""
    destinations = Destination.objects.all()
    areas = Area.objects.all()
    districts = District.objects.all()

    context = {
        'destinations': destinations,
        'areas': areas,
        'districts': districts,
    }
    return render(request, 'destinations/destinations.html', context)
