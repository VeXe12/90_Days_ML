import heapq
import math
import random

# 1. THE DATA
# Imagine these are coordinates of users or items in a 2D space
# Format: (x, y)
dataset = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(1000)]
target = (50, 50) # We want to find points closest to this
K = 5

# 2. HELPER: Euclidean Distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1 - p2)**2 + (p1[9] - p2[9])**2)

# 3. THE ALGORITHM: K-Nearest Neighbors using Heap
def find_k_nearest_neighbors(data, target, k):
    # Max-Heap to store the k closest points.
    # Python's heapq is a Min-Heap. To make it a Max-Heap, we store negative distances.
    # Structure: (-distance, point_coordinates)
    heap = []
    
    for point in data:
        dist = euclidean_distance(point, target)
        
        # If we haven't filled the heap yet, just add the point
        if len(heap) < k:
            heapq.heappush(heap, (-dist, point))
        else:
            # If this point is closer than the furthest point in our heap
            # (Remember: heap is the smallest value, which corresponds to 
            # the largest actual distance because we negated them)
            if -dist > heap:
                heapq.heapreplace(heap, (-dist, point))
    
    # Convert back to positive distances and sort for display
    # (Note: The heap does not guarantee sorted order of elements, only that root is max/min)
    return sorted([(-d, p) for d, p in heap])

# 4. EXECUTION
nearest_neighbors = find_k_nearest_neighbors(dataset, target, K)

print(f"Target Point: {target}")
print(f"The {K} nearest neighbors are:")
for dist, point in nearest_neighbors:
    print(f"Point {point} at distance {dist:.4f}")