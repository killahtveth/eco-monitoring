from django.test import TestCase
from monitoring.models import Location, Measurement
from monitoring.services import get_measurement_stats

class ServiceTests(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Парк", latitude=54.0, longitude=48.0)
        Measurement.objects.create(location=self.location, parameter="PM2.5", value=10.0)
        Measurement.objects.create(location=self.location, parameter="PM2.5", value=20.0)

    def test_stats_calculation(self):
        stats = get_measurement_stats(self.location.id, "PM2.5")
        self.assertEqual(stats['avg'], 15.0)
        self.assertEqual(stats['count'], 2)