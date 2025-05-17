import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate some synthetic data for demonstration purposes
data = np.random.rand(100, 5)
labels = KMeans(n_clusters=3).fit_predict(data)

plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Clustered Data with k-means clustering")
plt.show()
