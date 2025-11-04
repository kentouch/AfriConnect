"""from django.urls import path
from . import views

app_name = 'real_estate'

urlpatterns = [
    path('', views.index, name='real_estate_index'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='property_list'),
    path('properties/<int:property_id>/', views.property_detail, name='property_detail'),
    # Add more paths for real estate as needed
]"""
# real_estate/urls.py

from django.urls import path
from . import views

app_name = 'real_estate'

urlpatterns = [
    path('', views.home_view, name='home'), # Page d'accueil
    path('properties/', views.property_list_view, name='property_list'), # Liste des propriétés
    path('properties/<int:pk>/', views.property_detail_view, name='property_detail'), # Détails d'une propriété
    path('api/contact-agent/', views.contact_agent_view, name='contact_agent_api'), # API pour le formulaire de contact agent
]