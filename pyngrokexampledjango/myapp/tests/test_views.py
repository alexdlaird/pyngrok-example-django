__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os
import sys

from django.conf import settings
from django.test import TestCase
from django.urls import reverse


class TestCaseViews(TestCase):
    def test_healthcheck(self):
        # WHEN
        response = self.client.get(reverse('healthcheck'))

        self.assertEqual(response.status_code, 200)
        if os.environ.get("USE_NGROK", "False") == "True":
            sys.stderr.write("Asserting ngrok used -->")
            self.assertIn("ngrok", settings.BASE_URL)
        else:
            sys.stderr.write("Asserting ngrok not used -->")
            self.assertNotIn("ngrok", settings.BASE_URL)
