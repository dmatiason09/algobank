/**
 * Fibonacci
 *
 * Naive:     O(2^n) time — don't use beyond small n
 * Memoized:  O(n) time, O(n) space
 * Bottom-up: O(n) time, O(1) space
 */

function fibNaive(n) {
  if (n <= 1) return n;
  return fibNaive(n - 1) + fibNaive(n - 2);
}

function fibMemo(n, memo = {}) {
  if (n <= 1) return n;
  if (n in memo) return memo[n];
  memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
  return memo[n];
}

function fibBottomUp(n) {
  if (n <= 1) return n;

  let prev = 0;
  let curr = 1;
  for (let i = 2; i <= n; i++) {
    [prev, curr] = [curr, prev + curr];
  }
  return curr;
}

module.exports = { fibNaive, fibMemo, fibBottomUp };
