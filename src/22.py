import numpy as np
from sklearn.model_selection import train_test_split

def load_data(filename):
    """
    Load data from file.
    
    Args:
        filename (str): Path to the file containing the data.
        
    Returns:
        X_train: Training input features.
        y_train: Training target labels.
        X_test: Test input features.
        y_test: Test target labels.
    """
    # Load data
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Split into training and test sets
    X_train, y_train = [], []
    for line in lines:
        if line.startswith('X_train'):
            break
        elif line.startswith('X_test'):
            continue
        else:
            x_data, y_data = line.split(',')
            y_train.append(float(y_data))
            y_train.extend([0] * (10 - len(y_data)))
    
    # Convert to numpy arrays
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    
    return X_train, y_train

def split_data(x_train, y_train):
    """
    Split data into training and testing sets.
    
    Args:
        x_train (numpy array): Training input features.
        y_train (numpy array): Training target labels.
        
    Returns:
        x_train_test: Trained test features.
        y_train_test: Trained test target labels.
    """
    X_train, X_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2)
    
    # Convert to numpy arrays
    x_train_test = np.array(X_train).reshape(-1, 1)
    y_train_test = np.array(y_train).reshape(-1, 1)
    
    return x_train_test, y_train_test

def main():
    filename = 'path_to_your_file_here'  # Replace with the actual file path
    X_train, y_train = load_data(filename)
    x_train_test, y_train_test = split_data(X_train, y_train)

if __name__ == '__main__':
    main()
