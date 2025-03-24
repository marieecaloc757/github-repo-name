import math

def calculate_distance(point1, point2):
    """
    Calculate the distance between two points in 2D space.
    
    Args:
        point1 (tuple): A tuple representing the first point [x1, y1].
        point2 (tuple): A tuple representing the second point [x2, y2].
        
    Returns:
        float: The Euclidean distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Example usage and verification code
def check_distance():
    # Test cases
    test_point1 = [0, 0]
    test_point2 = [3, 4]
    
    calculated_distance = calculate_distance(test_point1, test_point2)
    print(f"Calculated distance: {calculated_distance}")
    
    # Expected output:
    # Calculated distance: 5.0
    if abs(calculated_distance - 5.0) < 1e-6:
        print("The code is correct.")
    else:
        print("The code is incorrect.")

check_distance()
