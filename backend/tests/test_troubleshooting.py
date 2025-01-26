import unittest
from backend.utils.troubleshooting import TroubleshootingGuide

class TestTroubleshootingGuide(unittest.TestCase):

    def setUp(self):
        self.troubleshooting_guide = TroubleshootingGuide()

    def test_missing_dependency(self):
        error_message = "ModuleNotFoundError: No module named 'requests'"
        solution = self.troubleshooting_guide.get_solution(error_message)
        self.assertIn("pip install requests", solution)

    def test_database_connection_error(self):
        error_message = "OperationalError: could not connect to server"
        solution = self.troubleshooting_guide.get_solution(error_message)
        self.assertIn("Check your database connection settings", solution)

    def test_invalid_api_key(self):
        error_message = "Invalid API key"
        solution = self.troubleshooting_guide.get_solution(error_message)
        self.assertIn("Verify your API key", solution)

    def test_unknown_error(self):
        error_message = "An unknown error occurred"
        solution = self.troubleshooting_guide.get_solution(error_message)
        self.assertIn("Contact support", solution)

if __name__ == '__main__':
    unittest.main()
