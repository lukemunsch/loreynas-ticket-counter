from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Destination, Area, District


def all_destinations(request):
    """set up our index view"""
    destinations = Destination.objects.all()
    areas = Area.objects.all()
    districts = District.objects.all()

    query = None
    # hotspots = None
    sort = None
    direction = None

    if request.GET:
        # filter for hotspots

        # filter for areas

        # filter for districts based on area

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                destinations = destinations.annotate(lower_name=Lower('name'))
            if sortkey == 'area':
                sortkey = 'area__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            destinations = destinations.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You forgot to add a search term!")
                return redirect(reverse('destinations'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            destinations = destinations.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'destinations': destinations,
        'areas': areas,
        'districts': districts,
        'search_term': query,
        'current_sorting': current_sorting,
    }
    return render(request, 'destinations/destinations.html', context)


def destination_detail(request, destination_id):
    """set up view once we have selected a specific destination"""
    destination = get_object_or_404(Destination, pk=destination_id)

    context = {
        'destination': destination,
    }
    return render(request, 'destinations/destination_detail.html', context)