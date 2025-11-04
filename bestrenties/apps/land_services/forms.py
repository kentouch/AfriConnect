# land_services/forms.py

# land_services/forms.py

from django import forms
from .models import LandServiceRequest

class LandServiceForm(forms.ModelForm):
    class Meta:
        model = LandServiceRequest
        fields = ['name', 'email', 'phone', 'country', 'service_type', 'description', 'desired_dates']
        labels = {
            'name': "Nom complet",
            'email': "Adresse e-mail",
            'phone': "Numéro de téléphone (optionnel)",
            'country': "Pays de la propriété",
            'service_type': "Type de service souhaité",
            'description': "Description détaillée du besoin",
            'desired_dates': "Dates / Délais souhaités (optionnel)",
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'desired_dates': forms.TextInput(attrs={'placeholder': 'Ex: Fin 2025, Urgence, etc.'}),
        }