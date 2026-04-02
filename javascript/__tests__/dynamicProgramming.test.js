const {
  fibNaive, fibMemo, fibBottomUp,
  knapsack,
  lcsLength, lcs,
  lisDp, lisBinarySearch,
  coinChange, coinChangeWays,
  editDistance,
  maxSubarray,
  climbStairs, climbStairsKSteps,
  uniquePaths, uniquePathsWithObstacles,
} = require('../dynamic_programming');

describe('Fibonacci', () => {
  const fns = [['fibNaive', fibNaive], ['fibMemo', fibMemo], ['fibBottomUp', fibBottomUp]];

  describe.each(fns)('%s', (name, fn) => {
    test('base cases', () => {
      expect(fn(0)).toBe(0);
      expect(fn(1)).toBe(1);
    });

    test('known values', () => {
      expect(fn(5)).toBe(5);
      expect(fn(10)).toBe(55);
    });
  });
});

describe('Knapsack', () => {
  test('basic case', () => {
    expect(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7)).toBe(9);
  });

  test('zero capacity', () => {
    expect(knapsack([1, 2], [10, 20], 0)).toBe(0);
  });

  test('empty items', () => {
    expect(knapsack([], [], 10)).toBe(0);
  });

  test('single item fits', () => {
    expect(knapsack([5], [10], 5)).toBe(10);
  });

  test('single item doesnt fit', () => {
    expect(knapsack([5], [10], 3)).toBe(0);
  });
});

describe('LCS', () => {
  test('basic', () => {
    expect(lcsLength('abcde', 'ace')).toBe(3);
    expect(lcs('abcde', 'ace')).toBe('ace');
  });

  test('no common', () => {
    expect(lcsLength('abc', 'xyz')).toBe(0);
    expect(lcs('abc', 'xyz')).toBe('');
  });

  test('identical strings', () => {
    expect(lcsLength('hello', 'hello')).toBe(5);
  });

  test('one empty', () => {
    expect(lcsLength('abc', '')).toBe(0);
  });
});

describe('LIS', () => {
  const fns = [['lisDp', lisDp], ['lisBinarySearch', lisBinarySearch]];

  describe.each(fns)('%s', (name, fn) => {
    test('basic', () => {
      expect(fn([10, 9, 2, 5, 3, 7, 101, 18])).toBe(4);
    });

    test('all increasing', () => {
      expect(fn([1, 2, 3, 4, 5])).toBe(5);
    });

    test('all decreasing', () => {
      expect(fn([5, 4, 3, 2, 1])).toBe(1);
    });

    test('empty', () => {
      expect(fn([])).toBe(0);
    });
  });
});

describe('Coin Change', () => {
  test('basic min coins', () => {
    expect(coinChange([1, 5, 10, 25], 30)).toBe(2);
  });

  test('impossible', () => {
    expect(coinChange([2], 3)).toBe(-1);
  });

  test('zero amount', () => {
    expect(coinChange([1, 2, 5], 0)).toBe(0);
  });

  test('count ways', () => {
    expect(coinChangeWays([1, 2, 5], 5)).toBe(4);
  });

  test('ways with single denomination', () => {
    expect(coinChangeWays([2], 6)).toBe(1);
  });
});

describe('Edit Distance', () => {
  test('basic', () => {
    expect(editDistance('kitten', 'sitting')).toBe(3);
  });

  test('same strings', () => {
    expect(editDistance('hello', 'hello')).toBe(0);
  });

  test('empty to something', () => {
    expect(editDistance('', 'abc')).toBe(3);
  });

  test('both empty', () => {
    expect(editDistance('', '')).toBe(0);
  });
});

describe('Max Subarray', () => {
  test('mixed values', () => {
    expect(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])).toBe(6);
  });

  test('all positive', () => {
    expect(maxSubarray([1, 2, 3, 4])).toBe(10);
  });

  test('all negative', () => {
    expect(maxSubarray([-3, -2, -5, -1])).toBe(-1);
  });

  test('empty', () => {
    expect(maxSubarray([])).toBe(0);
  });
});

describe('Climbing Stairs', () => {
  test('base cases', () => {
    expect(climbStairs(1)).toBe(1);
    expect(climbStairs(2)).toBe(2);
  });

  test('known values', () => {
    expect(climbStairs(5)).toBe(8);
  });

  test('k steps generalized', () => {
    expect(climbStairsKSteps(4, 3)).toBe(7);
  });

  test('k=2 matches regular', () => {
    for (let n = 1; n <= 8; n++) {
      expect(climbStairsKSteps(n, 2)).toBe(climbStairs(n));
    }
  });
});

describe('Unique Paths', () => {
  test('basic grid', () => {
    expect(uniquePaths(3, 7)).toBe(28);
  });

  test('single row', () => {
    expect(uniquePaths(1, 5)).toBe(1);
  });

  test('with obstacles', () => {
    const grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]];
    expect(uniquePathsWithObstacles(grid)).toBe(2);
  });

  test('blocked start', () => {
    expect(uniquePathsWithObstacles([[1, 0], [0, 0]])).toBe(0);
  });
});
