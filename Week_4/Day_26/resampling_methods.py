import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

print("Initializing Resampling Engine...\n")

# ==========================================
# 1. GENERATE SYNTHETIC NON-LINEAR DATA
# ==========================================
np.random.seed(42)
n_samples = 100
X = np.random.normal(0, 1, n_samples).reshape(-1, 1)

# The True Hidden Math: Y is a curve (quadratic), plus some random noise
y = 3 - 2 * X[:, 0] + 1.5 * X[:, 0]**2 + np.random.normal(0, 2, n_samples)

# ==========================================
# 2. THE VALIDATION SET APPROACH (80/20)
# ==========================================
print("--- 1. Validation Set Approach ---")
# Split the data [3]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
val_mse = np.mean((model.predict(X_test) - y_test)**2)
print(f"Validation Set MSE (Mean Squared Error): {val_mse:.4f}")
print("(Note: If you change the random_state, this number will jump around wildly!)\n")

# ==========================================
# 3. K-FOLD CROSS-VALIDATION (The Industry Standard)
# ==========================================
print("--- 2. K-Fold Cross-Validation (K=5) ---")
# Create the K-Fold splits [4]
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# We create two pipelines: A basic straight line, and a curve (Polynomial degree=2)
linear_pipe = make_pipeline(PolynomialFeatures(degree=1), LinearRegression())
quad_pipe = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())

# cross_val_score returns the error for EACH fold. We average them together.
# Scikit-Learn uses "neg_mean_squared_error" to treat all metrics as "higher is better", so we negate it back.
cv_linear_mse = -cross_val_score(linear_pipe, X, y, scoring='neg_mean_squared_error', cv=kf).mean()
cv_quad_mse = -cross_val_score(quad_pipe, X, y, scoring='neg_mean_squared_error', cv=kf).mean()

print(f"Linear Model CV MSE:    {cv_linear_mse:.4f}")
print(f"Quadratic Model CV MSE: {cv_quad_mse:.4f}")
print("-> K-Fold correctly proves that the Quadratic model performs significantly better!\n")

# ==========================================
# 4. LOOCV (Leave-One-Out Cross-Validation)
# ==========================================
print("--- 3. Leave-One-Out Cross-Validation (LOOCV) ---")
loo = LeaveOneOut()
loo_quad_mse = -cross_val_score(quad_pipe, X, y, scoring='neg_mean_squared_error', cv=loo).mean()
print(f"LOOCV Quadratic Model MSE (Computed by training {n_samples} separate models!): {loo_quad_mse:.4f}\n")

# ==========================================
# 5. THE BOOTSTRAP (Estimating Uncertainty)
# ==========================================
print("--- 4. The Bootstrap ---")
n_bootstraps = 1000
bootstrap_slopes = []

for _ in range(n_bootstraps):
    # Sample WITH REPLACEMENT from our dataset [2]
    indices = np.random.choice(n_samples, size=n_samples, replace=True)
    X_boot, y_boot = X[indices], y[indices]
    
    # Fit the model on the bootstrap sample and record the slope (coefficient)
    boot_model = LinearRegression().fit(X_boot, y_boot)
    bootstrap_slopes.append(boot_model.coef_)

# The standard deviation of our bootstrap estimates equals the Standard Error of our parameter!
se_slope = np.std(bootstrap_slopes)
print(f"We ran {n_bootstraps} bootstrapped models.")
print(f"Estimated Standard Error of the Linear Slope: {se_slope:.4f}")