import random

def get_random_code(length=10):
    """Returns a random string of letters and numbers of the given length."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters += letters.upper()
    letters += '0123456789'
    code = ''
    for i in range(length):
        code += random.choice(letters)
    return code
