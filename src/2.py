import random

def get_random_code():
    """Generate a random 4-digit number between 1000 and 9999."""
    return str(random.randint(1000, 9999))