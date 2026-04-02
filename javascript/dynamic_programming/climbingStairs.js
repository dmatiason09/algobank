/**
 * Climbing Stairs
 * Time:  O(n)
 * Space: O(1)
 *
 * It's just Fibonacci with different base cases.
 */

function climbStairs(n) {
  if (n <= 2) return n;

  let prev = 1;
  let curr = 2;
  for (let i = 3; i <= n; i++) {
    [prev, curr] = [curr, prev + curr];
  }
  return curr;
}

function climbStairsKSteps(n, k) {
  if (n === 0) return 1;

  const dp = new Array(n + 1).fill(0);
  dp[0] = 1;

  for (let i = 1; i <= n; i++) {
    for (let step = 1; step <= Math.min(k, i); step++) {
      dp[i] += dp[i - step];
    }
  }

  return dp[n];
}

module.exports = { climbStairs, climbStairsKSteps };
