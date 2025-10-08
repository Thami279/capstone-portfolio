from django.test import TestCase
from django.urls import reverse


class SmokeTests(TestCase):
    def test_homepage_loads(self):
        response = self.client.get(reverse("portfolio:home"))
        self.assertEqual(response.status_code, 200)
