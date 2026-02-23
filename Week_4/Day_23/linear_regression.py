import pandas as pd
import numpy as np
import statsmodels.api as sm

print("Initializing Linear Regression Engine...\n")

# ==========================================
# 1. GENERATE SYNTHETIC ADVERTISING DATA
# ==========================================
# We simulate 100 different markets (rows)
np.random.seed(42)
n_markets = 100

TV_budget = np.random.uniform(0, 300, n_markets)
Radio_budget = np.random.uniform(0, 50, n_markets)

# The True Hidden Math: Sales depend on TV, Radio, AND their synergy
# Sales = 7 (Base) + 0.05(TV) + 0.2(Radio) + 0.001(TV * Radio) + Noise
Sales = 7 + (0.05 * TV_budget) + (0.2 * Radio_budget) + (0.001 * TV_budget * Radio_budget) + np.random.normal(0, 2, n_markets)

# Load into a Pandas DataFrame
df = pd.DataFrame({'TV': TV_budget, 'Radio': Radio_budget, 'Sales': Sales})

# Create the Interaction Term (Synergy)
df['TV_x_Radio'] = df['TV'] * df['Radio']

print("--- Sample of our Advertising Data ---")
print(df.head(), "\n")

# ==========================================
# 2. PREPARE THE MODEL INPUTS
# ==========================================
# Select our features (X) and our target (y)
X = df[['TV', 'Radio', 'TV_x_Radio']]
y = df['Sales']

# statsmodels requires us to explicitly add a constant to calculate the Intercept (Beta 0)
X = sm.add_constant(X)

# ==========================================
# 3. FIT THE OLS (Ordinary Least Squares) MODEL
# ==========================================
# We use sm.OLS to fit the linear regression model
model = sm.OLS(y, X)
results = model.fit()

# ==========================================
# 4. PRINT THE MATHEMATICAL READOUT
# ==========================================
print(results.summary())
