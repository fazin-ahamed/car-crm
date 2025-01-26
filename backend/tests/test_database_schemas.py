from django.test import TestCase
from django.db import connection
from backend.models.vehicle import Vehicle, VehicleType
from backend.models.booking import Booking
from backend.models.customer import Customer

class DatabaseSchemaTest(TestCase):
    def test_vehicle_table_schema(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'backend_vehicle'")
            columns = [row[0] for row in cursor.fetchall()]
            expected_columns = ['id', 'type_id', 'registration_number', 'status', 'availability']
            self.assertEqual(columns, expected_columns)

    def test_vehicle_type_table_schema(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'backend_vehicletype'")
            columns = [row[0] for row in cursor.fetchall()]
            expected_columns = ['id', 'name', 'description']
            self.assertEqual(columns, expected_columns)

    def test_booking_table_schema(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'backend_booking'")
            columns = [row[0] for row in cursor.fetchall()]
            expected_columns = ['id', 'vehicle_id', 'user_id', 'start_date', 'end_date', 'status']
            self.assertEqual(columns, expected_columns)

    def test_customer_table_schema(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'backend_customer'")
            columns = [row[0] for row in cursor.fetchall()]
            expected_columns = ['id', 'user_id', 'phone', 'address', 'city', 'state', 'country', 'zip_code', 'date_of_birth', 'created_at', 'updated_at']
            self.assertEqual(columns, expected_columns)
