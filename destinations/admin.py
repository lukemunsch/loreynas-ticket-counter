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
        'area',
    )
    list_filter = ('area',)

    search_fields = ['district_name', 'area']


class DestinationAdmin(admin.ModelAdmin):
    """set up how we see our destination in admin page"""
    prepopulated_fields = {'slug': ('name',)}

    list_display = (
        'name',
        'district',
        'area',
        'price',
        'hotspot',
        'image',
    )

    list_filter = ('area','district',)

    search_fields = [
        'name',
        'area',
        'district',
        'description',
        'price'
    ]

    ordering = ('name', 'price',)


admin.site.register(Area, AreaAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Destination, DestinationAdmin)
