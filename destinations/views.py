from django.shortcuts import render, get_object_or_404
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


def destination_detail(request, destination_id):
    """set up view once we have selected a specific destination"""
    destination = get_object_or_404(Destination, pk=destination_id)

    context = {
        'destination': destination,
    }
    return render(request, 'destinations/destination_detail.html', context)
