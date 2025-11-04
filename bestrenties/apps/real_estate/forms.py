# real_estate/forms.py

from django import forms
from .models import Property, AgentContact

class PropertySearchForm(forms.Form):
    # Formulaire pour la barre de recherche sur la page d'accueil et immobilière
    location_search = forms.CharField(
        max_length=255, 
        required=False, 
        label="Localisation",
        widget=forms.TextInput(attrs={'placeholder': 'Ville, quartier, pays...'})
    )
    transaction_type = forms.ChoiceField(
        choices=[('', 'Tous')] + Property.TRANSACTION_CHOICES, 
        required=False, 
        label="Type de transaction"
    )
    property_type = forms.ChoiceField(
        choices=[('', 'Tous')] + Property.PROPERTY_TYPE_CHOICES, 
        required=False, 
        label="Type de propriété"
    )
    min_budget = forms.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        required=False, 
        label="Budget Min.",
        widget=forms.NumberInput(attrs={'placeholder': 'Min. USD'})
    )
    max_budget = forms.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        required=False, 
        label="Budget Max.",
        widget=forms.NumberInput(attrs={'placeholder': 'Max. USD'})
    )

class AgentContactForm(forms.ModelForm):
    # Formulaire de contact pour un agent sur la page de détails de propriété
    class Meta:
        model = AgentContact
        fields = ['name', 'email', 'phone', 'message', 'property']
        widgets = {
            'property': forms.HiddenInput(), # Le champ property sera rempli par JS ou la vue
            'message': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'name': "Votre Nom",
            'email': "Votre E-mail",
            'phone': "Votre Téléphone (optionnel)",
            'message': "Votre Message",
        }