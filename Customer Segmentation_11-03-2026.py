# Customer Segmentation using K-Means

from sklearn.cluster import KMeans

# Example dataset (Age, Spending Score)
data = [
    [20, 80],
    [25, 75],
    [30, 60],
    [40, 40],
    [50, 20]
]

# Create model
kmeans = KMeans(n_clusters=2)

# Train model
kmeans.fit(data)

# Print cluster groups
print("Customer Groups:", kmeans.labels_)