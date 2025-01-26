import unittest
from rest_framework.test import APIClient
from rest_framework import status

class APIDocumentationTests(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_documentation_endpoint(self):
        response = self.client.get('/api/docs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('application/json', response['Content-Type'])

    def test_api_documentation_content(self):
        response = self.client.get('/api/docs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        self.assertIn('paths', content)
        self.assertIn('/vehicles/', content['paths'])
        self.assertIn('/bookings/', content['paths'])
        self.assertIn('/customers/', content['paths'])

if __name__ == '__main__':
    unittest.main()
