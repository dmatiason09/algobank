"""
0/1 Knapsack
-------------
Time:  O(n * W) where n = items, W = capacity
Space: O(n * W) for the table, O(W) for the optimized version

Given items with weights and values, find the max value that fits
in a knapsack of capacity W. Each item can only be taken once.

Classic DP problem — shows up in interviews constantly.
"""


def knapsack(weights, values, capacity):
    """
    Returns the maximum value achievable.

    Uses a 2D table where dp[i][w] = best value using items 0..i-1
    with capacity w.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # don't take item i
            dp[i][w] = dp[i - 1][w]

            # take item i (if it fits)
            if weights[i - 1] <= w:
                with_item = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], with_item)

    return dp[n][capacity]


def knapsack_optimized(weights, values, capacity):
    """Space-optimized version using a single 1D array."""
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # iterate backwards to avoid using an item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
