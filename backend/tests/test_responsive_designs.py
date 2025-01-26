import unittest
from django.test import Client
from django.urls import reverse

class ResponsiveDesignsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_vehicle_list_responsive(self):
        response = self.client.get(reverse('vehicle-list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('class="vehicle-list"', response.content.decode())
        self.assertIn('class="responsive"', response.content.decode())

    def test_booking_calendar_responsive(self):
        response = self.client.get(reverse('booking-calendar'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('class="booking-calendar"', response.content.decode())
        self.assertIn('class="responsive"', response.content.decode())

    def test_reservation_form_responsive(self):
        response = self.client.get(reverse('reservation-form'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('class="reservation-form"', response.content.decode())
        self.assertIn('class="responsive"', response.content.decode())

    def test_customer_profile_responsive(self):
        response = self.client.get(reverse('customer-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('class="customer-profile"', response.content.decode())
        self.assertIn('class="responsive"', response.content.decode())

    def test_admin_dashboard_responsive(self):
        response = self.client.get(reverse('admin-dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('class="admin-dashboard"', response.content.decode())
        self.assertIn('class="responsive"', response.content.decode())

if __name__ == '__main__':
    unittest.main()
