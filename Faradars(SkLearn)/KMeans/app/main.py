import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from kneed import KneeLocator  # to find the elbow point

# Load data
iris = load_iris()
X = iris.data
y_true = iris.target

# Function to calculate inertia for a range of k
def calculate_elbow(X, max_k=10):
    inertias = []
    for k in range(1, max_k+1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
    return inertias

# Streamlit App
st.title("KMeans Clustering with Elbow Method")

# Sidebar for k selection
st.sidebar.header("Cluster Settings")
max_k = st.sidebar.slider("Max K for Elbow Curve", 3, 15, 10)
show_elbow = st.sidebar.checkbox("Show Elbow Curve", value=True)

# Elbow curve
inertias = calculate_elbow(X, max_k=max_k)
ks = list(range(1, max_k + 1))

# Use KneeLocator to find the elbow
knee = KneeLocator(ks, inertias, curve='convex', direction='decreasing')
best_k = knee.knee if knee.knee else 3  # fallback to 3

if show_elbow:
    st.subheader("Elbow Method - Optimal K")
    fig_elbow, ax_elbow = plt.subplots()
    ax_elbow.plot(ks, inertias, marker='o')
    if best_k:
        ax_elbow.axvline(best_k, color='red', linestyle='--', label=f"Elbow at k={best_k}")
        ax_elbow.legend()
    ax_elbow.set_xlabel("Number of Clusters (k)")
    ax_elbow.set_ylabel("Inertia")
    st.pyplot(fig_elbow)

# User selects k for clustering
k = st.sidebar.slider("Choose number of clusters (k)", 1, max_k, best_k)

# KMeans with selected k
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(X)

# PCA for visualization
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Plotting KMeans clustering vs Ground Truth
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.scatter(X_reduced[:, 0], X_reduced[:, 1], c=labels, cmap='viridis', s=40)
ax1.set_title(f'KMeans Clustering (k={k})')

ax2.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y_true, cmap='viridis', s=40)
ax2.set_title('Ground Truth Labels')

st.pyplot(fig)
