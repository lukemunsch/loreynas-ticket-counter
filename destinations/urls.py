from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_destinations, name='destinations'),
    path(
        '<int:destination_id>/',
        views.destination_detail,
        name='destination_detail'
    ),
    path('add_destination/', views.add_destination, name='add_destination'),
    path(
        'edit_destination/<int:destination_id>',
        views.edit_destination,
        name='edit_destination'
    ),
    path(
        'delete_destination/<int:destination_id>',
        views.delete_destination,
        name='delete_destination'
    ),

    path('areas/', views.all_areas, name='areas'),
    path('add_area/', views.add_area, name='add_area'),
    path('edit_area/<int:area_id>', views.edit_area, name='edit_area'),
    path('delete_area/<int:area_id>', views.delete_area, name='delete_area'),

    path('districts/', views.all_districts, name='districts'),
    path('add_district/', views.add_district, name='add_district'),
    path(
        'edit_district/<int:district_id>',
        views.edit_district,
        name='edit_district'
    ),
    path(
        'delete_district/<int:district_id>',
        views.delete_district,
        name='delete_district'
    ),
]
