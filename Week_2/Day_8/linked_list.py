import time

# 1. THE ATOM: The Node Class
# In ML, this could be a neuron in a network or a state in a graph.
class Node:
    def __init__(self, value):
        self.value = value  # The data (feature, weight, etc.)
        self.next = None    # The pointer to the next node (reference)

# 2. THE STRUCTURE: The Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Adds a new node to the end of the list.
        Time Complexity: O(N) (We must traverse to the end)
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        """Helper to visualize the linked list as a Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    # --- THE ENGINEER'S ALGORITHM ---
    def find_middle(self):
        """
        Finds the middle node using the 'Fast & Slow Pointer' technique.
        This allows finding the midpoint in ONE pass (O(N)) without knowing the length.
        """
        slow = self.head
        fast = self.head

        # Loop continues as long as 'fast' has a valid next step
        while fast and fast.next:
            slow = slow.next      # Moves 1 step
            fast = fast.next.next # Moves 2 steps
        
        # When 'fast' reaches the end, 'slow' is exactly at the middle
        return slow.value if slow else None

# 3. THE EXECUTION
if __name__ == "__main__":
    # Create a list of 10,001 items
    ll = LinkedList()
    print("Building Linked List (this might take a moment due to O(N) append)...")
    
    # We use a smaller range for the lab to keep it quick
    count = 11
    for i in range(1, count + 1):
        ll.append(i)

    print(f"List Data: {ll.to_list()}")

    # Find Middle
    middle = ll.find_middle()
    print(f"Middle Node Value: {middle}")
    
    # Verification
    expected = (count // 2) + 1
    print(f"Verification: {'Success' if middle == expected else 'Fail'}")