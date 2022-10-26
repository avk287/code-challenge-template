from django.test import TestCase
import django
django.setup()
from crop.models import CropData


class CropDataTest(TestCase):
    def setUp(self):
        django.setup()
        CropData.objects.create(year=1990, corn_yielld=100.0)
        CropData.objects.create(name=1991, corn_yielld=100.1)

    def test_animals_can_speak(self):
        """year and crop yield"""
        year1 = CropData.objects.get(year=1990)
        year2 = CropData.objects.get(name="cat")
        self.assertEqual(year1.speak(), '1990 : 100.0')
        self.assertEqual(year2.speak(), '1991 : 100.1')
