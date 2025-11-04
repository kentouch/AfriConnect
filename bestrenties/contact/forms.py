# contact/forms.py

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        labels = {
            'name': "Nom complet",
            'email': "Adresse e-mail",
            'phone': "Numéro de téléphone (optionnel)",
            'subject': "Sujet de votre demande",
            'message': "Votre message",
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }

