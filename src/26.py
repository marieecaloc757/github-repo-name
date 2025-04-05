import numpy as np
from sklearn.model_selection import train_test_split

def load_and_process_data(filename):
    """
    Load data from a file and preprocess it.
    
    Parameters:
        filename (str): The path to the file containing your dataset.

    Returns:
        X_train, y_train: Training features and labels.
    """
    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    data = []
    for line in lines:
        row = line.strip().split(',')
        if len(row) == 2:
            X = np.array([float(x) for x in row[0].split()]).reshape(-1, 1)
            y = int(float(row[1]))
            data.append((X, y))
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, np.array([i for i in range(len(lines))]), test_size=0.2)
    
    return X_train, y_train, X_test, y_test

# Example usage:
X_train, y_train, X_test, y_test = load_and_process_data('your_dataset_file.txt')
