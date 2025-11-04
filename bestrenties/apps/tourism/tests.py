from django.test import TestCase
from .models import TouristSite

class TouristSiteModelTest(TestCase):

    def setUp(self):
        TouristSite.objects.create(name="Gorée Island", description="A historic island and UNESCO World Heritage site.", location="Dakar, Senegal")
        TouristSite.objects.create(name="Nyungwe National Park", description="A beautiful national park known for its biodiversity.", location="Rwanda")

    def test_tourist_site_creation(self):
        gorée_island = TouristSite.objects.get(name="Gorée Island")
        nyungwe_national_park = TouristSite.objects.get(name="Nyungwe National Park")
        self.assertEqual(gorée_island.description, "A historic island and UNESCO World Heritage site.")
        self.assertEqual(nyungwe_national_park.location, "Rwanda")

    def test_tourist_site_str(self):
        gorée_island = TouristSite.objects.get(name="Gorée Island")
        self.assertEqual(str(gorée_island), "Gorée Island")