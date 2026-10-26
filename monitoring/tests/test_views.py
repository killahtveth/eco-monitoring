from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    def test_health_endpoint(self):
        response = self.client.get(reverse("health_check"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})
