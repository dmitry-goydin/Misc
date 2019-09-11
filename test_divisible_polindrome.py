from unittest import TestCase


class TestDivisiblePalindrome(TestCase):
    def test_divisible_palindrome(self):
        from Maya import divisible_palindrome
        self.assertEqual(divisible_palindrome(150, 11), 121, "Expected 121")
