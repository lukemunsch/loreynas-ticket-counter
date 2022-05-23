from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

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
    hotspot = False

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                destinations = destinations.annotate(
                    lower_name=Lower('name')
                )
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

        if 'hotspot' in request.GET:
            hotspot = request.GET['hotspot']
            destinations = destinations.filter(
                hotspot=True
            )
            hotspot = Destination.objects.filter(hotspot=hotspot)

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
        'hotspot': hotspot,
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


@login_required
def add_area(request):
    """add a new area to the database"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Area Added Successfully!')
            return redirect(reverse('areas'))
        else:
            messages.error(
                request,
                'Failed to add area - Make sure all details are valid!'
            )
    else:
        form = AreaForm()

    form = AreaForm()
    template = 'destinations/add_area.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def add_district(request):
    """add a new district to the database"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New District Added Successfully!')
            return redirect(reverse('add_district'))
        else:
            messages.error(
                request,
                'Failed to add district - Make sure all details are valid!'
            )
    else:
        form = DistrictForm()

    form = DistrictForm()
    template = 'destinations/add_district.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def add_destination(request):
    """add a new destination to the database"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'New Destination Added Successfully!'
            )
            return redirect(reverse('add_destination'))
        else:
            messages.error(
                request,
                'Failed to add destination - Make sure all details are valid!'
            )
    else:
        form = DestinationForm()

    form = DestinationForm()
    template = 'destinations/add_destination.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# section for editing our database entries
@login_required
def edit_area(request, area_id):
    """set up form to edit an existing area"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    area = get_object_or_404(Area, pk=area_id)
    if request.method == 'POST':
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Successfully updated { area.friendly_area_name }'
            )
            return redirect(reverse('areas'))
        else:
            messages.error(request, (
                'Failed to update area. '
                'Please make sure all details are correct.'
            ))
    else:
        form = AreaForm(instance=area)
        messages.info(
            request,
            f'You are editing { area.friendly_area_name }'
        )

    template = 'destinations/edit_area.html'
    context = {
        'form': form,
        'area': area,
    }
    return render(request, template, context)


@login_required
def edit_district(request, district_id):
    """set up form to edit an existing district"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    district = get_object_or_404(District, pk=district_id)
    if request.method == 'POST':
        form = DistrictForm(request.POST, instance=district)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Successfully updated { district.friendly_district_name }'
            )
            return redirect(reverse('districts'))
        else:
            messages.error(request, (
                'Failed to update district. '
                'Please make sure all details are correct.'
            ))
    else:
        form = DistrictForm(instance=district)
        messages.info(
            request,
            f'You are editing { district.friendly_district_name }'
        )

    template = 'destinations/edit_district.html'
    context = {
        'form': form,
        'district': district,
    }
    return render(request, template, context)


@login_required
def edit_destination(request, destination_id):
    """set up form to edit an existing destination"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    destination = get_object_or_404(Destination, pk=destination_id)
    if request.method == 'POST':
        form = DestinationForm(
            request.POST,
            request.FILES,
            instance=destination
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Successfully updated { destination.name }'
            )
            return redirect(reverse('destinations'))
        else:
            messages.error(request, (
                'Failed to update destination. '
                'Please make sure all details are correct.'
            ))
    else:
        form = DestinationForm(instance=destination)
        messages.info(request, f'You are editing { destination.name }')

    template = 'destinations/edit_destination.html'
    context = {
        'form': form,
        'destination': destination,
    }
    return render(request, template, context)


# deleting section of our code
@login_required
def delete_area(request, area_id):
    """delete area with protection redirect"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    area = get_object_or_404(Area, pk=area_id)

    if request.method == 'POST':
        area.delete()
        messages.success(
            request,
            f'Successfully deleted {area.friendly_area_name}'
        )
        return redirect(reverse('areas'))

    template = 'destinations/delete_area.html'
    context = {
        'area': area,
    }
    return render(request, template, context)


@login_required
def delete_district(request, district_id):
    """delete district with protection redirect"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    district = get_object_or_404(District, pk=district_id)

    if request.method == 'POST':
        district.delete()
        messages.success(
            request, f'Successfully deleted {district.friendly_district_name}'
        )
        return redirect(reverse('districts'))

    template = 'destinations/delete_district.html'
    context = {
        'district': district,
    }
    return render(request, template, context)


@login_required
def delete_destination(request, destination_id):
    """delete destination with protection redirect"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, you are not permitted to access this page.'
        )
        return redirect(reverse('home'))

    destination = get_object_or_404(Destination, pk=destination_id)

    if request.method == 'POST':
        destination.delete()
        messages.success(request, f'Successfully deleted {destination.name}')
        return redirect(reverse('destinations'))

    template = 'destinations/delete_destination.html'
    context = {
        'destination': destination,
    }
    return render(request, template, context)
