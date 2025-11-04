# tourism/forms.py

from django import forms
from .models import TourRequest

class TourRequestForm(forms.ModelForm):
    class Meta:
        model = TourRequest
        fields = ['name', 'email', 'phone', 'country_interest', 'travel_type', 'description']
        labels = {
            'name': "Nom complet",
            'email': "Adresse e-mail",
            'phone': "Numéro de téléphone (optionnel)",
            'country_interest': "Pays(s) d'intérêt",
            'travel_type': "Type de voyage souhaité",
            'description': "Message / Besoins spécifiques",
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }