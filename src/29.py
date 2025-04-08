import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Generate synthetic data
X = 10 * np.random.randn(1000)
y = 2 * X + 3 + np.random.randn(1000)

# Train a decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)
