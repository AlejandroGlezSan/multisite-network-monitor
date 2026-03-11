from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Site, NetworkDevice, Metric, Alert


class SiteModelTest(TestCase):
    def setUp(self):
        self.site = Site.objects.create(
            name="Sede Central",
            address="Calle Mayor 1",
            city="Las Palmas de GC",
            status="up"
        )

    def test_site_str(self):
        self.assertIn("Sede Central", str(self.site))

    def test_site_default_status(self):
        site = Site.objects.create(name="Nueva Sede", address="X", city="Y")
        self.assertEqual(site.status, 'unknown')


class NetworkDeviceModelTest(TestCase):
    def setUp(self):
        self.site = Site.objects.create(name="Sede", address="X", city="Y")
        self.device = NetworkDevice.objects.create(
            name="Router-01",
            site=self.site,
            device_type="router",
            ip_address="192.168.1.1"
        )

    def test_device_str(self):
        self.assertIn("192.168.1.1", str(self.device))

    def test_device_default_monitored(self):
        self.assertTrue(self.device.is_monitored)


class SiteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.site = Site.objects.create(name="Sede API", address="X", city="Y")

    def test_list_sites(self):
        response = self.client.get('/api/v1/sites/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_site(self):
        data = {"name": "Nueva", "address": "Calle 1", "city": "Madrid"}
        response = self.client.post('/api/v1/sites/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AlertAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.site = Site.objects.create(name="Sede", address="X", city="Y")
        self.alert = Alert.objects.create(
            title="CPU alta",
            description="CPU al 95%",
            severity="critical",
            site=self.site
        )

    def test_acknowledge_alert(self):
        response = self.client.post(f'/api/v1/alerts/{self.alert.id}/acknowledge/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.alert.refresh_from_db()
        self.assertEqual(self.alert.status, 'acknowledged')

    def test_resolve_alert(self):
        response = self.client.post(f'/api/v1/alerts/{self.alert.id}/resolve/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.alert.refresh_from_db()
        self.assertEqual(self.alert.status, 'resolved')