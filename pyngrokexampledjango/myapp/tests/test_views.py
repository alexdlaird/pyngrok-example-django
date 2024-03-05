__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os
import unittest

from django.conf import settings
from django.test import LiveServerTestCase
from django.urls import reverse


class TestCaseViews(LiveServerTestCase):
    @unittest.skipUnless(os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("NGROK_AUTHTOKEN"), "NGROK_AUTHTOKEN environment variable not set")
    def test_healthcheck(self):
        # WHEN
        response = self.client.get(reverse('healthcheck'))

        self.assertEqual(response.status_code, 200)
        self.assertIn("ngrok", settings.BASE_URL)
