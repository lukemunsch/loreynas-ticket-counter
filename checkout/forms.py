from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """set up a form to capture the order details"""
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'town_or_city', 'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'town_or_city': 'Town or City',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for fields in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholders'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
