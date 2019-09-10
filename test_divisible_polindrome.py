from unittest import TestCase


class TestDivisiblePolindrome(TestCase):
    def test_divisible_polindrome(self):
        from Maya import divisible_polindrome
        self.assertEqual(divisible_polindrome(150, 11), 121, "Expected 121")
