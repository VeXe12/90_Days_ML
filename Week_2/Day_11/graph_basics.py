from collections import deque

# 1. THE STRUCTURE: Adjacency List
# We use a Dictionary where Key = Node, Value = List of Neighbors
# This is efficient: O(1) to find neighbors, O(V + E) space.
class Graph:
    def __init__(self):
        # The "Adjacency List"
        # Example: { 'A': ['B', 'C'], 'B': ['A'] }
        self.graph = {}

    def add_edge(self, u, v, directed=False):
        """
        Adds an edge between node u and node v.
        If the graph is undirected, we add the link both ways.
        """
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        
        if not directed:
            self.graph[v].append(u)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    # 2. THE ALGORITHM: Breadth-First Search (BFS)
    # Uses a Queue (FIFO). Finds the shortest path in unweighted graphs.
    def bfs_shortest_path(self, start, goal):
        if start not in self.graph or goal not in self.graph:
            return None
        
        # Queue stores tuples: (current_node, path_taken_to_get_here)
        queue = deque([(start, [start])])
        
        # Visited set prevents infinite loops in cyclic graphs
        visited = set([start])

        while queue:
            # Dequeue the first element (FIFO)
            current_node, path = queue.popleft()

            # Check if we reached the target
            if current_node == goal:
                return path

            # Explore neighbors
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Create new path: current path + this neighbor
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
        
        return None # Path not found

# 3. EXECUTION
if __name__ == "__main__":
    # Build a Social Network Graph
    # A -- B -- E
    # |    |    |
    # C -- D -- F
    social_network = Graph()
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'D'),
        ('D', 'F'),
        ('E', 'F')
    ]
    
    print("--- Building Graph ---")
    for u, v in edges:
        social_network.add_edge(u, v)
    
    social_network.print_graph()

    # Find shortest path (degrees of separation)
    start_node = 'A'
    target_node = 'F'
    print(f"\n--- Finding Shortest Path from {start_node} to {target_node} ---")
    
    path = social_network.bfs_shortest_path(start_node, target_node)
    
    if path:
        print(f"Shortest Path Found: {path}")
        print(f"Degrees of Separation: {len(path) - 1}")
    else:
        print("No path found.")