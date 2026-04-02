# AlgoBank

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript&logoColor=white)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A collection of 50+ algorithm & data structure implementations in Python and JavaScript. Each one includes Big O analysis and unit tests.

I started this project to solidify my understanding of CS fundamentals and have a quick reference I can come back to. Most implementations prioritize readability over micro-optimizations — if you're looking for production-grade code, you'd probably use the language's standard library. This is for learning.

## Structure

```
python/
  sorting/                # sorting algorithms
  searching/              # searching algorithms
  data_structures/        # stacks, queues, linked lists, hash maps
  trees/                  # BST, AVL, heap, trie
  graphs/                 # graph traversals, Dijkstra, topological sort
  dynamic_programming/    # classic DP problems
  tests/                  # pytest tests
javascript/
  sorting/                # sorting algorithms
  searching/              # searching algorithms
  data_structures/        # stacks, queues, linked lists, hash maps
  trees/                  # BST, heap, trie
  graphs/                 # graph traversals, Dijkstra, topological sort
  dynamic_programming/    # classic DP problems
  __tests__/              # jest tests
```

## Algorithms

### Sorting

| Algorithm      | Python | JavaScript | Time (avg) | Time (worst) | Space |
|---------------|--------|------------|------------|-------------|-------|
| Bubble Sort   | ✅     | ✅         | O(n²)      | O(n²)       | O(1)  |
| Selection Sort| ✅     | ✅         | O(n²)      | O(n²)       | O(1)  |
| Insertion Sort| ✅     | ✅         | O(n²)      | O(n²)       | O(1)  |
| Merge Sort    | ✅     | ✅         | O(n log n) | O(n log n)  | O(n)  |
| Quick Sort    | ✅     | ✅         | O(n log n) | O(n²)       | O(log n) |
| Heap Sort     | ✅     | ✅         | O(n log n) | O(n log n)  | O(1)  |
| Counting Sort | ✅     | ✅         | O(n + k)   | O(n + k)    | O(k)  |
| Radix Sort    | ✅     | ✅         | O(nk)      | O(nk)       | O(n + k) |

### Searching

| Algorithm            | Python | JavaScript | Time (avg)      | Time (worst) | Space |
|---------------------|--------|------------|-----------------|-------------|-------|
| Linear Search       | ✅     | ✅         | O(n)            | O(n)        | O(1)  |
| Binary Search       | ✅     | ✅         | O(log n)        | O(log n)    | O(1)  |
| Binary Search (rec) | ✅     | ✅         | O(log n)        | O(log n)    | O(log n) |
| Jump Search         | ✅     | ✅         | O(√n)           | O(√n)       | O(1)  |
| Interpolation Search| ✅     | ✅         | O(log log n)    | O(n)        | O(1)  |

### Data Structures

| Structure    | Python | JavaScript | Notes |
|-------------|--------|------------|-------|
| Stack       | ✅     | ✅         | LIFO, push/pop/peek in O(1) |
| Queue       | ✅     | ✅         | FIFO, enqueue/dequeue in O(1) |
| Linked List | ✅     | ✅         | Singly linked, with reverse |
| Hash Map    | ✅     | ✅         | Separate chaining, auto-resize |

### Trees

| Structure  | Python | JavaScript | Notes |
|-----------|--------|------------|-------|
| BST       | ✅     | ✅         | Insert, delete, search, traversals |
| AVL Tree  | ✅     |            | Self-balancing BST with rotations |
| Min Heap  | ✅     | ✅         | Array-based binary heap |
| Trie      | ✅     | ✅         | Prefix tree with autocomplete |

### Graphs

| Algorithm        | Python | JavaScript | Time     | Notes |
|-----------------|--------|------------|----------|-------|
| BFS             | ✅     | ✅         | O(V + E) | Breadth-first traversal |
| DFS             | ✅     | ✅         | O(V + E) | Iterative + recursive (Python) |
| Dijkstra        | ✅     | ✅         | O((V+E) log V) | Shortest path, non-negative weights |
| Topological Sort| ✅     | ✅         | O(V + E) | Kahn's algorithm, cycle detection |

### Dynamic Programming

| Problem            | Python | JavaScript | Time       | Space |
|-------------------|--------|------------|------------|-------|
| Fibonacci         | ✅     | ✅         | O(n)       | O(1) bottom-up |
| 0/1 Knapsack      | ✅     | ✅         | O(n·W)     | O(W) optimized |
| LCS               | ✅     | ✅         | O(m·n)     | O(m·n) |
| LIS               | ✅     | ✅         | O(n log n) | O(n) |
| Coin Change       | ✅     | ✅         | O(amount·n)| O(amount) |
| Edit Distance     | ✅     | ✅         | O(m·n)     | O(m·n) |
| Max Subarray      | ✅     | ✅         | O(n)       | O(1) |
| Climbing Stairs   | ✅     | ✅         | O(n)       | O(1) |
| Unique Paths      | ✅     | ✅         | O(m·n)     | O(n) |

## Running Tests

**Python**
```bash
cd python
pytest tests/ -v
```

**JavaScript**
```bash
cd javascript
npm install
npm test
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
