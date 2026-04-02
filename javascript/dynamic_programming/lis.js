/**
 * Longest Increasing Subsequence
 *
 * DP:            O(n²)
 * Binary search: O(n log n)
 */

function lisDp(arr) {
  if (arr.length === 0) return 0;

  const dp = new Array(arr.length).fill(1);

  for (let i = 1; i < arr.length; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[j] < arr[i]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp);
}

function lisBinarySearch(arr) {
  if (arr.length === 0) return 0;

  const tails = [];

  for (const num of arr) {
    let lo = 0, hi = tails.length;
    while (lo < hi) {
      const mid = Math.floor((lo + hi) / 2);
      if (tails[mid] < num) lo = mid + 1;
      else hi = mid;
    }

    if (lo === tails.length) {
      tails.push(num);
    } else {
      tails[lo] = num;
    }
  }

  return tails.length;
}

module.exports = { lisDp, lisBinarySearch };
