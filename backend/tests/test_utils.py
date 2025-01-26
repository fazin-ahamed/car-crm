from django.test import TestCase
from backend.utils.helpers import format_date, validate_email, format_currency, validate_phone_number

class UtilsTest(TestCase):
    def test_format_date(self):
        date = '2023-01-01'
        formatted_date = format_date(date)
        self.assertEqual(formatted_date, 'January 1, 2023')

    def test_validate_email(self):
        valid_email = 'test@example.com'
        invalid_email = 'test@.com'
        self.assertTrue(validate_email(valid_email))
        self.assertFalse(validate_email(invalid_email))

    def test_format_currency(self):
        value = 1000
        currency = 'USD'
        formatted_currency = format_currency(value, currency)
        self.assertEqual(formatted_currency, '$1,000.00')

    def test_validate_phone_number(self):
        valid_phone_number = '+1234567890'
        invalid_phone_number = '12345'
        self.assertTrue(validate_phone_number(valid_phone_number))
        self.assertFalse(validate_phone_number(invalid_phone_number))
