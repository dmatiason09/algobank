"""
Unique Paths
-------------
Time:  O(m * n)
Space: O(n) with optimization

Count the number of unique paths from top-left to bottom-right
in an m x n grid, moving only right or down.

There's also a math solution using combinations: C(m+n-2, m-1)
but the DP version generalizes better to grids with obstacles.
"""


def unique_paths(m, n):
    """Basic version — no obstacles."""
    dp = [1] * n

    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[n - 1]


def unique_paths_with_obstacles(grid):
    """
    Same idea but some cells are blocked (1 = obstacle, 0 = free).
    Returns 0 if no path exists.
    """
    if not grid or grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]

    return dp[n - 1]
