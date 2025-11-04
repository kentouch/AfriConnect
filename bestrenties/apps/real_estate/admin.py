# real_estate/admin.py

from django.contrib import admin
from .models import Property, AgentContact

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'transaction_type', 'property_type', 'price', 'location_city', 'location_country', 'is_featured', 'published_date')
    list_filter = ('transaction_type', 'property_type', 'location_country', 'is_featured', 'is_low_cost')
    search_fields = ('title', 'description', 'location_city', 'location_address')
    #raw_id_fields = ('agent',) # Si vous liez à un utilisateur
    fieldsets = (
        (None, {
            'fields': ('title', 'description', ('transaction_type', 'property_type'), ('price', 'is_low_cost'))
        }),
        ('Localisation', {
            'fields': (('location_country', 'location_city'), 'location_address')
        }),
        ('Détails de la propriété', {
            'fields': (('bedrooms', 'bathrooms'), ('surface_area', 'land_area'), 'amenities')
        }),
        ('Spécifique au terrain agricole', {
            'fields': ('soil_type', 'water_access', 'current_crops'),
            'classes': ('collapse',) # Masque par défaut
        }),
        ('Images', {
            'fields': ('main_image', 'image1', 'image2', 'image3', 'image4')
        }),
        ('Marketing', {
            'fields': ('is_featured',)
        }),
        # ('Agent', {
        #     'fields': ('agent',)
        # }),
    )

@admin.register(AgentContact)
class AgentContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'property', 'contact_date')
    list_filter = ('contact_date', 'property__location_country')
    search_fields = ('name', 'email', 'message', 'property__title')
    readonly_fields = ('contact_date',)