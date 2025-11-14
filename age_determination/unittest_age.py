import unittest
from age import categorise_byage

class TestCategoriseByAge(unittest.TestCase):
    def test_child_category(self):
        self.assertEqual(categorise_byage(5), "child")
        self.assertEqual(categorise_byage(9), "child")
    def test_teenager_category(self):
        self.assertEqual(categorise_byage(15), "teenager")
        self.assertEqual(categorise_byage(18), "teenager")
    def test_adult_category(self):
        self.assertEqual(categorise_byage(19), "adult")
        self.assertEqual(categorise_byage(64), "adult")
    def test_golden_age_category(self):
        self.assertEqual(categorise_byage(65), "golden age")
        self.assertEqual(categorise_byage(120), "golden age")
    def test_invalid_age(self):
        self.assertEqual(categorise_byage(-1), "invalid age: -1")
        self.assertEqual(categorise_byage(130), "invalid age: 130")
