import unittest
from palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_palindrom_complex(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal, Panama'))

    def test_palindrom_non_palindrome(self):          
        self.assertFalse(is_palindrome('BTP405'))

    def test_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_palindrom_special_characters(self):        
        self.assertTrue(is_palindrome("Madam, I'm Adam"))


if __name__ == '__main__':
    unittest.main()
