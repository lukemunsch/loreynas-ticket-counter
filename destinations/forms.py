from django import forms
from .models import Area, District, Destination
from .widgets import CustomClearableFileInput


class AreaForm(forms.ModelForm):
    """Set up the form to create an area"""
    class Meta:
        model = Area
        fields = '__all__'
        widgets = {
            'area_name': forms.TextInput(
                attrs={'placeholder': 'area_name_in_this_style_please'}
            ),
            'friendly_area_name': forms.TextInput(
                attrs={'placeholder': 'Normal Name Format'}
            )
        }


class DistrictForm(forms.ModelForm):
    """set up the form to create a district"""
    class Meta:
        model = District
        fields = '__all__'
        widgets = {
            'district_name': forms.TextInput(
                attrs={'placeholder': 'district_name_in_this_style_please'}
            ),
            'friendly_district_name': forms.TextInput(
                attrs={'placeholder': 'Normal Name Format'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        areas = Area.objects.all()
        friendly_names = [(a.id, a.get_friendly_area_name()) for a in areas]

        self.fields['area'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-darkgold rounded-1'


class DestinationForm(forms.ModelForm):
    """set up the form to create a district"""
    class Meta:
        model = Destination
        fields = [
            'name',
            'district',
            'area',
            'description',
            'hotspot',
            'price',
            'image_url',
            'image'
        ]

    district = forms.ModelChoiceField(
        queryset=District.objects.all()
    )
    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        areas = Area.objects.all()
        districts = District.objects.all()
        friendly_area_names = [(
            a.id, a.get_friendly_area_name()
        ) for a in areas]
        friendly_district_names = [(
            d.id, d.get_friendly_district_name()
        ) for d in districts]

        self.fields['area'].choices = friendly_area_names
        self.fields['district'].choices = friendly_district_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-darkgold rounded-1'
