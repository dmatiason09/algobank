"""
Fibonacci
---------
Naive recursive: O(2^n) time, O(n) space
Memoized:        O(n) time, O(n) space
Bottom-up:       O(n) time, O(1) space

Three versions to show the progression from brute force to optimized.
The bottom-up approach with O(1) space is what you'd actually use.
"""


def fib_naive(n):
    """Don't use this for anything beyond n=30 or so."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_bottom_up(n):
    """Iterative with constant space — the way to go."""
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
