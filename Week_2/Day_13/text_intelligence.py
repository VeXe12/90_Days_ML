import collections

# ==========================================
# PART 1: 2D Dynamic Programming (Edit Distance)
# ==========================================
# Time Complexity: O(M * N)
# Space Complexity: O(M * N) (Can be optimized to O(min(M,N))
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    
    # 1. Create a 2D DP table (m+1 x n+1)
    # dp[i][j] = min edits to convert s1[:i] to s2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 2. Base Cases (Initialization)
    # Converting empty string to s2[:j] requires j inserts
    for j in range(n + 1):
        dp[0][j] = j
    # Converting s1[:i] to empty string requires i deletes
    for i in range(m + 1):
        dp[i][0] = i
        
    # 3. Fill the Table (Bottom-Up)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                # Characters match: No new edit needed, carry over previous cost
                dp[i][j] = dp[i-1][j-1]
            else:
                # Characters mismatch: Take min of 3 operations + 1 cost
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Deletion (remove char from s1)
                    dp[i][j-1],    # Insertion (add char to s1)
                    dp[i-1][j-1]   # Replacement (swap char)
                )
    
    return dp[m][n]

# ==========================================
# PART 2: Trie (Prefix Tree) for Autocomplete
# ==========================================
class TrieNode:
    def __init__(self):
        self.children = {} # Map character -> TrieNode
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # O(L) - Insert word of length L
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    # O(L) - Standard Search
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # O(L + V) - Find all words starting with prefix
    # L = length of prefix, V = number of nodes in subtree
    def autocomplete(self, prefix):
        results = []
        node = self.root
        
        # Step 1: Navigate to the end of the prefix
        for char in prefix:
            if char not in node.children:
                return [] # Prefix not found
            node = node.children[char]
            
        # Step 2: DFS to find all complete words below this point
        self._dfs(node, prefix, results)
        return results
    
    def _dfs(self, node, path, results):
        if node.is_end_of_word:
            results.append(path)
        
        for char, child_node in node.children.items():
            self._dfs(child_node, path + char, results)

# ==========================================
# 3. EXECUTION & BENCHMARK
# ==========================================
if __name__ == "__main__":
    print("--- 1. Edit Distance (2D DP) ---")
    w1, w2 = "kitten", "sitting"
    dist = levenshtein_distance(w1, w2)
    print(f"Distance between '{w1}' and '{w2}': {dist}") 
    # Expected: 3 (k->s, e->i, add g)
    
    print("\n--- 2. Trie Autocomplete ---")
    ml_terms = ["neural", "neuron", "network", "natural", "language", "logic"]
    trie = Trie()
    for term in ml_terms:
        trie.insert(term)
        
    query = "neu"
    suggestions = trie.autocomplete(query)
    print(f"Typed '{query}' -> Suggestions: {suggestions}")
    
    print("\n--- 3. Spell Checker Simulation ---")
    # If exact search fails, use Edit Distance on a small candidate set
    typo = "nural"
    if not trie.search(typo):
        print(f"'{typo}' not found. Searching for suggestions...")
        # In a real app, you wouldn't scan the whole list, but for this lab we will
        candidates = [word for word in ml_terms if levenshtein_distance(typo, word) <= 2]
        print(f"Did you mean: {candidates}?")