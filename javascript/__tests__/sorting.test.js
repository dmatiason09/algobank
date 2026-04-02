const {
  bubbleSort,
  selectionSort,
  insertionSort,
  mergeSort,
  quickSort,
  heapSort,
  countingSort,
  radixSort,
} = require('../sorting');

// all comparison-based sorts should pass the same tests
const comparisonSorts = [
  ['bubbleSort', bubbleSort],
  ['selectionSort', selectionSort],
  ['insertionSort', insertionSort],
  ['mergeSort', mergeSort],
  ['quickSort', quickSort],
  ['heapSort', heapSort],
];

// only work with non-negative ints
const integerSorts = [
  ['countingSort', countingSort],
  ['radixSort', radixSort],
];

describe.each(comparisonSorts)('%s', (name, sortFn) => {
  test('sorts a basic unsorted array', () => {
    expect(sortFn([64, 34, 25, 12, 22, 11, 90])).toEqual([11, 12, 22, 25, 34, 64, 90]);
  });

  test('handles empty array', () => {
    expect(sortFn([])).toEqual([]);
  });

  test('handles single element', () => {
    expect(sortFn([1])).toEqual([1]);
  });

  test('handles already sorted input', () => {
    expect(sortFn([1, 2, 3, 4, 5])).toEqual([1, 2, 3, 4, 5]);
  });

  test('handles reverse sorted input', () => {
    expect(sortFn([5, 4, 3, 2, 1])).toEqual([1, 2, 3, 4, 5]);
  });

  test('handles duplicates', () => {
    expect(sortFn([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])).toEqual([1, 1, 2, 3, 3, 4, 5, 5, 6, 9]);
  });

  test('handles negative numbers', () => {
    expect(sortFn([3, -2, -8, 5, 0, -1])).toEqual([-8, -2, -1, 0, 3, 5]);
  });

  test('handles all same values', () => {
    expect(sortFn([7, 7, 7, 7])).toEqual([7, 7, 7, 7]);
  });

  test('handles two elements', () => {
    expect(sortFn([2, 1])).toEqual([1, 2]);
  });
});

describe.each(integerSorts)('%s', (name, sortFn) => {
  test('sorts basic array', () => {
    expect(sortFn([64, 34, 25, 12, 22, 11, 90])).toEqual([11, 12, 22, 25, 34, 64, 90]);
  });

  test('handles empty array', () => {
    expect(sortFn([])).toEqual([]);
  });

  test('handles single element', () => {
    expect(sortFn([5])).toEqual([5]);
  });

  test('handles zeros', () => {
    expect(sortFn([0, 5, 0, 3, 0, 1])).toEqual([0, 0, 0, 1, 3, 5]);
  });

  test('handles already sorted', () => {
    expect(sortFn([1, 2, 3, 4, 5])).toEqual([1, 2, 3, 4, 5]);
  });

  test('handles duplicates', () => {
    expect(sortFn([4, 2, 2, 8, 3, 3, 1])).toEqual([1, 2, 2, 3, 3, 4, 8]);
  });

  test('handles larger numbers', () => {
    expect(sortFn([170, 45, 75, 90, 802, 24, 2, 66])).toEqual([2, 24, 45, 66, 75, 90, 170, 802]);
  });
});
