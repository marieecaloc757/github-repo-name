import numpy as np

def compute_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
        
    Returns:
        float: The average of the numbers.
    """
    if not numbers:
        return 0.0
    
    total = sum(numbers)
    count = len(numbers)
    return total / count

# Example usage
numbers = [1, 2, 3, 4, 5]
average = compute_average(numbers)
print("The average is:", average)
