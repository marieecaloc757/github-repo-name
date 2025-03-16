
import random

def get_random_python_code():
    # Generate a random number between 1 and 5
    num = random.randint(1, 5)

    if num == 1:
        return "print('Hello, world!')"
    elif num == 2:
        return "for i in range(10):\n\tprint(i)"
    elif num == 3:
        return "names = ['Alice', 'Bob', 'Charlie']\nfor name in names:\n\tprint(name)"
    elif num == 4:
        return "numbers = [1, 2, 3, 4, 5]\nfor number in numbers:\n\tif number % 2 == 0:\n\t\tprint(number)"
    else:
        return "users = {'Alice': {'age': 25}, 'Bob': {'age': 30}}"