import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Set up Streamlit page
st.set_page_config(page_title="Interactive Linear Regression", layout="centered")
st.title("🔍 Linear Regression Visualizer with Residuals")

# Generate synthetic data
np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 2 * X + 1 + np.random.normal(0, 1, (100, 1))

# Train a real model for comparison
model = LinearRegression()
model.fit(X, y)
y_pred_model = model.predict(X)
mse_model = mean_squared_error(y, y_pred_model)

# Sidebar sliders for manual line
st.sidebar.header("Manual Line Parameters")
slope = st.sidebar.slider("Slope (coefficient)", min_value=0.0, max_value=5.0, value=2.0, step=0.1)
intercept = st.sidebar.slider("Intercept", min_value=-5.0, max_value=10.0, value=1.0, step=0.1)

# Predict with manual line
y_manual = slope * X + intercept
residuals = y - y_manual
mse_manual = mean_squared_error(y, y_manual)

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# --- Top plot: Regression lines and data ---
ax1.scatter(X, y, color='blue', label='Data points', alpha=0.6)
ax1.plot(X, y_pred_model, color='green', label=f'Model: y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f}')
ax1.plot(X, y_manual, color='red', linestyle='--', label=f'Your Line: y = {slope:.2f}x + {intercept:.2f}')
ax1.set_title("Regression Lines")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.legend()
ax1.grid(True)

# --- Bottom plot: Residuals ---
ax2.scatter(X, residuals, alpha=0.7, color='orange')
ax2.axhline(y=0, color='red', linestyle='--')
ax2.set_title("Residual Plot (Your Line)")
ax2.set_xlabel("X")
ax2.set_ylabel("Residuals")
ax2.grid(True)

# Show plots and metrics
st.pyplot(fig)

st.markdown("---")
st.subheader("📈 MSE Comparison")
st.write(f"**Real model MSE:** {mse_model:.4f}")
st.write(f"**Your model MSE:** {mse_manual:.4f}")
