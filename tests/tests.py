import unittest


class SimpleTest(unittest.TestCase):
    def test_always_true(self):
        self.assertEqual(True, True)