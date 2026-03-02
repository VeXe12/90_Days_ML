import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

print("Initializing Unsupervised Learning Engine...\n")

# ==========================================
# 1. GENERATE SYNTHETIC HIGH-DIMENSIONAL DATA
# ==========================================
# 60 observations, 50 variables, 3 true classes
np.random.seed(42)
X = np.random.standard_normal((60, 50))

# Shift the means to create 3 distinct hidden clusters
X[:20, :10] += 3      # Class 0: shift first 10 features
X[20:40, 10:20] += 3  # Class 1: shift next 10 features
X[40:, 20:30] += 3    # Class 2: shift next 10 features

# These labels are strictly for our visualization, the algorithms WON'T see them!
true_labels = np.array([0]*20 + [1]*20 + [2]*20)

# ==========================================
# 2. PRINCIPAL COMPONENT ANALYSIS (PCA)
# ==========================================
print("Scaling data and computing Principal Components...")
# It is crucial to scale variables to have standard deviation 1 before PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# We want to compress the 50 features down to just 2 dimensions
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Variance explained by PC1: {pca.explained_variance_ratio_[0]:.2%}")
print(f"Variance explained by PC2: {pca.explained_variance_ratio_[1]:.2%}")
# ==========================================
# 3. HIERARCHICAL CLUSTERING
# ==========================================
print("Calculating Complete Linkage for Hierarchical Clustering...")
# Compute the distance matrix and linkages
linkage_comp = linkage(X_scaled, method='complete')

# ==========================================
# 4. VISUALIZATION
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: PCA Scatter Plot
colors = ['red', 'green', 'blue']
for i in range(3):
    ax1.scatter(X_pca[true_labels == i, 0], X_pca[true_labels == i, 1],
                c=colors[i], label=f'True Class {i}', s=60, edgecolors='k', alpha=0.8)
ax1.set_title("PCA: 50D Data Compressed to 2D", fontsize=14)
ax1.set_xlabel("First Principal Component (PC1)", fontsize=12)
ax1.set_ylabel("Second Principal Component (PC2)", fontsize=12)
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)

# Plot 2: Dendrogram
dendrogram(linkage_comp, ax=ax2, color_threshold=0, above_threshold_color='black')
ax2.set_title("Hierarchical Clustering Dendrogram", fontsize=14)
ax2.set_xlabel("Observation Index", fontsize=12)
ax2.set_ylabel("Euclidean Distance (Complete Linkage)", fontsize=12)

plt.tight_layout()
plt.show()

print("\nScript complete! Please check the generated plots.")