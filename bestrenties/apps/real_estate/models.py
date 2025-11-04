"""from django.db import models

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ]

    TRANSACTION_TYPE_CHOICES = [
        ('sale', 'Sale'),
        ('rent', 'Rent'),
    ]

    AVAILABILITY_STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
    ]

    title = models.CharField(max_length=200)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    availability_status = models.CharField(
        max_length=20,
        choices=AVAILABILITY_STATUS_CHOICES,
        default='available'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}, {self.country}"
    
# reviews for properties and services
class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for {self.property.title} - Rating: {self.rating}"""

# real_estate/models.py

from django.db import models
from django.contrib.auth.models import User # Si vous voulez lier les propriétés à des utilisateurs

class Property(models.Model):
    TRANSACTION_CHOICES = [
        ('sale', 'À Vendre'),
        ('rent', 'À Louer'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('house', 'Maison'),
        ('apartment', 'Appartement'),
        ('land', 'Terrain'),
        ('farmland', 'Terrain Agricole'),
        ('commercial', 'Commercial'),
    ]

    COUNTRY_CHOICES = [
        ('senegal', 'Sénégal'),
        ('burundi', 'Burundi'),
        ('rwanda', 'Rwanda'),
        ('gabon', 'Gabon'),
    ]

    title = models.CharField(max_length=200, verbose_name="Titre de la propriété")
    description = models.TextField(verbose_name="Description détaillée")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES, verbose_name="Type de transaction")
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, verbose_name="Type de propriété")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Prix (USD)")
    location_country = models.CharField(max_length=20, blank=True, choices=COUNTRY_CHOICES, verbose_name="Pays")
    location_city = models.CharField(max_length=100, blank=True, verbose_name="Ville")
    location_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse exacte")
    
    # Caractéristiques clés (pour flexibilité, on peut les rendre optionnelles ou textuelles)
    bedrooms = models.IntegerField(blank=True, null=True, verbose_name="Nombre de chambres")
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True, verbose_name="Nombre de salles de bain")
    surface_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Surface habitable (m²)")
    land_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Surface du terrain (m² ou hectares)")
    
    # Spécifique au terrain agricole
    soil_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Type de sol")
    water_access = models.CharField(max_length=100, blank=True, null=True, verbose_name="Accès à l'eau")
    current_crops = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cultures actuelles/passées")

    # Commodités (peut être un champ textuel ou un ManyToManyField si vous avez une liste fixe)
    amenities = models.TextField(blank=True, null=True, verbose_name="Commodités (séparées par des virgules)")
    
    # Images
    main_image = models.ImageField(upload_to='properties/', blank=True, null=True, verbose_name="Image principale")
    image1 = models.ImageField(upload_to='properties/', blank=True, null=True)
    image2 = models.ImageField(upload_to='properties/', blank=True, null=True)
    image3 = models.ImageField(upload_to='properties/', blank=True, null=True)
    image4 = models.ImageField(upload_to='properties/', blank=True, null=True)

    is_featured = models.BooleanField(default=False, verbose_name="Mise en avant")
    is_low_cost = models.BooleanField(default=False, verbose_name="Propriété à faible coût") # Déterminé par logique ou admin
    
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='properties_listed')

    def __str__(self):
        return f"{self.title} ({self.location_city}, {self.get_location_country_display()})"

    class Meta:
        verbose_name = "Propriété"
        verbose_name_plural = "Propriétés"
        ordering = ['-published_date']

class AgentContact(models.Model):
    # Modèle pour stocker les demandes de contact d'agent
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='agent_contacts')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact de {self.name} pour {self.property.title}"

    class Meta:
        verbose_name = "Contact Agent"
        verbose_name_plural = "Contacts Agents"