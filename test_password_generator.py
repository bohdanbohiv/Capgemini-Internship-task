from unittest import TestCase, main
from password_generator import generate_password
from password_checker import check_password


class TestPasswordGenerator(TestCase):
    def test_password_generator(self):
        for _ in range(10000):
            pw = generate_password()
            message = check_password(pw)
            self.assertEqual(message,
                             'Strong password',
                             f'{pw} does not qualify because: '
                             f'{message.removeprefix("Weak password:")}')


if __name__ == '__main__':
    main()
