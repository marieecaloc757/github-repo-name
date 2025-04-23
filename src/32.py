import numpy as np

def calculate_sum(a):
    """
    Calculate the sum of all elements in an array.
    
    Parameters:
    a (numpy.ndarray): A 1D numpy array.
    
    Returns:
    float: The sum of all elements in the array.
    """
    return np.sum(a)

# Example usage
a = np.array([5, 2, 8])
print(calculate_sum(a))  # Output: 15.0
