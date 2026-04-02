/**
 * Unique Paths
 * Time:  O(m * n)
 * Space: O(n)
 */

function uniquePaths(m, n) {
  const dp = new Array(n).fill(1);

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[j] += dp[j - 1];
    }
  }

  return dp[n - 1];
}

function uniquePathsWithObstacles(grid) {
  if (!grid.length || grid[0][0] === 1) return 0;

  const m = grid.length;
  const n = grid[0].length;
  const dp = new Array(n).fill(0);
  dp[0] = 1;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) {
        dp[j] = 0;
      } else if (j > 0) {
        dp[j] += dp[j - 1];
      }
    }
  }

  return dp[n - 1];
}

module.exports = { uniquePaths, uniquePathsWithObstacles };
