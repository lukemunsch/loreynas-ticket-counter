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
        self.destination = Destination.objects.create(
            name='test-dest',
            area=self.area,
            district=self.district,
            price=135.79,
            description='testing description'
        )
        self.password = 'MYpassword'
        self.email = 'test@testemail.com'
        self.username='tester123'
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            is_superuser=False
        )
        self.logged_in = self.client.login(
            username=self.username,
            email=self.email,
            password=self.password,
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

    def test_form_fails(self):
        """test that the form is not valid"""
        self.client.get(
            '/destinations/add_area/'
        )
        form = AreaForm({
            'area_name': '',
            'area_description': 'test description',
            'friendly_area_name': 'test name'
        })
        self.assertFalse(form.is_valid())

    def test_can_create_area(self):
        """test to create an area"""
        self.client.get(
            '/destinations/add_area/'
        )
        form = AreaForm({
            'area_name': 'test',
            'area_description': 'test description',
            'friendly_area_name': 'test name'
        })
        self.assertTrue(form.is_valid())
        form.save()
        response = self.client.post(
            '/destinations/add_area/'
        )
        areas = Area.objects.all()
        self.assertEqual(len(areas), 2)
        self.assertRedirects(response, '/')

    def test_can_get_edit_area_page(self):
        """test get edit area page"""
        response = self.client.get(f'/destinations/edit_area/{self.area.id}')
        self.assertEqual(response.status_code, 302)
        edit = self.client.post(
            f'/destinations/edit_area/{self.area.id}',
            {'area_name': 'upd_test_area'}
        )
        self.assertEqual(edit.status_code, 302)
        edit_area = Area.objects.get(id=self.area.id)
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
        districts = District.objects.all()
        self.assertTrue(len(districts), 2)

    def test_can_get_edit_district_page(self):
        """test for district edit page"""
        area = self.area
        district = self.district
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
        self.user.is_superuser=True
        logged_in = self.logged_in
        district = self.district
        response = self.client.get(
            f'/destinations/delete_district/{district.id}'
        )
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Http404):
            get_object_or_404(District, id=3)
        resp = self.client.post(
            f'/destinations/delete_district/{district.id}'
        )
        self.assertRedirects(response, '/')

class DestinationsTests(SetUpTestCase):
    """set up tests for destinations"""
    def test_destination_str_returns_destination_name(self):
        """check that our destination returns correct name"""
        self.assertEqual(str(self.destination), 'test-dest')

    def test_destination_name_form_fields_are_required(self):
        """test to make sure our form fields are required"""
        form = DestinationForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0],
            'This field is required.'
        )

    def test_get_destinations_list(self):
        """test to see if we can retrieve our list of destinations"""
        response = self.client.get('/destinations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/destinations.html')

    def test_get_add_destination_page(self):
        """test to open our add_destination page"""
        dest = Destination.objects.all()
        response = self.client.get('/destinations/add_destination/')
        self.assertEqual(response.status_code, 302)

    def test_can_create_destination(self):
        """test to create an destination"""
        form = DestinationForm({
            'name': 'test',
            'area': self.area,
            'district': self.district,
            'price': '123.45',
            'description': 'test descr'
        })
        self.assertTrue(form.is_valid())
        form.save()
        response = self.client.post(
            '/destinations/add_destination/',
            {'form': form}
        )
        destinations = Destination.objects.all()
        self.assertTrue(len(destinations), 1)

    def test_get_destinations_details_page(self):
        """test to get the specific destinations details page"""
        dest = self.destination
        response = self.client.get(f'/destinations/{dest.id}/')
        self.assertEqual(response.status_code, 200)

    def test_get_edit_destination_page(self):
        """test to get edit page"""
        self.user.is_superuser=True
        logged_in = self.logged_in
        dest = get_object_or_404(Destination, id=self.destination.id)
        response = self.client.post(
            f'/destinations/delete_destination/{dest.id}'
        )
        self.assertRedirects(response, '/')

    def test_can_sort_destinations_by_name(self):
        """test sort function"""
        self.client.get('/destinations/')
        sort = 'name'
        direction = 'asc'
        new_sort = self.client.get(
            f'/destinations/?sort={sort}&direction={direction}'
        )
        self.assertTrue(new_sort.status_code, 200)

    def test_can_sort_destinations_by_price(self):
        """test sort function"""
        self.client.get('/destinations/')
        sort = 'price'
        direction = 'asc'
        new_sort = self.client.get(
            f'/destinations/?sort={sort}&direction={direction}'
        )
        self.assertTrue(new_sort.status_code, 200)

    def test_can_filter_by_area(self):
        """test filtering by areas"""
        areas = Area.objects.all()
        area = self.area.area_name
        new_filter = self.client.get(
            f'/destinations/?area={area}'
        )
        self.assertTrue(new_filter.status_code, 200)

    def test_can_filter_by_district(self):
        """test for destiantion filtering by district"""
        districts = District.objects.all()
        district = self.district.district_name
        new_filter = self.client.get(
            f'/destinations/?district={district}'
        )
        self.assertTrue(new_filter.status_code, 200)

    def test_can_filter_by_hotspot(self):
        """test to get hotspots filtering"""
        dest = Destination.objects.all()
        self.assertEqual(len(dest), 1)
        new_filter = self.client.get(
            '/destinations/?hotspot=True'
        )
        self.assertTrue(new_filter.status_code, 200)

    def test_no_user_authorisations(self):
        """Test if user can add/edit/delete"""
        logged_in = self.logged_in
        self.assertFalse(self.user.is_superuser)
        response = self.client.get('/destinations/add_destination/')
        self.assertRedirects(response, '/')
        response1 = self.client.get('/destinations/add_district/')
        self.assertRedirects(response1, '/')
        response2 = self.client.get('/destinations/add_area/')
        self.assertRedirects(response2, '/')
        response3 = self.client.get('/destinations/edit_destination/1')
        self.assertRedirects(response3, '/')
        response4 = self.client.get('/destinations/edit_district/1')
        self.assertRedirects(response4, '/')
        response5 = self.client.get('/destinations/edit_area/1')
        self.assertRedirects(response5, '/')
        response6 = self.client.get('/destinations/delete_destination/1')
        self.assertRedirects(response6, '/')
        response7 = self.client.get('/destinations/delete_district/1')
        self.assertRedirects(response7, '/')
        response8 = self.client.get('/destinations/delete_area/1')
        self.assertRedirects(response8, '/')
