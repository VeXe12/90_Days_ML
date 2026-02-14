import heapq

# 1. THE DATA STRUCTURE: Weighted Graph
# We use a Dict of Dicts: { Node: { Neighbor: Weight, ... } }
# This allows O(1) lookup for edge weights.
class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        
        # Add edge with weight
        self.graph[u][v] = weight
        # If undirected, uncomment the next line:
        # self.graph[v][u] = weight 

    # 2. THE ALGORITHM: Dijkstra's Shortest Path
    # Uses a Min-Heap (Priority Queue) to greedily pick the closest node.
    def dijkstra(self, start_node, end_node):
        # Distances: Map node -> shortest distance found so far.
        # Initialize with infinity for all except start.
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0
        
        # Priority Queue: Stores tuples (current_distance, current_node)
        # We start at the source with distance 0.
        pq = [(0, start_node)]
        
        # Predecessors: To reconstruct the path later
        predecessors = {}

        while pq:
            # GREEDY STEP: Pop the node with the smallest distance
            current_dist, current_node = heapq.heappop(pq)

            # Optimization: If we reached the target, we can stop early
            if current_node == end_node:
                break

            # Lazy Deletion handling: If we found a shorter path to this node 
            # *after* pushing this tuple to the heap, ignore this stale entry.
            if current_dist > distances[current_node]:
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[current_node].items():
                distance = current_dist + weight

                # RELAXATION STEP: If we found a shorter path, update it
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    # Push new best distance to heap
                    heapq.heappush(pq, (distance, neighbor))
        
        return self._reconstruct_path(predecessors, start_node, end_node), distances[end_node]

    def _reconstruct_path(self, predecessors, start, end):
        path = []
        current = end
        while current != start:
            try:
                path.append(current)
                current = predecessors[current]
            except KeyError:
                return None # Path not found
        path.append(start)
        return path[::-1] # Reverse to get Start -> End

# 3. EXECUTION
if __name__ == "__main__":
    city_map = WeightedGraph()
    # Edges: (Source, Destination, Minutes of Traffic)
    edges = [
        ('Home', 'A', 5), ('Home', 'B', 2),
        ('A', 'C', 4), ('A', 'B', 8),
        ('B', 'A', 8), ('B', 'D', 7),
        ('C', 'D', 6), ('C', 'Office', 3),
        ('D', 'Office', 1)
    ]
    
    for u, v, w in edges:
        city_map.add_edge(u, v, w)

    start, end = 'Home', 'Office'
    print(f"--- Calculating Fastest Route: {start} -> {end} ---")
    
    path, time = city_map.dijkstra(start, end)
    
    if path:
        print(f"Route Found: {' -> '.join(path)}")
        print(f"Total Time: {time} minutes")
    else:
        print("No path exists.")