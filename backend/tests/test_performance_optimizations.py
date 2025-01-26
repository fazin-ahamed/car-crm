import time
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Vehicle, Booking, Customer

class PerformanceOptimizationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vehicle = Vehicle.objects.create(
            type="Sedan",
            registration_number="ABC123",
            status="Available",
            availability=True
        )
        self.customer = Customer.objects.create(
            name="John Doe",
            email="john.doe@example.com"
        )
        self.booking = Booking.objects.create(
            vehicle=self.vehicle,
            customer=self.customer,
            start_date="2023-01-01T10:00:00Z",
            end_date="2023-01-10T10:00:00Z",
            status="Confirmed"
        )

    def test_vehicle_list_performance(self):
        start_time = time.time()
        response = self.client.get(reverse('vehicle-list'))
        end_time = time.time()
        duration = end_time - start_time
        self.assertEqual(response.status_code, 200)
        self.assertLess(duration, 1, "Vehicle list API call took too long")

    def test_booking_list_performance(self):
        start_time = time.time()
        response = self.client.get(reverse('booking-list'))
        end_time = time.time()
        duration = end_time - start_time
        self.assertEqual(response.status_code, 200)
        self.assertLess(duration, 1, "Booking list API call took too long")

    def test_customer_list_performance(self):
        start_time = time.time()
        response = self.client.get(reverse('customer-list'))
        end_time = time.time()
        duration = end_time - start_time
        self.assertEqual(response.status_code, 200)
        self.assertLess(duration, 1, "Customer list API call took too long")
