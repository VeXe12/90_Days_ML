import sys

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        # Tree size is generally 4*n to handle all splits
        self.tree = [0] * (4 * self.n)
        self.data = data
        
        # Build the tree initially
        # node 1 is the root, covering range [0, n-1]
        self._build(node=1, start=0, end=self.n - 1)

    def _build(self, node, start, end):
        """
        Recursively builds the tree. 
        Top-down approach: Divide range until we hit a single element (leaf).
        """
        if start == end:
            # Leaf node: store the actual value
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            # Recursively build left and right children
            # Left child index: 2*node, Right child index: 2*node + 1
            self._build(2 * node, start, mid)
            self._build(2 * node + 1, mid + 1, end)
            
            # Internal node: Sum of children
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, idx, val):
        """
        Updates the value at data[idx] to val.
        """
        self._update_recursive(1, 0, self.n - 1, idx, val)

    def _update_recursive(self, node, start, end, idx, val):
        if start == end:
            # Leaf node found: update value
            self.tree[node] = val
            self.data[idx] = val # Update original data reference
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                # If index is in the left child
                self._update_recursive(2 * node, start, mid, idx, val)
            else:
                # If index is in the right child
                self._update_recursive(2 * node + 1, mid + 1, end, idx, val)
            
            # Recalculate parent sum after child update
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, L, R):
        """
        Returns the sum of data[L...R] inclusive.
        """
        return self._query_recursive(1, 0, self.n - 1, L, R)

    def _query_recursive(self, node, start, end, L, R):
        # Case 1: Range completely outside (No overlap)
        if R < start or end < L:
            return 0
        
        # Case 2: Range completely inside (Total overlap)
        if L <= start and end <= R:
            return self.tree[node]
        
        # Case 3: Partial overlap - Split and recurse
        mid = (start + end) // 2
        left_sum = self._query_recursive(2 * node, start, mid, L, R)
        right_sum = self._query_recursive(2 * node + 1, mid + 1, end, L, R)
        
        return left_sum + right_sum

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    # Sample Data: Sales over 6 days
    sales_data = [5, 7, 9, 11, 13, 15]
    st = SegmentTree(sales_data)

    print(f"Original Data: {sales_data}")
    
    # Query Range [7, 8] -> indices 2, 3, 4 -> 5 + 7 + 9 = 21
    print(f"Sum of range [7, 8]: {st.query(2, 4)}")
    
    print("\n--- Updating index 3 (value 7) to 10 ---")
    st.update(3, 10)
    print(f"New Data: {st.data}")
    
    # Query Range [7, 8] again -> 5 + 10 + 9 = 24
    print(f"Sum of range [7, 8] after update: {st.query(2, 4)}")