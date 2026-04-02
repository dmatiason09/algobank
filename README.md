# AlgoBank

A collection of algorithm & data structure implementations in Python and JavaScript. Each one includes Big O analysis and unit tests.

I started this project to solidify my understanding of CS fundamentals and have a quick reference I can come back to. Most implementations prioritize readability over micro-optimizations.

## Structure

```
python/
  sorting/       # sorting algorithms
  tests/         # pytest tests
javascript/
  sorting/       # sorting algorithms
  __tests__/     # jest tests
```

More categories (searching, trees, graphs, dynamic programming) coming soon.

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
