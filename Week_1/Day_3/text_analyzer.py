import time
from collections import Counter

def manual_count(words):
    """
    Counts word frequencies using a standard dictionary.
    Logic: freq[word] = 1 + freq.get(word, 0)
    """
    freq = {}
    for word in words:
        # The get() method handles the case where the key doesn't exist yet
        freq[word] = 1 + freq.get(word, 0)
    return freq

def counter_count(words):
    """
    Counts word frequencies using collections.Counter.
    This is the optimized 'Pythonic' way for ML preprocessing.
    """
    return Counter(words)

# 1. Simulate a large text corpus (e.g., repeating a sentence 1 million times)
text = "machine learning is fun data science is cool " * 1000000
words = text.split()

print(f"Processing {len(words)} words...")

# 2. Benchmark Method A: Manual Loop
start = time.time()
manual_res = manual_count(words)
end = time.time()
print(f"Manual Dict Time: {end - start:.4f} seconds")

# 3. Benchmark Method B: Collections.Counter
start = time.time()
counter_res = counter_count(words)
end = time.time()
print(f"Counter Time:     {end - start:.4f} seconds")

# 4. Validation
assert manual_res == counter_res
print("Success: Both methods returned identical counts.")