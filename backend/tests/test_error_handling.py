import unittest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from backend.models import Vehicle, Booking, Customer

class ErrorHandlingTests(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_vehicle_not_found(self):
        response = self.client.get(reverse('vehicle-detail', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_booking_not_found(self):
        response = self.client.get(reverse('booking-detail', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_customer_not_found(self):
        response = self.client.get(reverse('customer-detail', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_vehicle_data(self):
        invalid_data = {'registration_number': '', 'status': 'invalid'}
        response = self.client.post(reverse('vehicle-list'), invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_booking_data(self):
        invalid_data = {'start_date': 'invalid', 'end_date': 'invalid'}
        response = self.client.post(reverse('booking-list'), invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_customer_data(self):
        invalid_data = {'email': 'invalid'}
        response = self.client.post(reverse('customer-list'), invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
