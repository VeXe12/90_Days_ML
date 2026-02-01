import time

# 1. The Iterative Approach (O(n))
# This has to perform 'n' operations. If n doubles, time doubles.
def sum_loop(n):
    start = time.time()
    result = 0
    for i in range(1, n + 1):
        result += i
    end = time.time()
    return result, end - start

# 2. The Mathematical Approach (O(1))
# This performs 3 operations (add, mult, div) regardless of how big n is.
def sum_formula(n):
    start = time.time()
    result = (n * (n + 1)) // 2  # Gaussian summation formula
    end = time.time()
    return result, end - start

# Test with a massive number (100 Million)
N = 100_000_000 
print(f"Calculating sum of 1 to {N}...")

# Measure Loop
sum_1, time_1 = sum_loop(N)
print(f"Loop Method:    {sum_1} | Time: {time_1:.6f} seconds")

# Measure Math
sum_2, time_2 = sum_formula(N)
print(f"Formula Method: {sum_2} | Time: {time_2:.6f} seconds")

# Calculate the winner
if time_2 > 0:
    speedup = time_1 / time_2
    print(f"\nMath is {speedup:.0f}x faster!")
else:
    print("\nMath was too fast to measure (instant).")