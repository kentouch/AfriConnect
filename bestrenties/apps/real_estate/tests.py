from django.test import TestCase
from .models import Property

class PropertyModelTest(TestCase):

    def setUp(self):
        Property.objects.create(
            title="Test Property",
            property_type="House",
            transaction_type="Sale",
            location="Dakar, Senegal",
            price=250000,
            description="A beautiful house in the heart of Dakar."
        )

    def test_property_creation(self):
        property = Property.objects.get(title="Test Property")
        self.assertEqual(property.property_type, "House")
        self.assertEqual(property.transaction_type, "Sale")
        self.assertEqual(property.location, "Dakar, Senegal")
        self.assertEqual(property.price, 250000)
        self.assertEqual(property.description, "A beautiful house in the heart of Dakar.")

    def test_property_str(self):
        property = Property.objects.get(title="Test Property")
        self.assertEqual(str(property), "Test Property")