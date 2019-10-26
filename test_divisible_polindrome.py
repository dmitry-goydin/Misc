from unittest import TestCase


class TestDivisiblePalindromes(TestCase):
    def test_divisible_palindromes(self):
        from divisible_palindrome import divisible_palindromes
        self.assertEqual([11, 22, 33, 44, 55, 66, 77, 88, 99, 121], divisible_palindromes(150, 11),
                         "Unexpected result for (150, 11)")
        self.assertEqual([77], divisible_palindromes(150, 7), "Unexpected result for 150, 7")
        self.assertEqual([272, 323, 595, 646, 969], divisible_palindromes(1000, 17), "Unexpected result for (1000, 17)")
        self.assertEqual([], divisible_palindromes(10, 2), "Unexpected result for (10, 2)")
        self.assertEqual([], divisible_palindromes(100, -5), "Unexpected result for (100, -5)")
