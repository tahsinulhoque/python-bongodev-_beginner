import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Test
print(is_valid_email("test@domain.com"))     # True
print(is_valid_email("invalid-email@com"))   # False
