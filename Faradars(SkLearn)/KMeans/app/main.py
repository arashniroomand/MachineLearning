import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as dt
import sklearn.cluster as cl
from sklearn.decomposition import PCA

# Load Iris dataset
IRIS = dt.load_iris()
X = IRIS.data
Y = IRIS.target

# Apply PCA to reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Streamlit app title
st.title("K-Means Clustering on Iris Dataset with PCA")

# Sidebar for user input
st.sidebar.header("K-Means Parameters")
k_choice = st.sidebar.slider("Select number of clusters (k)", min_value=1, max_value=10, value=3)

# Function to perform K-Means clustering
def run_kmeans(data, k):
    kmn = cl.KMeans(n_clusters=k, random_state=42)
    kmn.fit(data)
    return kmn.labels_, kmn.cluster_centers_

# Function to plot K-Means results
def plot_kmeans(X_pca, labels, centroids, Y, k):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Predicted clusters
    ax1.scatter(X_pca[:, 0], X_pca[:, 1], s=15, c=labels, cmap='viridis')
    ax1.scatter(centroids[:, 0], centroids[:, 1], s=60, c='red', marker='x')
    ax1.set_xlabel('PC1')
    ax1.set_ylabel('PC2')
    ax1.set_title(f'K-Means Clustering (k={k})')
    
    # Actual target classes
    ax2.scatter(X_pca[:, 0], X_pca[:, 1], s=15, c=Y, cmap='viridis')
    ax2.set_xlabel('PC1')
    ax2.set_ylabel('PC2')
    ax2.set_title('Actual Iris Classes')
    
    plt.tight_layout()
    return fig

# Function to compute and plot elbow method with optimal k
def plot_elbow(data, max_k=10):
    inertias = []
    for k in range(1, max_k + 1):
        kmn = cl.KMeans(n_clusters=k, random_state=42)
        kmn.fit(data)
        inertias.append(kmn.inertia_)
    
    # Find optimal k using maximum distance to the line from first to last point
    ks = np.arange(1, max_k + 1)
    inertias = np.array(inertias)
    # Line from first to last point
    p1 = np.array([1, inertias[0]])
    p2 = np.array([max_k, inertias[-1]])
    line_vec = p2 - p1
    line_len = np.sqrt(np.sum(line_vec**2))
    line_unit = line_vec / line_len
    
    # Compute distances from each point to the line
    distances = []
    for k, inertia in zip(ks, inertias):
        point = np.array([k, inertia])
        vec = point - p1
        proj = np.dot(vec, line_unit) * line_unit
        dist = np.sqrt(np.sum((vec - proj)**2))
        distances.append(dist)
    
    # Optimal k is the one with maximum distance
    optimal_k = ks[np.argmax(distances)]
    
    # Plot elbow curve
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ks, inertias, marker='o')
    ax.axvline(x=optimal_k, color='red', linestyle='--', label=f'Optimal k = {optimal_k}')
    ax.set_xlabel('Number of clusters (k)')
    ax.set_ylabel('Inertia')
    ax.set_title('Elbow Method for Optimal k')
    ax.grid(True)
    ax.legend()
    return fig, optimal_k

# Display PCA explained variance
st.write(f"PCA Component 1 explains {pca.explained_variance_ratio_[0]:.2%} of variance")
st.write(f"PCA Component 2 explains {pca.explained_variance_ratio_[1]:.2%} of variance")

# Section 1: K-Means Clustering with Selected k
st.header("K-Means Clustering Results")
labels, centroids = run_kmeans(X_pca, k_choice)
fig_kmeans = plot_kmeans(X_pca, labels, centroids, Y, k_choice)
st.pyplot(fig_kmeans)

# Section 2: Elbow Method with Optimal k
st.header("Elbow Method to Find Optimal k")
fig_elbow, optimal_k = plot_elbow(X_pca)
st.pyplot(fig_elbow)
st.write(f"The 'elbow' point suggests the optimal number of clusters is **k={optimal_k}**. This is where adding more clusters yields diminishing reductions in inertia.")