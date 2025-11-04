from django.db import models

# Create your models here.
# contact/models.py

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Adresse e-mail")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Numéro de téléphone")
    subject = models.CharField(max_length=200, verbose_name="Sujet de la demande")
    message = models.TextField(verbose_name="Votre message")
    sent_date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")

    def __str__(self):
        return f"Message de {self.name} - {self.subject}"

    class Meta:
        verbose_name = "Message de Contact"
        verbose_name_plural = "Messages de Contact"
        ordering = ['-sent_date']