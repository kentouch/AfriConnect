"""from django.urls import path
from . import views

app_name = 'land_services'

urlpatterns = [
    path('', views.index, name='land_services_index'),
    # Add more paths for land services as needed
]"""

# land_services/urls.py

from django.urls import path
from . import views

app_name = 'land_services'

urlpatterns = [
    path('', views.land_services_view, name='land_services'),
    path('submit-request/', views.submit_land_service_request, name='submit_land_service_request'),
]