import random
def get_random_code():
    # Generate a random 6-digit code
    code = ""
    for i in range(6):
        code += str(random.randint(0, 9))
    return code