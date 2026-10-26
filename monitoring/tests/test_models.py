from django.test import TestCase
from django.core.exceptions import ValidationError
from monitoring.models import Location, Measurement

class ModelTests(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Центр", latitude=54.31, longitude=48.40)

    def test_measurement_negative_value(self):
        measurement = Measurement(location=self.location, parameter="PM2.5", value=-5.0)
        with self.assertRaises(ValidationError):
            measurement.full_clean()

    def test_measurement_valid(self):
        measurement = Measurement(location=self.location, parameter="PM2.5", value=15.5)
        measurement.full_clean()
        measurement.save()
        self.assertEqual(Measurement.objects.count(), 1)