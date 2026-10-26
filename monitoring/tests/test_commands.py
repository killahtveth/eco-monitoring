from django.core.management import call_command
from django.test import TestCase

from monitoring.models import Measurement


class CommandTests(TestCase):
    def test_collect_data_command(self):
        call_command("collect_data")
        self.assertTrue(Measurement.objects.exists())
