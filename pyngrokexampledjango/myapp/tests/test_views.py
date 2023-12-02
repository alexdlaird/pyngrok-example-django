from unittest import TestCase

from django.test import Client
from django.urls import reverse


class TestCaseViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_healthcheck(self):
        # WHEN
        response = self.client.get(reverse('healthcheck'))

        self.assertEqual(response.status_code, 200)
