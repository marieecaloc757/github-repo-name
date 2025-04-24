import numpy as np
import pandas as pd

def sample_data(n_samples=1000):
    """
    Generate a sample data set with n_samples.
    
    Parameters:
    - n_samples: Number of samples to generate (default is 1000).
    
    Returns:
    - A randomly sampled data frame.
    """
    # Example: Generating random data points
    data = np.random.rand(n_samples, 2)
    return pd.DataFrame(data)

# To use the function with a different seed for reproducibility
sample_data(seed=42)
