"""
Interpolation Search
--------------------
Time:  O(log log n) average for uniformly distributed data, O(n) worst
Space: O(1)

Like binary search but instead of always going to the middle, it estimates
where the target might be based on value distribution. Works best when
elements are uniformly spread out.
"""


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # estimate position based on linear interpolation
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if pos < low or pos > high:
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1
