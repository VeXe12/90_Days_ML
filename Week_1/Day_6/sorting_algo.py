import time
import random

# ---------------------------------------------------------
# 1. THE NAIVE APPROACH: Bubble Sort
# Time Complexity: O(N^2)
# Strategy: Repeatedly swap adjacent elements if they are wrong.
# ---------------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    # We work on a copy to keep the benchmark fair
    arr = arr.copy() 
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ---------------------------------------------------------
# 2. THE ENGINEER'S APPROACH: Merge Sort (Recursive)
# Time Complexity: O(N log N)
# Strategy: Divide & Conquer. Split list in half, sort halves, merge.
# ---------------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # DIVIDE: Find the middle and split [2]
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # CONQUER: Merge the sorted halves [3]
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # Compare pointers and append smaller value
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # Append any remaining items (one list will be empty)
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

# ---------------------------------------------------------
# 3. THE BENCHMARK
# ---------------------------------------------------------
if __name__ == "__main__":
    # Generate 5,000 random numbers
    # (Bubble sort is too slow for 1M items, so we keep N small)
    N = 5000
    data = [random.randint(0, 10000) for _ in range(N)]
    print(f"Sorting {N} elements...")

    # Test 1: Bubble Sort (O(N^2))
    start = time.time()
    bubble_sort(data)
    print(f"Bubble Sort:     {time.time() - start:.4f} seconds")

    # Test 2: Merge Sort (O(N log N))
    start = time.time()
    merge_sort(data)
    print(f"Merge Sort:      {time.time() - start:.4f} seconds")

    # Test 3: Python's Built-in Sort (Timsort)
    # Timsort is a hybrid of Merge Sort + Insertion Sort [4]
    start = time.time()
    sorted(data) 
    print(f"Python (Timsort): {time.time() - start:.4f} seconds")
