from typing import Optional, Dict
from .models import Measurement


def get_measurement_stats(location_id: int, parameter: str) -> Optional[Dict[str, float]]:
    measurements = Measurement.objects.filter(
        location_id=location_id,
        parameter=parameter
    ).values_list('value', flat=True)

    if not measurements:
        return None

    values = list(measurements)
    return {
        'min': min(values),
        'max': max(values),
        'avg': sum(values) / len(values),
        'count': len(values)
    }