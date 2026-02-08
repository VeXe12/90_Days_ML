import time
from collections import deque

# Constants
DATA_SIZE = 100000  # Number of items to process

# ---------------------------------------------------------
# 1. THE TRAP: Using a List as a Queue
# ---------------------------------------------------------
def list_queue_simulation():
    print(f"\n--- Simulating List Queue (Size: {DATA_SIZE}) ---")
    queue = []
    
    # Enqueue (Append is O(1) - Fast)
    start_time = time.time()
    for i in range(DATA_SIZE):
        queue.append(i)
    print(f"List Enqueue: {time.time() - start_time:.4f} seconds")
    
    # Dequeue (Pop(0) is O(N) - SLOW)
    # Every time we remove index 0, Python shifts 99,999 items left.
    start_time = time.time()
    while queue:
        queue.pop(0) 
    print(f"List Dequeue: {time.time() - start_time:.4f} seconds")

# ---------------------------------------------------------
# 2. THE SOLUTION: Using collections.deque
# ---------------------------------------------------------
def deque_queue_simulation():
    print(f"\n--- Simulating Deque (Size: {DATA_SIZE}) ---")
    queue = deque()
    
    # Enqueue (Append is O(1) - Fast)
    start_time = time.time()
    for i in range(DATA_SIZE):
        queue.append(i)
    print(f"Deque Enqueue: {time.time() - start_time:.4f} seconds")
    
    # Dequeue (Popleft is O(1) - FAST)
    # Deque is a Doubly Linked List; removing the head is instant.
    start_time = time.time()
    while queue:
        queue.popleft()
    print(f"Deque Dequeue: {time.time() - start_time:.4f} seconds")

# ---------------------------------------------------------
# 3. EXECUTION
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Benchmarking Queue Implementations...")
    
    # Run Deque first to show how fast it should be
    deque_queue_simulation()
    
    # Run List second to feel the pain
    list_queue_simulation()