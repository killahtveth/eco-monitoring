import random

from django.core.management.base import BaseCommand

from monitoring.models import Location, Measurement


class Command(BaseCommand):
    help = "Сбор экологических данных (имитация для прототипа)"

    def handle(self, *args, **options):
        location, _ = Location.objects.get_or_create(
            name="Центр города", defaults={"latitude": 54.31, "longitude": 48.40}
        )

        # Имитация получения данных с внешнего API
        parameters = ["PM2.5", "CO2", "NO2"]
        for param in parameters:
            # Генерируем случайное значение
            value = round(random.uniform(5.0, 50.0), 1)

            Measurement.objects.create(location=location, parameter=param, value=value)

        self.stdout.write(self.style.SUCCESS("Данные успешно собраны!"))
