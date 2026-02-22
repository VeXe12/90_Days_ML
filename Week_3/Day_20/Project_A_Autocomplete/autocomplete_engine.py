import collections

class TrieNode:
    """A single node in the Prefix Tree."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class AutocompleteEngine:
    def __init__(self):
        # 1. The Data Structure (Phase 1)
        self.root = TrieNode()
        
        # 2. The Math Engine (Phase 2)
        # unigram_counts stores how many times a single word appears: {"machine": 3}
        self.unigram_counts = collections.defaultdict(int)
        # bigram_counts stores how many times word B follows word A: {"machine": {"learning": 2, "code": 1}}
        self.bigram_counts = collections.defaultdict(lambda: collections.defaultdict(int))
        # bigram_probs stores the final MLE probabilities: P(B|A)
        self.bigram_probs = collections.defaultdict(lambda: collections.defaultdict(float))

    # ==========================================
    # PART 1: TRAINING THE MARKOV CHAIN
    # ==========================================
    def train(self, corpus):
        """Trains the engine by building the Trie and calculating Bigram probabilities."""
        # Simple tokenization (convert to lowercase, split by space)
        words = corpus.lower().replace('.', '').split()
        
        # 1. Build the Trie for fast prefix lookups
        for word in set(words):
            self._insert_into_trie(word)
            
        # 2. Count Frequencies (Maximum Likelihood Estimation)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            self.unigram_counts[w1] += 1
            self.bigram_counts[w1][w2] += 1
            
        # 3. Calculate Transition Probabilities: P(w2 | w1) = Count(w1, w2) / Count(w1)
        for w1, following_words in self.bigram_counts.items():
            for w2, count in following_words.items():
                self.bigram_probs[w1][w2] = count / self.unigram_counts[w1]
                
        print(f"Engine Trained! Vocabulary size: {len(self.unigram_counts)} words.")

    # ==========================================
    # PART 2: TRIE OPERATIONS (SPEED)
    # ==========================================
    def _insert_into_trie(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def _find_words_with_prefix(self, prefix):
        """Returns all words in the Trie that start with 'prefix'."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return [] # Prefix not found
            node = node.children[char]
            
        # Do a Depth First Search (DFS) from this node to find all valid endings
        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, path, results):
        if node.is_end_of_word:
            results.append(path)
        for char, next_node in node.children.items():
            self._dfs(next_node, path + char, results)

    # ==========================================
    # PART 3: THE AUTOCOMPLETE LOGIC (INTELLIGENCE)
    # ==========================================
    def suggest(self, context_word, partial_word):
        """
        Suggests completions for 'partial_word' based on the preceding 'context_word'.
        """
        # Step 1: Get all mathematically possible words from the Trie
        candidates = self._find_words_with_prefix(partial_word)
        
        # Step 2: Rank them using our Markov Chain probabilities
        ranked_suggestions = []
        for cand in candidates:
            # Look up P(candidate | context_word). Defaults to 0.0 if never seen together.
            prob = self.bigram_probs[context_word].get(cand, 0.0)
            
            # (In a real system, if prob is 0, we'd fallback to the unigram probability of the candidate)
            ranked_suggestions.append((cand, prob))
            
        # Step 3: Sort by highest probability first
        ranked_suggestions.sort(key=lambda x: x[1], reverse=True)
        return ranked_suggestions


# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    # A small corpus mimicking technical writing
    corpus = """
    machine learning is a subfield of artificial intelligence. 
    machine code is understood by computers. 
    machine learning engineers build models. 
    artificial intelligence is transforming software engineering.
    software engineers write code.
    machine learning algorithms require data.
    """
    
    engine = AutocompleteEngine()
    engine.train(corpus)
    
    print("\n--- Testing Autocomplete ---")
    
    context = "machine"
    prefix = "l"
    print(f"\nUser typed: '{context} {prefix}...'")
    suggestions = engine.suggest(context, prefix)
    
    for word, prob in suggestions:
        print(f" -> Suggestion: {word:<15} | Probability: {prob:.2%}")
        
    context = "software"
    prefix = "e"
    print(f"\nUser typed: '{context} {prefix}...'")
    suggestions = engine.suggest(context, prefix)
    
    for word, prob in suggestions:
        print(f" -> Suggestion: {word:<15} | Probability: {prob:.2%}")