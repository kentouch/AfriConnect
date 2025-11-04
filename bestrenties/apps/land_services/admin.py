"""from django.contrib import admin
from .models import LandService

admin.site.register(LandService)"""

# land_services/admin.py

from django.contrib import admin
from .models import LandServiceRequest

@admin.register(LandServiceRequest)
class LandServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_type', 'country', 'request_date')
    list_filter = ('service_type', 'country', 'request_date')
    search_fields = ('name', 'email', 'description')
    readonly_fields = ('request_date',)