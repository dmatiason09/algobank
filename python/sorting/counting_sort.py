"""
Counting Sort
-------------
Time:  O(n + k) where k is the range of input values
Space: O(k)

Non-comparison based sort. Works great when k isn't much larger than n.
Only works with non-negative integers (or you need to shift the values).
"""


def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    # rebuild the array from counts
    idx = 0
    for val, freq in enumerate(count):
        for _ in range(freq):
            arr[idx] = val
            idx += 1

    return arr
