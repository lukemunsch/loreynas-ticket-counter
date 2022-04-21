from django.shortcuts import render, redirect, reverse, get_object_or_404
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


# def all_destinations(request):
#     """set up view ocne we have selected a specific destination"""
#     destination = get_object_or_404(klass)

#     context = {
#         'destinations': destinations,
#         'areas': areas,
#         'districts': districts,
#     }
#     return render(request, 'destinations/destinations.html', context)
