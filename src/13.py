import random
def get_random_code():
    numbers = "23456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(10):
        code += random.choice(numbers)
        code += random.choice(letters)
    return code