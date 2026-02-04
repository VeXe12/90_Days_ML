import time
import sys

# 1. VISUALIZE THE STACK
# Python has a limit on how many function calls can be "active" at once.
# This prevents infinite recursion from crashing your entire OS.
print(f"Current Recursion Limit: {sys.getrecursionlimit()}")

def crash_the_stack(n):
    try:
        # Recursive step: calling itself
        return crash_the_stack(n + 1)
    except RecursionError:
        print(f"CRASHED! Stack overflowed at depth: {n}")
        return n

# Uncomment this line to see the crash (it's safe, Python catches it)
crash_the_stack(0)


# 2. THE ALGORITHMS
def linear_search(arr, target):
    """
    Scans every item one by one. O(n).
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search_recursive(arr, target, left, right):
    """
    Divides the search space in half each time. O(log n).
    Requires a SORTED array.
    """
    # Base Case: The search space is empty
    if left > right:
        return -1
    
    # Calculate middle index
    mid = (left + right) // 2
    
    # Base Case: Found it!
    if arr[mid] == target:
        return mid
    
    # Recursive Step: Choose the left or right half
    elif arr[mid] < target:
        # Target is in the right half
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        # Target is in the left half
        return binary_search_recursive(arr, target, left, mid - 1)

# 3. THE BENCHMARK
# Create a massive sorted dataset (10 million numbers)
size = 10_000_000
data = list(range(size))
target = size - 1  # Worst case: looking for the very last number

print(f"\nSearching for {target} in {size} items...")

# Test Linear
start = time.time()
linear_search(data, target)
print(f"Linear Search: {time.time() - start:.6f} seconds")

# Test Binary (Recursive)
start = time.time()
binary_search_recursive(data, target, 0, len(data) - 1)
print(f"Binary Search: {time.time() - start:.6f} seconds")