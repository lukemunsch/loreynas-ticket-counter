from django import forms
from .models import Area, District, Destination


class AreaForm(forms.ModelForm):
    """Set up the form to create an area"""
    class Meta:
        model = Area
        fields = '__all__'
