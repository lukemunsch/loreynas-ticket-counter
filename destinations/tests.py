from django.contrib.auth.models import User
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


class SetUpTestCase(TestCase):
    """Set up prebuilds for areas, districts and users"""
    def setUp(self):
        """set up prebuilt area, district and user"""
        self.area = Area.objects.create(area_name='test-a')
        self.district = District.objects.create(
            district_name='test-d',
            area=self.area
        )
        self.password = 'MYpassword'
        self.email = 'test@testemail.com'
        self.username='tester123'
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )

class TestAreas(SetUpTestCase):
    """Testing the code related to our areas"""
    def test_area_str_returns_area_name(self):
        """test to get our list of areas"""
        self.assertEqual(str(self.area), 'test-a')

    def test_area_name_form_fields_are_required(self):
        """test to make sure our form fields are required"""
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

    def test_get_add_area_page(self):
        """test to open our add_area page"""
        response = self.client.get('/destinations/add_area/')
        self.assertEqual(response.status_code, 302)

    def test_can_create_area(self):
        """test to create an area"""
        form = AreaForm({
            'area_name': 'test',
            'area_description': 'test description',
            'friendly_area_name': 'test name'
        })
        self.assertTrue(form.is_valid())
        form.save()
        areas = Area.objects.all()
        self.assertEqual(len(areas), 2)

    def test_can_get_edit_area_page(self):
        """test get edit area page"""
        area = Area.objects.create(area_name='test-b')
        response = self.client.get(f'/destinations/edit_area/{area.id}')
        self.assertEqual(response.status_code, 302)
        edit = self.client.post(
            f'/destinations/edit_area/{area.id}',
            {'area_name': 'upd_test_area'}
        )
        self.assertEqual(edit.status_code, 302)
        edit_area = Area.objects.get(id=area.id)
        self.assertTrue(edit_area.area_name, 'upd_test_area')

    def test_get_delete_area_page(self):
        """test can get delete area page"""
        area = Area.objects.create(area_name='test')
        response = self.client.get(
            f'/destinations/delete_area/{area.id}'
        )
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Http404):
            get_object_or_404(Area, id=3)

class TestDistricts(SetUpTestCase):
    """set up tests for the districts section"""
    def test_district_str_returns_district_name(self):
        """test to get our list of districts"""
        self.assertEqual(str(self.district), 'test-d')

    def test_get_district_list(self):
        """test to see if we can retrieve our list of districts"""
        response = self.client.get('/destinations/districts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/districts.html')

    def test_get_add_district_page(self):
        """test to open our add_district page"""
        district = District.objects.all()
        response = self.client.get('/destinations/add_district/')
        self.assertEqual(response.status_code, 302)
    
    def test_can_create_district(self):
        """test to create an district"""
        form = DistrictForm({
            'district_name': 'test',
            'area': self.area,
            'friendly_district_name': 'test name'
        })
        self.assertTrue(form.is_valid())
        form.save()
        response = self.client.post(
            '/destinations/add_district/',
            {'form': form}
        )
        self.assertRedirects(response, '/')
        districts = District.objects.all()
        self.assertTrue(len(districts), 2)

    def test_can_get_edit_district_page(self):
        """test for district edit page"""
        area = Area.objects.create(area_name='test_name')
        district = District.objects.create(
            district_name='test',
            area=area
        )
        response = self.client.get(f'/destinations/edit_district/{district.id}')
        self.assertEqual(response.status_code, 302)
        edit = self.client.post(
            f'/destinations/edit_district/{district.id}',
            {'district_name': 'upd_test_district'}
        )
        self.assertEqual(edit.status_code, 302)
        edit_district = District.objects.get(id=district.id)
        self.assertTrue(edit_district.district_name, 'upd_test_district')

    def test_get_delete_district_page(self):
        """test can get delete district page"""
        area = Area.objects.create(area_name='test-area')
        district = District.objects.create(
            district_name='test',
            area=area
        )
        response = self.client.get(
            f'/destinations/delete_district/{district.id}'
        )
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Http404):
            get_object_or_404(District, id=3)

class DestinationsTests(SetUpTestCase):
    """set up tests for destinations"""
    def test_destination_str_returns_destination_name(self):
        """check that our destination returns correct name"""
        dest = Destination.objects.create(name='test', area=self.area, district=self.district, price=123.45)
        self.assertEqual(str(dest), 'test')
