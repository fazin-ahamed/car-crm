import unittest
from rest_framework.test import APIClient
from rest_framework import status

class APIDocumentationTests(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_documentation_generation(self):
        response = self.client.get('/api/docs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('application/json', response['Content-Type'])

    def test_api_documentation_accuracy(self):
        response = self.client.get('/api/docs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        documentation = response.json()
        self.assertIn('paths', documentation)
        self.assertIn('/api/vehicles/', documentation['paths'])
        self.assertIn('/api/bookings/', documentation['paths'])
        self.assertIn('/api/customers/', documentation['paths'])

if __name__ == '__main__':
    unittest.main()
