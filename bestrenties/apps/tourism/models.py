"""from django.db import models

class TouristSite(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    tourist_site = models.ForeignKey(TouristSite, related_name='reviews', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user_name} for {self.tourist_site.name}'"""
# tourism/models.py

from django.db import models

class TouristSite(models.Model):
    COUNTRY_CHOICES = [
        ('senegal', 'Sénégal'),
        ('burundi', 'Burundi'),
        ('rwanda', 'Rwanda'),
        ('gabon', 'Gabon'),
    ]
    CATEGORY_CHOICES = [
        ('nature', 'Nature & Faune'),
        ('culture', 'Culturel & Historique'),
        ('aventure', 'Aventure & Activités'),
        ('urbain', 'Urbain'),
        ('plage', 'Plage & Détente'),
    ]

    name = models.CharField(max_length=200, verbose_name="Nom du site touristique")
    description = models.TextField(verbose_name="Description détaillée")
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, verbose_name="Pays")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ville / Région")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Catégorie")
    main_image = models.ImageField(upload_to='tourist_sites/', blank=True, null=True, verbose_name="Image principale")
    # Ajoutez d'autres champs d'image si nécessaire
    image1 = models.ImageField(upload_to='tourist_sites/', blank=True, null=True)
    image2 = models.ImageField(upload_to='tourist_sites/', blank=True, null=True)
    
    # Coordonnées géographiques pour la carte
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_country_display()})"

    class Meta:
        verbose_name = "Site Touristique"
        verbose_name_plural = "Sites Touristiques"
        ordering = ['name']

class TourRequest(models.Model):
    TRAVEL_TYPE_CHOICES = [
        ('aventure', 'Aventure & Safari'),
        ('culturel', 'Culturel & Historique'),
        ('nature', 'Nature & Randonnée'),
        ('detente', 'Détente & Plages'),
        ('affaires', 'Affaires & Urbain'),
        ('other', 'Autre'),
    ]
    COUNTRY_CHOICES = [ # Dupliqué pour la clarté du formulaire, mais pourrait être lié
        ('senegal', 'Sénégal'),
        ('burundi', 'Burundi'),
        ('rwanda', 'Rwanda'),
        ('gabon', 'Gabon'),
        ('all', 'Tous / Plusieurs')
    ]

    name = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Adresse e-mail")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Numéro de téléphone")
    country_interest = models.CharField(max_length=20, choices=COUNTRY_CHOICES, verbose_name="Pays(s) d'intérêt")
    travel_type = models.CharField(max_length=50, choices=TRAVEL_TYPE_CHOICES, verbose_name="Type de voyage souhaité")
    description = models.TextField(verbose_name="Message / Besoins spécifiques")
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de la demande")

    def __str__(self):
        return f"Demande de voyage de {self.name} pour {self.get_country_interest_display()}"

    class Meta:
        verbose_name = "Demande de Voyage"
        verbose_name_plural = "Demandes de Voyages"
        ordering = ['-request_date']