from django.contrib import admin
from .models import Area, District, Destination


class AreaAdmin(admin.ModelAdmin):
    """set up how we want to see the Area model in admin page"""
    list_display = (
        'area_name',
        'friendly_area_name',
    )
    ordering = ('area_name',)


class DistrictAdmin(admin.ModelAdmin):
    """set how we want to see our district model in admin"""
    list_display = (
        'district_name',
        'area_name',
    )
    list_filter = ('area_name',)

    search_fields = ['district_name', 'area_name']


class DestinationAdmin(admin.ModelAdmin):
    """set up how we see our destination in admin page"""
    prepopulated_fields = {'slug': ('dest_name',)}

    list_display = (
        'dest_name',
        'district_name',
        'area_name',
        'slug',
        'price',
        'hotspot',
    )

    list_filter = ('area_name','district_name',)

    search_fields = [
        'dest_name',
        'area_name',
        'district_name',
        'description',
        'price'
    ]

    ordering = ('dest_name', 'price',)


admin.site.register(Area, AreaAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Destination, DestinationAdmin)
