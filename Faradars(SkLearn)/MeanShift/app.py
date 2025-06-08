# app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from MeanShift import mean_shift, group_clusters

st.set_page_config(page_title="Mean Shift Clustering (1D)", layout="centered")

st.title("📈 Mean Shift Clustering - 1D Interactive Demo")
st.write("""
This app demonstrates the **Mean Shift** algorithm in one dimension.
Points will shift iteratively to the average of their neighbors within a given bandwidth.
""")

# Sidebar for user inputs
st.sidebar.header("Settings")

num_points = st.sidebar.slider("Number of Points", 5, 30, 10)
min_val = st.sidebar.number_input("Minimum Value", value=0.0)
max_val = st.sidebar.number_input("Maximum Value", value=10.0)
bandwidth = st.sidebar.slider("Bandwidth", 0.1, 3.0, 1.0)
max_iter = st.sidebar.slider("Max Iterations", 10, 200, 100)
tol = st.sidebar.number_input("Convergence Tolerance", value=1e-3, format="%.5f")
random_seed = st.sidebar.number_input("Random Seed", value=42)

# Generate data
np.random.seed(int(random_seed))
data = np.round(np.random.uniform(min_val, max_val, num_points), 2)
data_list = list(data)

st.subheader("📌 Initial Data")
st.write("Generated Points:", data_list)

# Run mean shift
shifted, iterations = mean_shift(data_list, bandwidth, max_iter, tol)
cluster_ids, cluster_centers = group_clusters(shifted, tol=0.5)

# Output results
st.subheader("🔍 Results")
for i, (orig, final, steps, cid) in enumerate(zip(data_list, shifted, iterations, cluster_ids)):
    st.write(f"Point {i+1}: {orig} → {round(final, 3)} (Cluster {cid}, {steps} steps)")

# Visualization
st.subheader("🎨 Visualization")
fig, ax = plt.subplots(figsize=(10, 2))
colors = cm.get_cmap("tab10", len(cluster_centers))

for i in range(len(data_list)):
    ax.scatter(data_list[i], 0, color=colors(cluster_ids[i]), label=f"Cluster {cluster_ids[i]}" if i == cluster_ids.index(cluster_ids[i]) else "", s=80, edgecolor='black')
    ax.scatter(shifted[i], 0.1, color=colors(cluster_ids[i]), s=80)
    ax.plot([data_list[i], shifted[i]], [0, 0.1], color='gray', linestyle='--', alpha=0.4)

ax.set_yticks([])
ax.set_title("Mean Shift: Clustering and Movement")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=len(cluster_centers))
st.pyplot(fig)

st.markdown("---")
st.caption("Developed By Arash Niroumand")
