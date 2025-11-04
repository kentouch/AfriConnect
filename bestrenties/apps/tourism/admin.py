"""from django.contrib import admin
from .models import TouristSite, Review

admin.site.register(TouristSite)
admin.site.register(Review)"""

# tourism/admin.py

from django.contrib import admin
from .models import TouristSite, TourRequest

@admin.register(TouristSite)
class TouristSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'category')
    list_filter = ('country', 'category')
    search_fields = ('name', 'description', 'city')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', ('country', 'city'), 'category')
        }),
        ('Images', {
            'fields': ('main_image', 'image1', 'image2')
        }),
        ('Localisation', {
            'fields': ('latitude', 'longitude')
        }),
    )

@admin.register(TourRequest)
class TourRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country_interest', 'travel_type', 'request_date')
    list_filter = ('country_interest', 'travel_type', 'request_date')
    search_fields = ('name', 'email', 'description')
    readonly_fields = ('request_date',)