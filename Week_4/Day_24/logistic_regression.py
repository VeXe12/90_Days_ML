import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

print("Initializing Logistic Regression Classifier...\n")

# ==========================================
# 1. GENERATE SYNTHETIC CREDIT CARD DATA
# ==========================================
np.random.seed(42)
n_customers = 1000

# Most people have low balances, some have high. 
balance = np.random.normal(1000, 500, n_customers)
income = np.random.normal(50000, 15000, n_customers)

# The Hidden Math: Higher balance significantly increases odds of default
log_odds = -10 + 0.006 * balance + 0.00001 * income
# Apply the Sigmoid/Logistic function to squash into probabilities between 0 and 1
probability_of_default = 1 / (1 + np.exp(-log_odds))

# Generate actual default labels (1 or 0) based on those probabilities
default = np.random.binomial(1, probability_of_default)

df = pd.DataFrame({'Balance': balance, 'Income': income, 'Default': default})
print("--- Sample Customer Data ---")
print(df.head(), "\n")

# ==========================================
# 2. PREPARE & SCALE THE DATA
# ==========================================
X = df[['Balance', 'Income']]
y = df['Default']

# Split into 80% Training and 20% Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling: Crucial for Logistic Regression to perform gradient descent efficiently
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 3. TRAIN THE MODEL
# ==========================================
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# ==========================================
# 4. EVALUATE THE MODEL
# ==========================================
# Predict exact classes (0 or 1)
y_pred = model.predict(X_test_scaled)

# Predict mathematical probabilities (the S-Curve output)
y_probabilities = model.predict_proba(X_test_scaled)

print("--- Model Evaluation ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")

print("--- Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
print("              Predicted No Default | Predicted Default")
print(f"Actual No Default:        {cm[0][0]}      |        {cm[0][1]}")
print(f"Actual Default:           {cm[1][0]}       |        {cm[1][1]}\n")

print("--- Behind the Scenes: Probability Outputs ---")
# Show the first 5 test customers: [Probability of 0, Probability of 1]
print(np.round(y_probabilities[:5], 3))