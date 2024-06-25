from django.test import TestCase
from django.urls import reverse
from .models import Student, Grade

# Tests de gestion
class IndexTest(TestCase):
    def test_index(self):
        response = self.client.get('index')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, world!')