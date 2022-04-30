from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """set up admin to allow editing in admin page directly"""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """set up admin page for orer model"""
    readonly_fields = ('order_number', 'date', 'discount', 'order_total', 'grand_total',)
    inlines = (OrderLineItemAdminInline,)
    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'town_or_city', 'country',  'order_total', 'discount', 'grand_total',)
    list_display = ('order_number', 'date', 'full_name', 'order_total', 'discount', 'grand_total',)
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
