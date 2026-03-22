# Heap Data Structures — Implementation, Analysis, and Applications

## 📌 Overview

This project explores **heap data structures** through implementation and analysis. It includes:

* Implementation of the **Heapsort algorithm**
* Implementation of a **Priority Queue using a binary max-heap**
* A performance comparison between **Heapsort, Quicksort, and Merge Sort**

The goal of this project is to understand both the theoretical behavior and practical performance of heap-based algorithms.

---

## 📂 Project Structure

```
assignment4_part1.py   # Heapsort + sorting comparison
assignment4_part2.py   # Priority Queue implementation
Assignment_4_Report_MSCS-532-B01.pdf           # Detailed report (analysis and discussion)
README.md             # Project documentation
```

---

## ⚙️ Requirements

* Python 3.x
* No external libraries required (uses only built-in modules)

---

## ▶️ How to Run

### 🔹 Part 1 — Sorting Algorithms Comparison

This script implements and compares Heapsort, Quicksort, and Merge Sort.

Run:

```
python assignment4_part1.py
```

What it does:

* Generates random arrays of different sizes
* Sorts them using three algorithms
* Measures execution time
* Displays performance results

---

### 🔹 Part 2 — Priority Queue (Task Scheduler)

This script implements a heap-based priority queue.

Run:

```
python assignment4_part2.py
```

What it does:

* Creates tasks with different priorities
* Inserts them into a max-heap
* Displays the queue
* Processes tasks from highest to lowest priority

---

## 🧠 Code Overview

### 🔹 Heapsort (Part 1)

Heapsort is implemented using a **binary max-heap**.

* The algorithm first builds a heap from the input array
* Then repeatedly extracts the largest element and places it at the end

Key functions:

* `heapify()` → maintains the heap property
* `heapsort()` → builds the heap and sorts the array

---

### 🔹 Quicksort

Quicksort uses a **divide-and-conquer approach**.

* Selects a pivot
* Splits the array into smaller parts
* Recursively sorts each part

It is very fast in practice due to efficient memory usage.

---

### 🔹 Merge Sort

Merge Sort also uses **divide-and-conquer**.

* Splits the array into halves
* Recursively sorts them
* Merges sorted subarrays

It is stable and guarantees consistent performance.

---

### 🔹 Performance Testing

The program includes a test function that:

* Generates random datasets
* Runs all three algorithms
* Measures execution time

This allows comparison between theoretical and practical performance.

---

### 🔹 Priority Queue (Part 2)

The priority queue is implemented using a **binary max-heap stored in a list**.

* The highest-priority task is always at the root
* Efficient insertion and removal are maintained

Key operations:

* `insert()` → adds a task (O(log n))
* `extract_max()` → removes highest priority (O(log n))
* `peek()` → returns highest priority (O(1))

---

## 📊 Summary of Findings

The experimental comparison showed that:

Quicksort was the fastest on the tested random arrays.
Merge Sort was slightly slower than Quicksort, but still performed well.
Heapsort was the slowest in practice, even though it has the same asymptotic complexity as the other two algorithms.

This shows that theoretical complexity alone does not fully determine practical performance. Factors such as:

memory access,
number of swaps,
recursion overhead,
and constant factors

can strongly affect runtime.

The priority queue implementation also showed that a heap is very effective for scheduling problems because it always keeps the highest-priority task easily accessible.

Key Takeaways

This project demonstrates that heap data structures are useful for both:

sorting
priority-based scheduling

Heapsort provides guaranteed O(n log n) performance and uses very little extra memory.
The priority queue shows how heaps can solve practical problems where urgent tasks must be processed first.

These ideas are widely used in:

operating systems,
network scheduling,
graph algorithms,
real-time systems,
and task management applications.
---

## 👤 Author

Fathiya Adan
MSCS-532: Algorithms and Data Structures

