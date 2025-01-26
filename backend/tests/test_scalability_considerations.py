import unittest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from backend.models import Vehicle, Booking, Customer
from backend.serializers import VehicleSerializer, BookingSerializer, CustomerSerializer

class ScalabilityConsiderationsTestCase(TestCase):
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

    def test_vehicle_scalability(self):
        for _ in range(1000):
            response = self.client.post(reverse('vehicle-list'), self.vehicle_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_booking_scalability(self):
        for _ in range(1000):
            response = self.client.post(reverse('booking-list'), self.booking_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_scalability(self):
        for _ in range(1000):
            response = self.client.post(reverse('customer-list'), self.customer_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
