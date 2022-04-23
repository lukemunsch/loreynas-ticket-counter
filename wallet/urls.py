from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_wallet, name='view_wallet'),
    path('add/<ticket_id>/', views.add_to_wallet, name='add_to_wallet'),
]
