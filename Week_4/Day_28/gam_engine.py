import numpy as np
import matplotlib.pyplot as plt
from pygam import LinearGAM, s, l, f

print("Initializing Generalized Additive Models (GAMs) Engine...\n")

# ==========================================
# 1. GENERATE SYNTHETIC DATA (The 3 Features)
# ==========================================
np.random.seed(42)
n_samples = 500

# Feature 0: Age (18 to 65) -> Non-linear relationship (Parabola)
age = np.random.uniform(18, 65, n_samples)
wage_age = 50 + 2.5 * age - 0.03 * age**2

# Feature 1: Year (2010 to 2025) -> Linear relationship (Straight line)
year = np.random.randint(2010, 2026, n_samples)
wage_year = 2 * (year - 2010)

# Feature 2: Education (0: HS, 1: College, 2: Grad) -> Step function
education = np.random.randint(0, 3, n_samples)
wage_edu = np.where(education == 0, 0, np.where(education == 1, 15, 35))

# The Target Variable (Y) = The sum of all effects + Random Noise
wage = wage_age + wage_year + wage_edu + np.random.normal(0, 5, n_samples)

# Combine features into our X matrix
X = np.column_stack((age, year, education))
y = wage

# ==========================================
# 2. BUILD THE GAM
# ==========================================
print("Fitting the GAM...")
# s(0) means apply a Spline to column 0 (Age)
# l(1) means apply a Linear line to column 1 (Year)
# f(2) means treat column 2 (Education) as a categorical Factor
gam = LinearGAM(s(0) + l(1) + f(2))

# gridsearch() automatically finds the best smoothing penalty (lambda) using Cross-Validation!
gam.gridsearch(X, y)

print("\nModel Summary:")
print(gam.summary())

# ==========================================
# 3. VISUALIZE THE ISOLATED EFFECTS (PDPs)
# ==========================================
print("\nGenerating Partial Dependence Plots...")
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
titles = ['Effect of Age (Spline)', 'Effect of Year (Linear)', 'Effect of Education (Factor)']

for i, ax in enumerate(axs):
    # Generate a grid of values for the current feature
    XX = gam.generate_X_grid(term=i)
    
    # Calculate the isolated partial dependence and 95% confidence intervals
    pdep, conf_intervals = gam.partial_dependence(term=i, X=XX, width=0.95)
    
    ax.plot(XX[:, i], pdep, color='blue', linewidth=2)
    ax.fill_between(XX[:, i], conf_intervals[:, 0], conf_intervals[:, 1], color='blue', alpha=0.1)
    
    ax.set_title(titles[i], fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

print("Script complete! Please check the generated plots.")