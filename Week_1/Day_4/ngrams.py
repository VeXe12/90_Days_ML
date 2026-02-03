import time
import sys

# ---------------------------------------------------------
# THEORY: N-Grams
# An N-gram is a sequence of N items from a text.
# Bi-gram (N=2): "machine learning", "learning is"
# Tri-gram (N=3): "machine learning is", "learning is fun"
# ---------------------------------------------------------

def generate_ngrams_naive(words, n):
    """
    Naive approach: String concatenation (Slow).
    In Python, strings are immutable. Doing 's += word' creates 
    a NEW string object in memory every time.
    """
    output = []
    for i in range(len(words) - n + 1):
        gram = ""
        for j in range(n):
            gram += words[i + j] + " " # Expensive operation
        output.append(gram.strip())
    return output

def generate_ngrams_sliding_window(words, n):
    """
    Optimized approach: Sliding Window + Join (Fast).
    We slice the list (window) and join it at the end.
    This is O(N) linear time.
    """
    output = []
    # The 'window' slides from index 0 to len - n
    for i in range(len(words) - n + 1):
        # Select the window of 'n' words
        window = words[i : i + n] 
        # Join them efficiently
        output.append(" ".join(window)) 
    return output

# --- Execution ---
text = "machine learning is the study of computer algorithms that improve automatically through experience " * 10000
words = text.split()
N = 3

print(f"Processing {len(words)} words for {N}-grams...")

# Measure Naive
start = time.time()
naive_result = generate_ngrams_naive(words, N)
end = time.time()
print(f"Naive Method:   {end - start:.4f} seconds")

# Measure Sliding Window
start = time.time()
window_result = generate_ngrams_sliding_window(words, N)
end = time.time()
print(f"Sliding Window: {end - start:.4f} seconds")

# Validation
assert naive_result == window_result
print("\nSuccess: Both methods produced the same output.")