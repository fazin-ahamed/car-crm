import unittest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from backend.models import Vehicle, Booking, Customer

class BestPracticesTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vehicle_data = {
            "type": "Sedan",
            "registration_number": "ABC123",
            "status": "Available",
            "availability": True
        }
        self.booking_data = {
            "vehicle": 1,
            "user": 1,
            "start_date": "2023-01-01T00:00:00Z",
            "end_date": "2023-01-02T00:00:00Z",
            "status": "Confirmed"
        }
        self.customer_data = {
            "user": 1,
            "phone": "1234567890",
            "address": "123 Main St",
            "city": "Anytown",
            "state": "Anystate",
            "country": "Anycountry",
            "zip_code": "12345",
            "date_of_birth": "1990-01-01"
        }

    def test_vehicle_best_practices(self):
        response = self.client.post(reverse('vehicle-list'), self.vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertIn('type', response.data)
        self.assertIn('registration_number', response.data)
        self.assertIn('status', response.data)
        self.assertIn('availability', response.data)

    def test_booking_best_practices(self):
        response = self.client.post(reverse('booking-list'), self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertIn('vehicle', response.data)
        self.assertIn('user', response.data)
        self.assertIn('start_date', response.data)
        self.assertIn('end_date', response.data)
        self.assertIn('status', response.data)

    def test_customer_best_practices(self):
        response = self.client.post(reverse('customer-list'), self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertIn('user', response.data)
        self.assertIn('phone', response.data)
        self.assertIn('address', response.data)
        self.assertIn('city', response.data)
        self.assertIn('state', response.data)
        self.assertIn('country', response.data)
        self.assertIn('zip_code', response.data)
        self.assertIn('date_of_birth', response.data)
