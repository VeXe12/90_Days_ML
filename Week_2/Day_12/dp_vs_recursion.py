import time
import sys

# Increase recursion depth just in case, though DP avoids this limit
sys.setrecursionlimit(2000)

# ==========================================
# PART 1: The Benchmark (Fibonacci)
# ==========================================

# 1. Naive Recursion (O(2^N) - Exponential Time)
# This calculates the same subproblems over and over.
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# 2. Top-Down DP (Memoization) (O(N) - Linear Time)
# We use a dictionary 'memo' to cache results we've already computed.
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# 3. Bottom-Up DP (Tabulation) (O(N) - Linear Time)
# We eliminate recursion entirely and fill a table iteratively.
def fib_tab(n):
    if n <= 1:
        return n
    
    # Initialize table [0, 1, 0, 0, ...]
    table = [0] * (n + 1)
    table[1] = 1
    
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
        
    return table[n]

# ==========================================
# PART 2: Real World Optimization (House Robber)
# ==========================================
# Problem: Maximize money stolen from houses [1-3] without robbing adjacent ones.
# Logic: dp[i] = max(loot[i] + dp[i-2], dp[i-1])

def rob_houses(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # DP Table
    dp = [0] * len(nums)
    
    # Base Cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # Fill table
    for i in range(2, len(nums)):
        # Choice: Rob current house (and house i-2) OR skip current (keep loot from i-1)
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
    return dp[-1]

# ==========================================
# 3. EXECUTION & BENCHMARK
# ==========================================
if __name__ == "__main__":
    n = 35  # Try 40 if your machine is fast. DO NOT try 50 with naive.
    
    print(f"--- Benchmarking Fibonacci({n}) ---")
    
    # Test Naive
    start = time.time()
    result = fib_naive(n)
    print(f"Naive Recursion: {result} (Time: {time.time() - start:.4f}s)")
    
    # Test Memoization
    start = time.time()
    result = fib_memo(n)
    print(f"Memoization:     {result} (Time: {time.time() - start:.4f}s)")
    
    # Test Tabulation
    start = time.time()
    result = fib_tab(n)
    print(f"Tabulation:      {result} (Time: {time.time() - start:.4f}s)")
    
    print("\n--- House Robber Optimization ---")
    neighborhoods = [
        [1, 3],
        [1, 5],
        [2, 2] # Tricky case: equal houses
    ]
    
    for hood in neighborhoods:
        print(f"Houses: {hood} -> Max Loot: ${rob_houses(hood)}")