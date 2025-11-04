"""from django.db import models

class LandService(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('survey', 'Survey'),
        ('consultation', 'Consultation'),
        ('registration', 'Registration'),
        ('transfer', 'Transfer'),
    ]

    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    description = models.TextField()
    user_request = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_type} service in {self.location}"""

# land_services/models.py

from django.db import models

class LandServiceRequest(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('defrichage', 'Préparation et Défrichage des Terres'),
        ('analyse-sols', 'Analyse et Amélioration des Sols'),
        ('irrigation', 'Installation de Systèmes d\'Irrigation'),
        ('accompagnement-agricole', 'Accompagnement Achat/Location Terrains Agricoles'),
        ('other', 'Autre / Demande Générale'),
    ]
    COUNTRY_CHOICES = [
        ('senegal', 'Sénégal'),
        ('burundi', 'Burundi'),
        ('rwanda', 'Rwanda'),
        ('gabon', 'Gabon'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Adresse e-mail")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Numéro de téléphone")
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, verbose_name="Pays de la propriété")
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES, verbose_name="Type de service souhaité")
    description = models.TextField(verbose_name="Description détaillée du besoin")
    desired_dates = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dates / Délais souhaités")
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de la demande")

    def __str__(self):
        return f"Demande de service de {self.name} pour {self.get_service_type_display()}"

    class Meta:
        verbose_name = "Demande de Service Foncier"
        verbose_name_plural = "Demandes de Services Fonciers"
        ordering = ['-request_date']