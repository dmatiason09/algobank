"""
Maximum Subarray (Kadane's Algorithm)
--------------------------------------
Time:  O(n)
Space: O(1)

Finds the contiguous subarray with the largest sum.
Kadane's is technically greedy but it's always grouped with DP problems
in interviews so I'm putting it here.
"""


def max_subarray(arr):
    """Returns the maximum subarray sum."""
    if not arr:
        return 0

    max_sum = arr[0]
    current = arr[0]

    for i in range(1, len(arr)):
        # either extend the current subarray or start fresh
        current = max(arr[i], current + arr[i])
        max_sum = max(max_sum, current)

    return max_sum


def max_subarray_with_indices(arr):
    """Also returns the start and end indices of the subarray."""
    if not arr:
        return 0, -1, -1

    max_sum = arr[0]
    current = arr[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current + arr[i]:
            current = arr[i]
            temp_start = i
        else:
            current += arr[i]

        if current > max_sum:
            max_sum = current
            start = temp_start
            end = i

    return max_sum, start, end
