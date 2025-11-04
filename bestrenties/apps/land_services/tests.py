from django.test import TestCase
from .models import LandService

class LandServiceModelTest(TestCase):
    def setUp(self):
        LandService.objects.create(service_type="Land Survey", location="Dakar")
        LandService.objects.create(service_type="Land Registration", location="Banjul")

    def test_land_service_creation(self):
        land_service = LandService.objects.get(service_type="Land Survey")
        self.assertEqual(land_service.location, "Dakar")

    def test_land_service_str(self):
        land_service = LandService.objects.get(service_type="Land Registration")
        self.assertEqual(str(land_service), "Land Registration at Banjul")