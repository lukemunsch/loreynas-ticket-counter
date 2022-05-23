from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import (
    Area,
    District,
    Destination
)
from .forms import (
    AreaForm,
    DistrictForm,
    DestinationForm
)
from .views import (
    add_area,
    add_district,
    add_destination,
    edit_area,
    edit_district,
    edit_destination,
    delete_area,
    delete_district,
    delete_destination,
    all_areas,
    all_districts,
    all_destinations,
)


class TestAreas(TestCase):
    """Testing the code related to our areas"""
    def test_area_str_returns_area_name(self):
        """test to get our list of areas"""
        area = Area.objects.create(area_name='test')
        self.assertEqual(str(area), 'test')

    def test_get_friendly_area_name(self):
        """test to get friendly area name"""
        area = Area.objects.create(
            area_name='test_area',
            friendly_area_name='test area')
        self.assertEqual(area.friendly_area_name, 'test area')

    def test_area_name_form_fields_are_required(self):
        """test to make sure ur form fields are required"""
        form = AreaForm({'area_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('area_name', form.errors.keys())
        self.assertEqual(
            form.errors['area_name'][0],
            'This field is required.'
        )

    def test_get_area_list(self):
        """test to see if we can retrieve our list of areas"""
        response = self.client.get('/destinations/areas/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/areas.html')

    def test_add_area_page(self):
        """test to open our add_area page"""
        response = self.client.get('/destinations/add_area/')
        self.assertEqual(response.status_code, 302)

    def test_can_get_edit_area_page(self):
        """test get edit area page"""
        area = Area.objects.create(area_name='test_name')
        response = self.client.get(f'/destinations/edit_area/{area.id}')
        self.assertEqual(response.status_code, 302)
        edit = self.client.post(
            f'/destinations/edit_area/{area.id}',
            {'area_name': 'upd_test_area'}
        )
        self.assertEqual(edit.status_code, 302)
        edit_area = Area.objects.get(id=area.id)
        self.assertTrue(edit_area.area_name, 'upd_test_area')

    def test_delete_area(self):
        """test can get delete area page and delete area"""
        area = Area.objects.create(area_name='test')
        response = self.client.get(
            f'/destinations/delete_area/{area.id}'
        )
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Http404):
            get_object_or_404(Area, id=2)
