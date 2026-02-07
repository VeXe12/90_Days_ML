# 90 Days of Machine Learning Engineering 🚀

**Goal:** Master the fundamentals of Machine Learning Engineering, starting from Python internals and Data Structures to Advanced Deep Learning.
**Status:** In Progress (Started Jan 31, 2025).

This repository documents my daily progress, code labs, and algorithmic challenges. I focus on "First Principles"—understanding *how* things work under the hood (Memory, Time Complexity, Math) before simply importing libraries.

---

## 📅 Progress Log

| Day | Date | Topic | Key Concepts & Labs | Code |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Jan 31 | **Memory Management** | Analyzed `sys.getsizeof()` and `id()`. Proved why Python Lists consume more RAM than Tuples due to dynamic array over-allocation. Solved In-Place algorithms ($O(1)$ space). | [View Code](./Day-01) |
| **02** | Feb 01 | **Time Complexity (Big O)** | Benchmarked Loop ($O(n)$) vs. Math Formula ($O(1)$) speed. Mastered Big O notation to predict scalability issues in large datasets. | [View Code](./Day-02) |
| **03** | Feb 02 | **Hash Maps & Sets (NLP)** | Implemented **Bag-of-Words** frequency counting. Compared manual loops vs. `collections.Counter` ($O(n)$). Solved Intersection/Frequency problems using Hash Tables. | [View Code](./Day-03) |
| **04** | Feb 03 | **Sliding Window & Strings** | Implemented **N-Gram Generator** for NLP. Benchmarked naive string concatenation ($O(n^2)$) vs. Sliding Window pattern ($O(n)$). Solved sequence processing problems. | [View Code](./Day-04) |
| **05** | Feb 04 | **Recursion & Divide/Conquer** | Visualized the **Call Stack** and Stack Overflow limits. Benchmarked Linear Search ($O(n)$) vs. Binary Search ($O(\log n)$) on 10M items. | [View Code](./Day-05) |
| **06** | Feb 05 | **Sorting & Timsort** | Implemented **Merge Sort** ($O(N \log N)$). Benchmarked against Bubble Sort ($O(N^2)$) and Python's **Timsort**. Solved Partitioning & Merging problems. | [View Code](./Day-06) |
| **07** | Feb 06 | **Heaps & Priority Queues** | Implemented **K-Nearest Neighbors (KNN)** search using Heaps. Optimized "Top K" retrieval from $O(N \log N)$ to $O(N \log K)$. | [View Code](./Day-07) |
| **08** | Feb 07 | **Linked Lists & Pointers** | Built a **Singly Linked List** from scratch. Mastered **Fast & Slow Pointers** for cycle detection and finding midpoints in one pass. | [View Code](./Day-08) |

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
*   **Theory:** String Immutability in Python and the $O(n^2)$ concatenation trap. The **Sliding Window** algorithmic pattern for efficient sequence processing.
*   **Lab:** `ngrams.py` - Generating Bi-grams and Tri-grams using a sliding window to prepare text for language models.
*   **DSA:** Sequence & Two Pointers (LeetCode #125 Valid Palindrome, #3 Longest Substring Without Repeating Characters).

### **Day 5: Recursion & The Call Stack**
*   **Theory:** The "Divide & Conquer" paradigm. Understanding Stack Frames, memory overhead of recursion, and why $O(\log n)$ is critical for massive datasets.
*   **Lab:** `recursion_lab.py` - Visualizing recursion depth limits and benchmarking Binary Search speed.
*   **DSA:** Binary Search & Recursion (LeetCode #704 Binary Search, #35 Search Insert Position, #50 Pow(x, n)).

### **Day 6: Sorting Algorithms & Timsort**
*   **Theory:** Why sorting allows for efficient data cleaning and median finding. The move from Brute Force ($O(N^2)$) to Divide & Conquer ($O(N \log N)$). Understanding **Timsort** (Python's default sort).
*   **Lab:** `sorting_algo.py` - Implemented Merge Sort from scratch. Benchmarked Bubble Sort ($O(N^2)$) vs. Merge Sort ($O(N \log N)$) vs. Timsort.
*   **DSA:** Sorting & Partitioning (LeetCode #88 Merge Sorted Array, #75 Sort Colors, #215 Kth Largest Element).

### **Day 7: Heaps & Priority Queues**
*   **Theory:** Breaking the bottleneck of sorting entire datasets. Using **Heaps** to find the "Top K" elements in $O(N \log K)$ time.
*   **Lab:** `knn_simulation.py` - Simulating K-Nearest Neighbors (KNN) lookup. Calculating Euclidean distance and efficiently retrieving neighbors using a Max-Heap.
*   **DSA:** Heap Applications (LeetCode #973 K Closest Points to Origin, #1046 Last Stone Weight).

### **Day 8: Linked Lists & Pointers**
*   **Theory:** Non-contiguous memory. How **Nodes** and **Pointers** form the basis of Computational Graphs (DAGs) in Deep Learning frameworks.
*   **Lab:** `linked_list.py` - Implementing a Linked List class. Using the **Fast & Slow Pointer** (Tortoise & Hare) technique to find the middle of a list in a single pass.
*   **DSA:** Pointer Manipulation (LeetCode #141 Linked List Cycle, #876 Middle of Linked List, #206 Reverse Linked List).

---

## 🛠️ Tech Stack
*   **Language:** Python 3.13
*   **Tools:** VS Code, Git, LeetCode
*   **Libraries:** `sys`, `time`, `collections`, `heapq`, `math` (Standard Library focus for Week 1)

---

## 🔗 Connect
Documenting my journey on [LinkedIn](www.linkedin.com/in/sujal-shrivastava-355470250).
