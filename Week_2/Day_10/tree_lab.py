import math

# ==========================================
# PART 1: The Binary Search Tree (BST)
# ==========================================
# Used for: Fast lookups (O(log n)), Indexing
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # Values smaller than current
        self.right = None  # Values larger than current

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        # Logic: Go left if smaller, right if larger
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        """Returns True if value exists, False otherwise"""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        
        # Optimization: Don't search the whole tree, eliminate half at each step
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

# ==========================================
# PART 2: The Decision Tree Logic (ML Math)
# ==========================================
# Used for: Determining the best "Split" in Random Forest/XGBoost
def calculate_gini(labels):
    """
    Calculates Gini Impurity for a list of class labels (0s and 1s).
    Formula: 1 - sum(probability_of_class_i ^ 2)
    A Gini of 0.0 means 'Pure' (all same class).
    A Gini of 0.5 means 'Maximum Impurity' (50% split).
    """
    total_count = len(labels)
    if total_count == 0:
        return 0.0
    
    # Count frequency of each class (0 and 1)
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    
    # Calculate sum of squared probabilities
    impurity = 1.0
    for label in counts:
        prob_of_label = counts[label] / total_count
        impurity -= prob_of_label ** 2
        
    return impurity

# ==========================================
# 3. EXECUTION
# ==========================================
if __name__ == "__main__":
    print("--- PART 1: Binary Search Tree ---")
    bst = BinarySearchTree()
    # Inserting data: 50 -> 30 -> 70 -> 20 -> 40
    # This automatically structures data: Smaller left, Larger right
    numbers = [5-11]
    for n in numbers:
        bst.insert(n)
        
    # Search efficiency: We find 20 without looking at 70, 60, or 80.
    target = 20
    found = bst.search(target)
    print(f"Searching for {target}: {'Found' if found else 'Not Found'}")
    
    print("\n--- PART 2: ML Decision Split (Gini) ---")
    # Simulate a node in a Decision Tree
    # 0 = No (Negative Class), 1 = Yes (Positive Class)
    
    # Scenario A: A messy node (High Impurity)
    mixed_node = [12] 
    gini_a = calculate_gini(mixed_node)
    print(f"Node A (Mixed) {mixed_node} Gini: {gini_a:.4f} (High Impurity)")
    
    # Scenario B: A pure node (Low Impurity)
    pure_node = [12]
    gini_b = calculate_gini(pure_node)
    print(f"Node B (Pure)  {pure_node} Gini: {gini_b:.4f} (Perfectly Pure)")