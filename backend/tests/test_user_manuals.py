import unittest
from backend.utils.user_manuals import UserManual

class TestUserManuals(unittest.TestCase):

    def setUp(self):
        self.user_manual = UserManual()

    def test_user_manual_content(self):
        content = self.user_manual.get_content()
        self.assertIsNotNone(content)
        self.assertIn("Introduction", content)
        self.assertIn("Getting Started", content)
        self.assertIn("Features", content)
        self.assertIn("FAQ", content)

    def test_user_manual_accuracy(self):
        content = self.user_manual.get_content()
        self.assertIn("Introduction", content)
        self.assertIn("Getting Started", content)
        self.assertIn("Features", content)
        self.assertIn("FAQ", content)
        self.assertNotIn("Lorem Ipsum", content)
        self.assertNotIn("Placeholder", content)

if __name__ == '__main__':
    unittest.main()
