import re

USERNAME_REGEX = re.compile(r'^\w+$')

def validate_username(username):
    if not USERNAME_REGEX.match(username):
        return 'Invalid username'
    return None