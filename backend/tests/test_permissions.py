from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from backend.models.vehicle import Vehicle
from backend.models.booking import Booking
from backend.models.customer import Customer

class PermissionsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.vehicle = Vehicle.objects.create(
            type='Car',
            registration_number='ABC123',
            status='Available',
            availability=True
        )

        self.booking = Booking.objects.create(
            vehicle=self.vehicle,
            user=self.user,
            start_date='2023-01-01T10:00:00Z',
            end_date='2023-01-02T10:00:00Z',
            status='Confirmed'
        )

        self.customer = Customer.objects.create(
            user=self.user,
            name='John Doe',
            email='john.doe@example.com',
            phone='1234567890'
        )

    def test_vehicle_permissions(self):
        response = self.client.get(f'/api/vehicles/{self.vehicle.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(f'/api/vehicles/{self.vehicle.id}/', {
            'type': 'Truck',
            'registration_number': 'XYZ789',
            'status': 'Unavailable',
            'availability': False
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_booking_permissions(self):
        response = self.client.get(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(f'/api/bookings/{self.booking.id}/', {
            'vehicle': self.vehicle.id,
            'user': self.user.id,
            'start_date': '2023-01-03T10:00:00Z',
            'end_date': '2023-01-04T10:00:00Z',
            'status': 'Cancelled'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_permissions(self):
        response = self.client.get(f'/api/customers/{self.customer.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(f'/api/customers/{self.customer.id}/', {
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'phone': '0987654321'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
