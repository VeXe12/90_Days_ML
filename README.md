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

---

## 🛠️ Tech Stack
*   **Language:** Python
*   **Tools:** VS Code, Git, LeetCode
*   **Libraries:** `sys`, `time`, `collections` (Standard Library focus for Week 1)

---

## 🔗 Connect
Documenting my journey on [LinkedIn](www.linkedin.com/in/sujal-shrivastava-355470250).
