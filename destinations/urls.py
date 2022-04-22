from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_destinations, name='destinations'),
    path('<int:destination_id>/', views.destination_detail, name='destination_detail'),
]
