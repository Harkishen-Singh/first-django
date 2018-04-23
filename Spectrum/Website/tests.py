from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.

class SpectrumTest(SimpleTestCase):
    def test_home_case(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_case(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        
