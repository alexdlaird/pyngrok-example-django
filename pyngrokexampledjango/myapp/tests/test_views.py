import os
import unittest
from unittest import TestCase

from django.test import Client
from django.urls import reverse


class TestCaseViews(TestCase):
    def setUp(self):
        os.environ["USE_NGROK"] = "True"
        self.client = Client()

    @unittest.skipIf(not os.environ.get("NGROK_AUTHTOKEN"), "NGROK_AUTHTOKEN environment variable not set")
    def test_healthcheck(self):
        # WHEN
        response = self.client.get(reverse('healthcheck'))

        self.assertEqual(response.status_code, 200)
