import numpy as np
import matplotlib.pyplot as plt

def draw_random_shape():
    """
    Generate a random shape using NumPy arrays and Matplotlib.
    
    Example usage:
    >>> random_shape = draw_random_shape()
    """

    # Define the number of points for each dimension
    points_per_dim = 10
    
    # Create an array with random numbers between -5 and 5
    random_numbers = np.random.rand(points_per_dim, points_per_dim)
    
    # Use NumPy's broadcasting feature to expand the shape arrays
    expanded_random_numbers = np.expand_dims(random_numbers, axis=0)
    
    # Generate a mask of ones in the center of each dimension
    center_mask = np.ones((points_per_dim, points_per_dim))
    
    # Combine the array and the mask into an Numpy array for plotting
    combined_array = np.concatenate((expanded_random_numbers, center_mask), axis=0)
    
    # Plot the shape with a dashed line border
    plt.plot(combined_array[:, 0], combined_array[:, 1], 'k-')
    
    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Random Shape')
    
    # Show the plot
    plt.show()
