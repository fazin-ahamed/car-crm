import unittest
from django.core.cache import cache
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from backend.models import Vehicle, Booking, Customer
from backend.serializers import VehicleSerializer, BookingSerializer, CustomerSerializer

class CachingTests(APITestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            type="Car",
            registration_number="ABC123",
            status="Available",
            availability=True
        )
        self.booking = Booking.objects.create(
            vehicle=self.vehicle,
            user_id=1,
            start_date="2023-01-01T10:00:00Z",
            end_date="2023-01-02T10:00:00Z",
            status="Confirmed"
        )
        self.customer = Customer.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            phone="1234567890"
        )

    def test_vehicle_list_caching(self):
        url = reverse('vehicle-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['registration_number'], self.vehicle.registration_number)

        # Check if the response is cached
        cached_response = cache.get(url)
        self.assertIsNotNone(cached_response)
        self.assertEqual(cached_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(cached_response.data), 1)
        self.assertEqual(cached_response.data[0]['registration_number'], self.vehicle.registration_number)

    def test_booking_list_caching(self):
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status'], self.booking.status)

        # Check if the response is cached
        cached_response = cache.get(url)
        self.assertIsNotNone(cached_response)
        self.assertEqual(cached_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(cached_response.data), 1)
        self.assertEqual(cached_response.data[0]['status'], self.booking.status)

    def test_customer_list_caching(self):
        url = reverse('customer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], self.customer.email)

        # Check if the response is cached
        cached_response = cache.get(url)
        self.assertIsNotNone(cached_response)
        self.assertEqual(cached_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(cached_response.data), 1)
        self.assertEqual(cached_response.data[0]['email'], self.customer.email)
