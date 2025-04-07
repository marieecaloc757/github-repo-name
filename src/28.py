import numpy as np

def calculate_square_root(numbers):
    """
    Calculate and return the square root of each number in the list.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        list: A list containing the square roots of the input numbers.
    """
    return [np.sqrt(num) for num in numbers]

# Example usage
numbers = [1, 4, 9, 16]
result = calculate_square_root(numbers)
print(result)
