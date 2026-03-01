import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC

print("Initializing Support Vector Machine (SVM) Engine...\n")

# ==========================================
# 1. GENERATE SYNTHETIC NON-LINEAR DATA
# ==========================================
# We use make_circles to create a "bullseye" dataset (one class inside another)
X, y = make_circles(n_samples=400, factor=0.3, noise=0.1, random_state=42)

# ==========================================
# 2. DEFINE THE MODELS (Testing the Kernel Trick)
# ==========================================
# Model A: Linear Kernel (Will try to draw a straight line)
svm_linear = SVC(kernel='linear', C=1.0)

# Model B: RBF Kernel (Radial Basis Function - The "Bubble" maker)
# Gamma controls the 'spread' of the kernel. 
svm_rbf_good = SVC(kernel='rbf', gamma=1.0, C=1.0)

# Model C: RBF Kernel with HIGH Gamma (Massive Overfitting)
# A very high gamma means the similarity radius is tiny; it will draw tight bubbles around individual points.
svm_rbf_overfit = SVC(kernel='rbf', gamma=50.0, C=1.0)

models = [svm_linear, svm_rbf_good, svm_rbf_overfit]
titles = ['Linear Kernel (Underfit)', 'RBF Kernel (Good Fit)', 'RBF Kernel (Overfit, High Gamma)']

# ==========================================
# 3. TRAIN AND VISUALIZE THE BOUNDARIES
# ==========================================
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Create a mesh grid across the whole plot to calculate the decision boundary mathematically
xx, yy = np.meshgrid(np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 100),
                     np.linspace(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5, 100))

for ax, model, title in zip(axes, models, titles):
    print(f"Training {title}...")
    model.fit(X, y)
    
    # Predict the distance to the separating hyperplane for every point in the grid
    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot the decision boundaries (where Z = 0 is the exact hyperplane)
    ax.contourf(xx, yy, Z, levels=[-1, 0, 1], alpha=0.3, colors=['blue', 'gray', 'red'])
    ax.contour(xx, yy, Z, levels=[-1, 0, 1], linewidths=2, colors='black') # The actual Hyperplane
    
    # Scatter the actual training data points
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolors='k', s=30)
    ax.set_title(title, fontsize=14)
    ax.set_xticks(())
    ax.set_yticks(())

plt.tight_layout()
plt.show()

print("\nScript complete! Please check the generated plots.")