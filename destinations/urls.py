from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_destinations, name='destinations'),
    path('areas/', views.all_areas, name='areas'),
    path('add_area/', views.add_area, name='add_area'),
    path('add_district/', views.add_district, name='add_district'),
    path('add_destination/', views.add_destination, name='add_destination'),
    path('districts/', views.all_districts, name='districts'),
    path('<int:destination_id>/', views.destination_detail, name='destination_detail'),
]
