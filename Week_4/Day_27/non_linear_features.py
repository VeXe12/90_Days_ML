import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, SplineTransformer
from sklearn.pipeline import make_pipeline

print("Initializing Feature Engineering Engine...\n")

# ==========================================
# 1. GENERATE SYNTHETIC DATA (Age vs Wage)
# ==========================================
np.random.seed(42)
# Simulate 200 workers with ages ranging from 18 to 80
age = np.linspace(18, 80, 200).reshape(-1, 1)

# The Hidden Math: Earning potential peaks in middle age, forming a parabola
true_wage = 50 + 2.5 * age - 0.025 * age**2
# Add random real-world noise (variance)
wage = true_wage + np.random.normal(0, 10, size=age.shape)

# ==========================================
# 2. POLYNOMIAL REGRESSION
# ==========================================
# Transforms [X] into [X, X^2, X^3]
poly_pipe = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
poly_pipe.fit(age, wage)
poly_pred = poly_pipe.predict(age)

# ==========================================
# 3. STEP FUNCTIONS (Piecewise Constant)
# ==========================================
# Chop the continuous Age variable into 4 distinct bins
age_binned = pd.cut(age.flatten(), bins=4)
# One-Hot Encode the bins so the Linear Model can read them
age_dummies = pd.get_dummies(age_binned, drop_first=True)

step_model = LinearRegression()
step_model.fit(age_dummies, wage)
step_pred = step_model.predict(age_dummies)

# ==========================================
# 4. REGRESSION SPLINES
# ==========================================
# Places knots in the data and fits smooth cubic polynomials between them
spline_pipe = make_pipeline(SplineTransformer(degree=3, n_knots=4), LinearRegression())
spline_pipe.fit(age, wage)
spline_pred = spline_pipe.predict(age)

# ==========================================
# 5. VISUALIZE THE ENGINEERED FEATURES
# ==========================================
plt.figure(figsize=(10, 6))
plt.scatter(age, wage, color='lightgray', label='Raw Data (Age vs Wage)')

# Plotting our three different feature engineering approaches
plt.plot(age, poly_pred, color='blue', linewidth=2.5, label='Polynomial (Degree 3)')
plt.plot(age, step_pred, color='green', linewidth=2.5, label='Step Function (4 Bins)')
plt.plot(age, spline_pred, color='red', linewidth=2.5, label='Cubic Spline (4 Knots)')

plt.xlabel('Age', fontsize=14)
plt.ylabel('Wage ($)', fontsize=14)
plt.title('Moving Beyond Linearity: Feature Engineering', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Script complete! Please check the generated plot.")