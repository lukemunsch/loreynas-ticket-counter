from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_destinations, name='destinations'),
    path('areas/', views.all_areas, name='areas'),
    path('districts/', views.all_districts, name='districts'),
    path('<int:destination_id>/', views.destination_detail, name='destination_detail'),
]
