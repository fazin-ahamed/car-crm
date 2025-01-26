import unittest
from backend.utils.animations import AnimationHandler

class TestAnimationImplementations(unittest.TestCase):

    def setUp(self):
        self.animation_handler = AnimationHandler()

    def test_animation_start(self):
        result = self.animation_handler.start_animation("fadeIn")
        self.assertTrue(result)
        self.assertEqual(self.animation_handler.current_animation, "fadeIn")

    def test_animation_stop(self):
        self.animation_handler.start_animation("fadeOut")
        result = self.animation_handler.stop_animation()
        self.assertTrue(result)
        self.assertIsNone(self.animation_handler.current_animation)

    def test_animation_pause(self):
        self.animation_handler.start_animation("slideIn")
        result = self.animation_handler.pause_animation()
        self.assertTrue(result)
        self.assertEqual(self.animation_handler.current_animation, "slideIn")
        self.assertTrue(self.animation_handler.is_paused)

    def test_animation_resume(self):
        self.animation_handler.start_animation("slideOut")
        self.animation_handler.pause_animation()
        result = self.animation_handler.resume_animation()
        self.assertTrue(result)
        self.assertEqual(self.animation_handler.current_animation, "slideOut")
        self.assertFalse(self.animation_handler.is_paused)

    def test_invalid_animation(self):
        result = self.animation_handler.start_animation("invalidAnimation")
        self.assertFalse(result)
        self.assertIsNone(self.animation_handler.current_animation)

if __name__ == "__main__":
    unittest.main()
