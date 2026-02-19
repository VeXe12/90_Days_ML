# 90 Days of Machine Learning Engineering 🚀

**Goal:** Master the fundamentals of Machine Learning Engineering, starting from Python internals and Data Structures to Advanced Deep Learning.
**Status:** In Progress (Started Feb 1, 2025).

This repository documents my daily progress, code labs, and algorithmic challenges. I focus on "First Principles"—understanding *how* things work under the hood (Memory, Time Complexity, Math) before simply importing libraries.

---

## 📅 Progress Log

| Day | Topic | Key Concepts & Labs | Code |
| :--- | :--- | :--- | :--- |
| **01** | **Memory Management** | Analyzed `sys.getsizeof()` and `id()`. Proved why Python Lists consume more RAM than Tuples. Solved In-Place algorithms ($O(1)$ space). | [View Code](./Day-01) |
| **02** | **Time Complexity** | Benchmarked Loop ($O(n)$) vs. Math Formula ($O(1)$). Mastered Big O notation for scalability. | [View Code](./Day-02) |
| **03** | **Hash Maps (NLP)** | Implemented **Bag-of-Words** frequency counting. Compared loops vs. `collections.Counter`. | [View Code](./Day-03) |
| **04** | **Sliding Window** | Implemented **N-Gram Generator**. Benchmarked string concatenation ($O(n^2)$) vs. Sliding Window ($O(n)$). | [View Code](./Day-04) |
| **05** | **Recursion** | Visualized **Call Stack** limits. Benchmarked Binary Search ($O(\log n)$) vs. Linear Search ($O(n)$). | [View Code](./Day-05) |
| **06** | **Sorting & Timsort** | Implemented **Merge Sort**. Benchmarked Bubble Sort ($O(n^2)$) vs. Timsort ($O(n \log n)$). | [View Code](./Day-06) |
| **07** | **Heaps (Top K)** | Implemented **KNN** search using Heaps. Optimized "Top K" retrieval to $O(N \log K)$. | [View Code](./Day-07) |
| **08** | **Linked Lists** | Built a **Singly Linked List**. Used **Fast & Slow Pointers** for cycle detection and finding midpoints. | [View Code](./Day-08) |
| **09** | **Stacks & Queues** | Benchmarked `list.pop(0)` vs `deque.popleft()`. Simualted a Data Pipeline Buffer. | [View Code](./Day-09) |
| **10** | **Trees & BST** | Implemented a **Binary Search Tree** ($O(\log n)$ search). Built a **Gini Impurity** calculator for Decision Trees. | [View Code](./Day-10) |
| **11** | **Graphs & BFS** | Implemented **Adjacency List** graph representation. Used **BFS** (Queue) for shortest path finding in unweighted graphs. | [View Code](./Day-11) |
| **12** | **Dynamic Programming** | Benchmarked **Recursion** ($O(2^N)$) vs **Memoization** ($O(N)$). Solved 1D optimization problems. | [View Code](./Day-12) |
| **13** | **2D DP & Tries** | Built a **Spell Checker** (Levenshtein Distance) and **Autocomplete** engine (Trie). Mastered 2D Grid DP. | [View Code](./Day-13) |
| **14** | **Greedy Algorithms** | Implemented **Dijkstra's Algorithm** ($O(E \log V)$). Built a **Weighted Graph** routing engine. Solved Interval Scheduling. | [View Code](./Day-14) |
| **15** | **Backtracking** | Built a **Sudoku Solver**. Mastered the **Backtracking Template** (`choose` $\rightarrow$ `explore` $\rightarrow$ `un-choose`) and State Space Tree pruning. | [View Code](./Day-15) |
| **16** | **Range Queries** | Built a **Segment Tree** for mutable arrays. Optimized range sum queries from $O(N)$ to $O(\log N)$. Studied **Fenwick Trees**. | [View Code](./Day-16) |
| **17** | **Bit Manipulation** | Mastered bitwise operators (`&`, `\|`, `^`, `<<`). Implemented **Brian Kernighan’s Algorithm** and **XOR Swap**. | [View Code](./Day-17) |
| **18** | **Probability & Stats** | Simulated **Law of Large Numbers**. Implemented **Bayes' Theorem** calculator. Mastered nuances of False Positives. | [View Code](./Day-18) |
| **19** | **Naive Bayes & Distributions** | Built a **Text Classifier** from scratch using MLE and **Laplace Smoothing**. Solved statistical array problems. | [View Code](./Day-19) |

---

## 📂 Daily Breakdown

### **Day 1: Python Memory & Space Complexity**
*   **Theory:** Mutability vs. Immutability, Memory overhead of Lists vs. Tuples.
*   **Lab:** `memory_analysis.py` - Script to inspect object sizes in bytes.
*   **DSA:** Two Pointers technique (LeetCode #26 Remove Duplicates, #344 Reverse String).

### **Day 2: Time Complexity & Big O**
*   **Theory:** $O(1)$ vs $O(n)$ vs $O(n^2)$. Why nested loops crash production servers.
*   **Lab:** `complexity.py` - Timer script proving mathematical summation is instant compared to iteration.
*   **DSA:** Hash Maps for lookup speed (LeetCode #1 Two Sum, #217 Contains Duplicate).

### **Day 3: Hash Maps & Text Processing**
*   **Theory:** Hashing, Collisions, and Set Theory.
*   **Lab:** `text_analyzer.py` - Implementing a "Bag of Words" model from scratch for NLP preprocessing.
*   **DSA:** Frequency Maps & Sets (LeetCode #349 Intersection of Arrays, #387 First Unique Char).

### **Day 4: String Manipulation & Sliding Window**
*   **Theory:** String Immutability in Python. The **Sliding Window** pattern for efficient sequence processing.
*   **Lab:** `ngrams.py` - Generating Bi-grams and Tri-grams using a sliding window.
*   **DSA:** Sequence & Two Pointers (LeetCode #125 Valid Palindrome, #3 Longest Substring Without Repeating Characters).

### **Day 5: Recursion & The Call Stack**
*   **Theory:** Divide & Conquer. Stack Frames, recursion overhead, and why $O(\log n)$ is critical.
*   **Lab:** `recursion_lab.py` - Visualizing recursion depth limits and benchmarking Binary Search.
*   **DSA:** Binary Search & Recursion (LeetCode #704 Binary Search, #35 Search Insert Position, #50 Pow(x, n)).

### **Day 6: Sorting Algorithms & Timsort**
*   **Theory:** Brute Force ($O(N^2)$) vs Divide & Conquer ($O(N \log N)$). Understanding Python's **Timsort**.
*   **Lab:** `sorting_algo.py` - Implemented Merge Sort. Benchmarked Bubble Sort vs. Merge Sort vs. Timsort.
*   **DSA:** Sorting & Partitioning (LeetCode #88 Merge Sorted Array, #75 Sort Colors, #215 Kth Largest Element).

### **Day 7: Heaps & Priority Queues**
*   **Theory:** Efficiently finding the "Top K" elements in $O(N \log K)$ time.
*   **Lab:** `knn_simulation.py` - Simulating K-Nearest Neighbors (KNN) lookup using a Max-Heap.
*   **DSA:** Heap Applications (LeetCode #973 K Closest Points to Origin, #1046 Last Stone Weight).

### **Day 8: Linked Lists & Pointers**
*   **Theory:** Non-contiguous memory. Nodes and Pointers as the basis of Computational Graphs.
*   **Lab:** `linked_list.py` - Implementing a Linked List and the **Fast & Slow Pointer** technique.
*   **DSA:** Pointer Manipulation (LeetCode #141 Linked List Cycle, #876 Middle of Linked List, #206 Reverse Linked List).

### **Day 9: Stacks, Queues & Buffers**
*   **Theory:** LIFO vs FIFO. Why `list` is unsafe for Queues ($O(N)$ shifts).
*   **Lab:** `queue_buffer.py` - Proved `collections.deque` is $O(1)$ for pipeline buffering while `list` lags.
*   **DSA:** Stack Logic (LeetCode #20 Valid Parentheses, #232 Queue using Stacks, #155 Min Stack).

### **Day 10: Trees & Binary Search Trees (BST)**
*   **Theory:** Moving from Linear to Hierarchical structures. **BFS** (Queue) vs **DFS** (Stack/Recursion). The logic behind Decision Tree splits (**Gini Impurity**).
*   **Lab:** `tree_lab.py` - Implemented a BST from scratch for $O(\log n)$ search. Coded a Gini Impurity calculator to understand how ML models evaluate "splits."
*   **DSA:** Tree Traversal (LeetCode #104 Max Depth of Binary Tree, #98 Validate BST, #102 Level Order Traversal).

### **Day 11: Graphs & BFS**
*   **Theory:** Adjacency Matrices vs. Adjacency Lists. Graph Traversal (BFS/DFS) and "Degrees of Separation."
*   **Lab:** `graph_basics.py` - Implemented a Graph class using a Dictionary of Sets. Used BFS to find the shortest path between nodes in a social network.
*   **DSA:** Graph Traversal (LeetCode #997 Find the Town Judge, #200 Number of Islands, #1091 Shortest Path in Binary Matrix).

### **Day 12: Dynamic Programming (DP)**
*   **Theory:** The "Bellman Equation" of ML. Overlapping Subproblems and Optimal Substructure. Top-Down (Memoization) vs Bottom-Up (Tabulation).
*   **Lab:** `dp_vs_recursion.py` - Benchmarking Fibonacci. Proved caching reduces execution time from seconds ($O(2^N)$) to microseconds ($O(N)$). Implemented "House Robber" logic.
*   **DSA:** 1D Dynamic Programming (LeetCode #70 Climbing Stairs, #746 Min Cost Climbing Stairs, #198 House Robber).

### **Day 13: 2D Dynamic Programming & Tries**
*   **Theory:** 2D Grids in DP and String Alignment. **Tries** (Prefix Trees) for fast string lookups ($O(L)$).
*   **Lab:** `text_intelligence.py` - Built a **Levenshtein Distance** calculator (Spell Checker logic) and a **Trie** for Autocomplete.
*   **DSA:** String Algorithms (LeetCode #208 Implement Trie, #1143 Longest Common Subsequence, #72 Edit Distance).

### **Day 14: Greedy Algorithms & Weighted Graphs**
*   **Theory:** The Greedy Choice Property. Dijkstra's Algorithm (Priority Queue) vs. BFS.
*   **Lab:** `dijkstra_lab.py` - Built a GPS routing engine using Dijkstra's algorithm to find the shortest path in a weighted traffic network.
*   **DSA:** Weighted Graphs & Greedy (LeetCode #743 Network Delay Time, #787 Cheapest Flights Within K Stops, #435 Non-overlapping Intervals).

### **Day 15: Backtracking & Constraint Satisfaction**
*   **Theory:** State Space Trees and DFS. Constraint Satisfaction Problems (CSPs) in AI. The "Choose $\rightarrow$ Explore $\rightarrow$ Un-choose" template.
*   **Lab:** `sudoku_solver.py` - Implemented a backtracking algorithm to solve 9x9 Sudoku puzzles by pruning invalid branches.
*   **DSA:** Backtracking (LeetCode #46 Permutations, #78 Subsets, #51 N-Queens).

### **Day 16: Range Queries & Segment Trees**
*   **Theory:** Handling mutable data efficiently. **Segment Trees** allow range sum queries and element updates in $O(\log N)$ time, whereas Prefix Sums require $O(N)$ for updates. Studied **Fenwick Trees** (Binary Indexed Trees) which use bit manipulation to achieve similar performance with less memory.
*   **Lab:** `segment_tree.py` - Built a Segment Tree class from scratch. Implemented recursive `build`, `update`, and `query` methods to manage a dynamic sales dataset.
*   **DSA:** Range Queries (LeetCode #307 Range Sum Query - Mutable, #315 Count of Smaller Numbers After Self, #308 Range Sum Query 2D).

### **Day 17: Bit Manipulation**
*   **Theory:** Binary representation, Two's Complement, and Bitmasks. The "Magic" of XOR and using `n & (n-1)` to clear the lowest set bit.
*   **Lab:** `bit_utils.py` - Implemented a `BitManipulator` class with methods for parity checks, bit toggling, and isolating the lowest set bit (core logic of Fenwick Trees).
*   **DSA:** Bitwise Logic (LeetCode #136 Single Number, #191 Number of 1 Bits, #338 Counting Bits).

### **Day 18: Probability & Statistics (The Engine of ML)**
*   **Theory:** Random Variables, Distributions (Normal, Binomial), and the **Law of Large Numbers**. The math behind **Naive Bayes** and updating beliefs with evidence.
*   **Lab:** `probability_basics.py` - Simulated convergence of random events ($N=100k$) and built a **Bayes' Theorem Calculator** to solve medical diagnostic problems (False Positives).
*   **DSA:** Number Theory & Math (LeetCode #258 Add Digits, #202 Happy Number, #172 Factorial Trailing Zeroes).

### **Day 19: The Naive Bayes Classifier & Distributions**
*   **Theory:** The "Naive" conditional independence assumption, Maximum Likelihood Estimation (MLE), and Probability Distributions (Gaussian). Understood **Laplace Smoothing** and Log-Likelihoods to prevent numerical underflow.
*   **Lab:** `naive_bayes_scratch.py` - Built a text classifier from scratch without ML libraries to categorize headlines (Sports vs. Politics).
*   **DSA:** Statistics & Products (LeetCode #169 Majority Element, #238 Product of Array Except Self, #628 Maximum Product of Three Numbers).

---

## 🛠️ Tech Stack
*   **Language:** Python 3.13.2
*   **Tools:** VS Code, Git, LeetCode
*   **Libraries:** `sys`, `time`, `collections`, `heapq`, `math`, `random`

---

## 🔗 Connect
Documenting my journey on [LinkedIn](www.linkedin.com/in/sujal-shrivastava-355470250).
