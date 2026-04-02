"""
Longest Increasing Subsequence (LIS)
-------------------------------------
DP approach: O(n²) time, O(n) space
Binary search approach: O(n log n) time, O(n) space

Finds the length of the longest strictly increasing subsequence.
The O(n²) version is easier to understand, the O(n log n) version
is what you'd want for larger inputs.
"""

import bisect


def lis_dp(arr):
    """O(n²) DP approach — straightforward but slow for large arrays."""
    if not arr:
        return 0

    n = len(arr)
    dp = [1] * n  # every element is a subsequence of length 1

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_binary_search(arr):
    """
    O(n log n) using patience sorting idea.
    tails[i] holds the smallest tail value for an increasing
    subsequence of length i+1.
    """
    if not arr:
        return 0

    tails = []

    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)
