# 90 Days of Machine Learning Engineering 🚀

**Goal:** Master the fundamentals of Machine Learning Engineering, starting from Python internals and Data Structures to Advanced Deep Learning.
**Status:** In Progress (Started Jan 31, 2025).

This repository documents my daily progress, code labs, and algorithmic challenges. I focus on "First Principles"—understanding *how* things work under the hood (Memory, Time Complexity, Math) before simply importing libraries.

---

## 📅 Progress Log

| Day | Topic | Key Concepts & Labs | Code |
| :--- | :--- | :--- | :--- |
| **01** | **Memory Management** | Analyzed `sys.getsizeof()` and `id()`. Proved why Python Lists consume more RAM than Tuples due to dynamic array over-allocation. Solved In-Place algorithms ($O(1)$ space). | [View Code](./Day-01) |
| **02** | **Time Complexity (Big O)** | Benchmarked Loop ($O(n)$) vs. Math Formula ($O(1)$) speed. Mastered Big O notation to predict scalability issues in large datasets. | [View Code](./Day-02) |
| **03** | **Hash Maps & Sets (NLP)** | Implemented **Bag-of-Words** frequency counting. Compared manual loops vs. `collections.Counter` ($O(n)$). Solved Intersection/Frequency problems using Hash Tables. | [View Code](./Day-03) |

---

## 📂 Daily Breakdown

### **Day 1: Python Memory & Space Complexity**
*   **Theory:** Mutability vs. Immutability, Memory overhead of Lists vs. Tuples.
*   **Lab:** `memory_analysis.py` - Script to inspect object sizes in bytes.
*   **DSA:** LeetCode #26, #344.

### **Day 2: Time Complexity & Big O**
*   **Theory:** $O(1)$ vs $O(n)$ vs $O(n^2)$. Why nested loops crash production servers.
*   **Lab:** `complexity.py` - Timer script proving mathematical summation is instant compared to iteration.
*   **DSA:** LeetCode #1, #217.

### **Day 3: Hash Maps & Text Processing**
*   **Theory:** Hashing, Collisions, and Set Theory.
*   **Lab:** `text_analyzer.py` - Implementing a "Bag of Words" model from scratch for NLP preprocessing.
*   **DSA:** LeetCode #349, #387.

---

## 🛠️ Tech Stack
*   **Language:** Python
*   **Tools:** VS Code, Git, LeetCode
*   **Libraries:** `sys`, `time`, `collections` (Standard Library focus for Week 1)

---

## 🔗 Connect
Documenting my journey on [LinkedIn](www.linkedin.com/in/sujal-shrivastava-355470250).
