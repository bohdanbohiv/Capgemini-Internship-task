def _main():
    from sys import argv

    if len(argv) != 2:
        print('Usage: python password_checker.py password')
        return
    print(check_password(argv[1]))


def check_password(password: str) -> str:
    from string import punctuation

    message = []

    if not contains_lower_and_upper(password):
        message.append(
            '- Password must contain both lowercase and uppercase characters')

    if not contains_digits(password):
        message.append('- Password must contain digits')

    if not contains_punctuation(password):
        message.append(
            '- Password must contain at least one punctuation character'
            f' ({punctuation})')

    if len(password) < 14:
        message.append('- Password must be at least 14 characters long')

    return '\n'.join(['Weak password:'] + message) if message else \
        'Strong password'


def contains_lower_and_upper(password: str) -> bool:
    from re import search
    return search('[A-Z]', password) and bool(search('[a-z]', password))


def contains_digits(password: str) -> bool:
    from re import search
    return bool(search(r'\d', password))


def contains_punctuation(password: str) -> bool:
    from re import search
    from string import punctuation
    return bool(search('[' + punctuation.replace('\\', '\\' * 3) + ']',
                       password))


if __name__ == '__main__':
    _main()
