from rest_framework.test import APITestCase
from backend.models.vehicle import Vehicle
from backend.models.booking import Booking
from backend.models.customer import Customer
from backend.serializers.vehicle import VehicleSerializer
from backend.serializers.booking import BookingSerializer
from backend.serializers.customer import CustomerSerializer

class VehicleSerializerTest(APITestCase):
    def setUp(self):
        self.vehicle_data = {
            'type': 1,
            'registration_number': 'ABC123',
            'status': 'available',
            'availability': True
        }
        self.vehicle = Vehicle.objects.create(**self.vehicle_data)

    def test_vehicle_serialization(self):
        serializer = VehicleSerializer(self.vehicle)
        self.assertEqual(serializer.data['registration_number'], self.vehicle_data['registration_number'])
        self.assertEqual(serializer.data['status'], self.vehicle_data['status'])
        self.assertEqual(serializer.data['availability'], self.vehicle_data['availability'])

    def test_vehicle_deserialization(self):
        serializer = VehicleSerializer(data=self.vehicle_data)
        self.assertTrue(serializer.is_valid())
        vehicle = serializer.save()
        self.assertEqual(vehicle.registration_number, self.vehicle_data['registration_number'])
        self.assertEqual(vehicle.status, self.vehicle_data['status'])
        self.assertEqual(vehicle.availability, self.vehicle_data['availability'])

class BookingSerializerTest(APITestCase):
    def setUp(self):
        self.booking_data = {
            'vehicle': 1,
            'user': 1,
            'start_date': '2023-01-01T00:00:00Z',
            'end_date': '2023-01-02T00:00:00Z',
            'status': 'confirmed'
        }
        self.booking = Booking.objects.create(**self.booking_data)

    def test_booking_serialization(self):
        serializer = BookingSerializer(self.booking)
        self.assertEqual(serializer.data['start_date'], self.booking_data['start_date'])
        self.assertEqual(serializer.data['end_date'], self.booking_data['end_date'])
        self.assertEqual(serializer.data['status'], self.booking_data['status'])

    def test_booking_deserialization(self):
        serializer = BookingSerializer(data=self.booking_data)
        self.assertTrue(serializer.is_valid())
        booking = serializer.save()
        self.assertEqual(booking.start_date, self.booking_data['start_date'])
        self.assertEqual(booking.end_date, self.booking_data['end_date'])
        self.assertEqual(booking.status, self.booking_data['status'])

class CustomerSerializerTest(APITestCase):
    def setUp(self):
        self.customer_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        }
        self.customer = Customer.objects.create(**self.customer_data)

    def test_customer_serialization(self):
        serializer = CustomerSerializer(self.customer)
        self.assertEqual(serializer.data['first_name'], self.customer_data['first_name'])
        self.assertEqual(serializer.data['last_name'], self.customer_data['last_name'])
        self.assertEqual(serializer.data['email'], self.customer_data['email'])

    def test_customer_deserialization(self):
        serializer = CustomerSerializer(data=self.customer_data)
        self.assertTrue(serializer.is_valid())
        customer = serializer.save()
        self.assertEqual(customer.first_name, self.customer_data['first_name'])
        self.assertEqual(customer.last_name, self.customer_data['last_name'])
        self.assertEqual(customer.email, self.customer_data['email'])
