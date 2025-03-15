import random
import string
import sys
def secret_message(my_string):
    """Encrypts a message by replacing each letter with a randomly generated one"""
    new_string = ''
    for char in my_string:
        if char.isalpha():
            new_string += random.choice(string.ascii_letters)
        else:
            new_string += char
    return new_string
my_string = input("Enter a message to encrypt: ")
encrypted_message = secret_message(my_string)
print("Encrypted message:", encrypted_message)
