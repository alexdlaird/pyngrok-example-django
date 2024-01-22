import os
from unittest import TestCase

from django.test import Client
from django.urls import reverse


class TestCaseViewsNoNgrok(TestCase):
    def setUp(self):
        os.environ["USE_NGROK"] = "False"
        self.client = Client()

    def test_healthcheck_no_ngrok(self):
        # WHEN
        response = self.client.get(reverse('healthcheck'))

        self.assertEqual(response.status_code, 200)
