# AlgoBank

A collection of algorithm & data structure implementations in Python and JavaScript. Each one includes Big O analysis and unit tests.

I started this project to solidify my understanding of CS fundamentals and have a quick reference I can come back to. Most implementations prioritize readability over micro-optimizations.

## Structure

```
python/
  sorting/          # sorting algorithms
  searching/        # searching algorithms
  data_structures/  # stacks, queues, linked lists, hash maps
  tests/            # pytest tests
javascript/
  sorting/          # sorting algorithms
  searching/        # searching algorithms
  data_structures/  # stacks, queues, linked lists, hash maps
  __tests__/        # jest tests
```

More categories (trees, graphs, dynamic programming) coming soon.

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

## License

MIT
