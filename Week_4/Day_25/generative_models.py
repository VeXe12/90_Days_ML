import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

print("Initializing Generative Models...\n")

# ==========================================
# 1. GENERATE SYNTHETIC MEDICAL DATA
# ==========================================
np.random.seed(42)
n_samples = 1000

# Class 0: Healthy (Normally distributed, tight variance)
healthy_bio1 = np.random.normal(50, 10, n_samples // 2)
healthy_bio2 = np.random.normal(50, 10, n_samples // 2)

# Class 1: Diseased (Normally distributed, much wider variance)
# Notice how the standard deviation (variance) is 25 here, but 10 for Healthy!
disease_bio1 = np.random.normal(65, 25, n_samples // 2)
disease_bio2 = np.random.normal(65, 25, n_samples // 2)

X = np.vstack((np.column_stack((healthy_bio1, healthy_bio2)), 
               np.column_stack((disease_bio1, disease_bio2))))
y = np.hstack((np.zeros(n_samples // 2), np.ones(n_samples // 2)))

df = pd.DataFrame({'Biomarker_1': X[:, 0], 'Biomarker_2': X[:, 1], 'Diagnosis': y})

# ==========================================
# 2. PREPARE THE DATA
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ==========================================
# 3. TRAIN AND EVALUATE MODELS
# ==========================================
models = {
    "Linear Discriminant Analysis (LDA)": LinearDiscriminantAnalysis(),
    "Quadratic Discriminant Analysis (QDA)": QuadraticDiscriminantAnalysis(),
    "Gaussian Naive Bayes": GaussianNB()
}

for name, model in models.items():
    # Fit the model (This computes the Prior Probabilities and Density Functions)
    model.fit(X_train, y_train)
    
    # Make Predictions
    y_pred = model.predict(X_test)
    
    # Evaluate
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    print(f"--- {name} ---")
    print(f"Accuracy: {acc * 100:.2f}%")
    print(f"Confusion Matrix:\n{cm}\n")

# ==========================================
# 4. LOOKING UNDER THE HOOD (NAIVE BAYES)
# ==========================================
print("--- Under the Hood: Naive Bayes Priors ---")
nb_model = models["Gaussian Naive Bayes"]
print(f"Probability of Healthy (Prior): {nb_model.class_prior_[0]*100:.2f}%")
print(f"Probability of Diseased (Prior): {nb_model.class_prior_[1]*100:.2f}%")