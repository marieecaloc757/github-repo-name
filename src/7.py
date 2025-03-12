import random
def get_random_python_code():
    code = ""
    # Generate a random number of lines
    num_lines = random.randint(1, 10)
    for i in range(num_lines):
        # Add a random line of Python code to the string
        code += f"print('This is line {i + 1}')\n"
    return code