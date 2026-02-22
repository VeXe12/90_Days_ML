import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# ==========================================
# 1. CREATE THE MESSY DATASET
# ==========================================
data = {
    'Age': [25, 32, np.nan, 47, 51, 22, np.nan, 38],
    'Salary': [50000, 64000, 58000, np.nan, 120000, 45000, 85000, 72000],
    'City': ['New York', 'London', 'London', 'Paris', np.nan, 'New York', 'Paris', 'London'],
    'Purchased_App': ['No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No'] # Target variable
}
df = pd.DataFrame(data)

print("--- 🛑 ORIGINAL MESSY DATA ---")
print(df)

# Separate Features (X) from the Target (y)
X = df.drop('Purchased_App', axis=1)
y = df['Purchased_App']

# ==========================================
# 2. DEFINE THE PIPELINE STEPS
# ==========================================
# Tell the pipeline which columns are numbers and which are text
numeric_features = ['Age', 'Salary']
categorical_features = ['City']

# Pipeline for Numbers: Fill missing with Mean -> Scale to standard normal distribution
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Pipeline for Text: Fill missing with most frequent -> One-Hot Encode (convert to 1s and 0s)
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine both pipelines into a single master engine
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# ==========================================
# 3. EXECUTE THE PIPELINE
# ==========================================
# .fit_transform() learns the means/scales and applies them to the data simultaneously
X_processed = preprocessor.fit_transform(X)

print("\n--- ✅ CLEANED & MATHEMATICALLY READY DATA (X_processed) ---")
# Print rounded to 2 decimal places for readability
print(np.round(X_processed, 2))

# Notice the output columns:
# Column 0: Scaled Age
# Column 1: Scaled Salary
# Columns 2, 3, 4: One-Hot Encoded City (London, New York, Paris)