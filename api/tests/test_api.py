from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthEndpointTests(APITestCase):
    def test_health_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"status": "ok"})


class HelloEndpointTests(APITestCase):
    def test_hello_default_name(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "Hello, world!")

    def test_hello_with_name(self):
        response = self.client.get(reverse("hello"), {"name": "Rory"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "Hello, Rory!")

    def test_hello_includes_course(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.json()["course"], "CSC 325")
