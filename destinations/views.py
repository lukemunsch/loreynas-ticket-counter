from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Destination, Area, District
from .forms import AreaForm, DistrictForm, DestinationForm


# rendering views of models
def all_areas(request):
    """set up a page for all areas"""
    areas = Area.objects.all()
    context = {
        'areas': areas,
    }
    return render(request, 'destinations/areas.html', context)


def all_districts(request):
    """set up a page for all areas"""
    districts = District.objects.all()
    context = {
        'districts': districts,
    }
    return render(request, 'destinations/districts.html', context)


def all_destinations(request):
    """set up our index view"""
    destinations = Destination.objects.all()
    areas = Area.objects.all()
    districts = District.objects.all()

    query = None
    sort = None
    direction = None
    area = None
    district = None

    if request.GET:
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

        if 'area' in request.GET:
            area = request.GET['area']
            destinations = destinations.filter(area__area_name=area)
            districts = districts.filter(area__area_name=area)
            area = Area.objects.filter(area_name=area)

        if 'district' in request.GET:
            district = request.GET['district']
            destinations = destinations.filter(
                district__district_name=district)
            district = District.objects.filter(district_name=district)

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
        'current_area': area,
        'current_district': district,
    }
    return render(request, 'destinations/destinations.html', context)


# display details of specific destination
def destination_detail(request, destination_id):
    """set up view once we have selected a specific destination"""
    destination = get_object_or_404(Destination, pk=destination_id)

    context = {
        'destination': destination,
    }
    return render(request, 'destinations/destination_detail.html', context)


def add_area(request):
    """add a new area to the database"""
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Area Added Successfully!')
            return redirect(reverse('add_area'))
        else:
            messages.error(request, 'Failed to add area - Make sure all details are valid!')
    else:
        form = AreaForm()

    form = AreaForm()
    template = 'destinations/add_area.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_area(request, area_id):
    """set up form to edit an existing area"""
    area = get_object_or_404(Area, pk=area_id)
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES, instance=area)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated { area.friendly_area_name }')
            return redirect(reverse('destination_detail', args=[area.id]))
        else:
            messages.error(request, (
                'Failed to update area. '
                'Please make sure all details are correct.'
            ))
    else:
        form = AreaForm(instance=area)
        messages.info(request, f'You are editing { area.friendly_area_name }')

    


    template = 'destinations/edit_area.html'
    context = {
        'form': form,
        'area': area,
    }
    return render(request, template, context)


def add_district(request):
    """add a new district to the database"""
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New District Added Successfully!')
            return redirect(reverse('add_district'))
        else:
            messages.error(request, 'Failed to add district - Make sure all details are valid!')
    else:
        form = DistrictForm()

    form = DistrictForm()
    template = 'destinations/add_district.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def add_destination(request):
    """add a new destination to the database"""
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Destination Added Successfully!')
            return redirect(reverse('add_destination'))
        else:
            messages.error(request, 'Failed to add destination - Make sure all details are valid!')
    else:
        form = DestinationForm()

    form = DestinationForm()
    template = 'destinations/add_destination.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
