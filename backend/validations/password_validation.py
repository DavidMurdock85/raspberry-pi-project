import re

PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

def validate_password(password):
    if not PASSWORD_REGEX.match(password):
        return 'Invalid password'
    return None