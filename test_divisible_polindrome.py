from unittest import TestCase


class TestDivisiblePalindrome(TestCase):
    def test_divisible_palindrome(self):
        from Maya import divisible_palindrome
        self.assertEqual(divisible_palindrome(150, 11), 121, "Unexpected result for (150, 11)")


class TestDivisiblePalindromes(TestCase):
    def test_divisible_palindromes(self):
        from Maya import divisible_palindromes
        self.assertEqual(divisible_palindromes(150, 11), [121, 99, 88, 77, 66, 55, 44, 33, 22, 11],
                         "Unexpected result for (150, 11)")
        self.assertEqual(divisible_palindromes(150, 7), [77], "Unexpected result for 150, 7")
        self.assertEqual(divisible_palindromes(1000, 17), [969, 646, 595, 323, 272], "Unexpected result for (1000, 17)")
