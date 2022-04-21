from unittest import TestCase, main
from password_checker import *


class TestPasswordChecker(TestCase):
    def test_contains_lower_and_upper(self):
        self.assertTrue(contains_lower_and_upper('Qwerty'))
        self.assertFalse(contains_lower_and_upper('qwerty'))
        self.assertFalse(contains_lower_and_upper('QWERTY'))

    def test_contains_digits(self):
        self.assertTrue(contains_digits('1w3r5y'))
        self.assertFalse(contains_digits('qwerty'))
        self.assertTrue(contains_digits('123456'))

    def test_contains_punctuation(self):
        self.assertTrue(contains_punctuation('Pass the test, please'))
        self.assertFalse(contains_punctuation('qwerty'))

    def test_check_length(self):
        self.assertFalse(check_length('qwerty'))
        self.assertTrue(check_length('0123456789abcd'))

    def test_check_password(self):
        self.assertEqual(check_password('qwerty'), '''Weak password:
- Password must contain both lowercase and uppercase characters
- Password must contain digits
- Password must contain at least one punctuation character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
- Password must be at least 14 characters long''')
        self.assertEqual(check_password('Qwerty123'), '''Weak password:
- Password must contain at least one punctuation character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
- Password must be at least 14 characters long''')
        self.assertEqual(check_password('The quick br0wn fox jumps 0ver the lazy d0g.'), 'Strong password')


if __name__ == '__main__':
    main()
