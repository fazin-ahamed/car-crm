from django.test import TestCase
from django.contrib.auth.models import User
from backend.models.vehicle import Vehicle, VehicleType
from backend.models.booking import Booking
from backend.models.customer import Customer

class VehicleModelTest(TestCase):
    def setUp(self):
        self.vehicle_type = VehicleType.objects.create(name='Sedan', description='A small car')
        self.vehicle = Vehicle.objects.create(
            type=self.vehicle_type,
            registration_number='ABC123',
            status='available',
            availability=True
        )

    def test_vehicle_creation(self):
        self.assertEqual(self.vehicle.registration_number, 'ABC123')
        self.assertEqual(self.vehicle.status, 'available')
        self.assertTrue(self.vehicle.availability)
        self.assertEqual(self.vehicle.type.name, 'Sedan')

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.vehicle_type = VehicleType.objects.create(name='Sedan', description='A small car')
        self.vehicle = Vehicle.objects.create(
            type=self.vehicle_type,
            registration_number='ABC123',
            status='available',
            availability=True
        )
        self.booking = Booking.objects.create(
            vehicle=self.vehicle,
            user=self.user,
            start_date='2023-01-01T00:00:00Z',
            end_date='2023-01-02T00:00:00Z',
            status='confirmed'
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.vehicle.registration_number, 'ABC123')
        self.assertEqual(self.booking.user.username, 'testuser')
        self.assertEqual(self.booking.start_date, '2023-01-01T00:00:00Z')
        self.assertEqual(self.booking.end_date, '2023-01-02T00:00:00Z')
        self.assertEqual(self.booking.status, 'confirmed')

class CustomerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = Customer.objects.create(
            user=self.user,
            phone='1234567890',
            address='123 Main St',
            city='Anytown',
            state='Anystate',
            country='Anycountry',
            zip_code='12345',
            date_of_birth='1990-01-01'
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.user.username, 'testuser')
        self.assertEqual(self.customer.phone, '1234567890')
        self.assertEqual(self.customer.address, '123 Main St')
        self.assertEqual(self.customer.city, 'Anytown')
        self.assertEqual(self.customer.state, 'Anystate')
        self.assertEqual(self.customer.country, 'Anycountry')
        self.assertEqual(self.customer.zip_code, '12345')
        self.assertEqual(self.customer.date_of_birth, '1990-01-01')
