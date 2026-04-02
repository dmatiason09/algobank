const {
  linearSearch,
  binarySearch,
  binarySearchRecursive,
  jumpSearch,
  interpolationSearch,
} = require('../searching');

describe('linearSearch', () => {
  test('finds element in unsorted array', () => {
    expect(linearSearch([4, 2, 7, 1, 9], 7)).toBe(2);
  });

  test('returns first occurrence', () => {
    expect(linearSearch([1, 3, 3, 5], 3)).toBe(1);
  });

  test('returns -1 when not found', () => {
    expect(linearSearch([1, 2, 3], 10)).toBe(-1);
  });

  test('handles empty array', () => {
    expect(linearSearch([], 5)).toBe(-1);
  });

  test('works with strings', () => {
    expect(linearSearch(['a', 'b', 'c'], 'b')).toBe(1);
  });
});

// all of these need sorted input
const sortedSearchFns = [
  ['binarySearch', binarySearch],
  ['binarySearchRecursive', binarySearchRecursive],
  ['jumpSearch', jumpSearch],
  ['interpolationSearch', interpolationSearch],
];

describe.each(sortedSearchFns)('%s', (name, searchFn) => {
  const arr = [1, 3, 5, 7, 9, 11, 13];

  test('finds element in middle', () => {
    expect(searchFn(arr, 7)).toBe(3);
  });

  test('finds first element', () => {
    expect(searchFn([2, 4, 6, 8, 10], 2)).toBe(0);
  });

  test('finds last element', () => {
    expect(searchFn([2, 4, 6, 8, 10], 10)).toBe(4);
  });

  test('returns -1 when not found', () => {
    expect(searchFn(arr, 6)).toBe(-1);
  });

  test('handles empty array', () => {
    expect(searchFn([], 1)).toBe(-1);
  });

  test('handles single element found', () => {
    expect(searchFn([5], 5)).toBe(0);
  });

  test('handles single element not found', () => {
    expect(searchFn([5], 3)).toBe(-1);
  });

  test('works on larger array', () => {
    const big = Array.from({ length: 50 }, (_, i) => i * 2);
    expect(searchFn(big, 50)).toBe(25);
    expect(searchFn(big, 51)).toBe(-1);
  });
});
