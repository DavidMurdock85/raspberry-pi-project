import re

PHONE_REGEX = re.compile(r'^\+?1?\d{9,15}$')

def validate_phone(phone):
    if not PHONE_REGEX.match(phone):
        return 'Invalid phone number'
    return None