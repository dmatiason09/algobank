"""
Climbing Stairs
---------------
Time:  O(n)
Space: O(1)

You can climb 1 or 2 steps at a time. How many distinct ways
to reach the top of n stairs?

Turns out it's just Fibonacci in disguise. One of those problems
that seems tricky until you see the pattern.
"""


def climb_stairs(n):
    if n <= 2:
        return n

    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


def climb_stairs_k_steps(n, k):
    """
    Generalized version where you can take 1 to k steps at a time.
    Time: O(n * k), Space: O(n)
    """
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for step in range(1, min(k, i) + 1):
            dp[i] += dp[i - step]

    return dp[n]
