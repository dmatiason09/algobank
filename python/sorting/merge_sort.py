"""
Merge Sort
----------
Time:  O(n log n) always
Space: O(n)

Consistent performance regardless of input. The trade-off is the extra
memory needed for the temporary arrays during merging.
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # use <= for stability (equal elements keep original order)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # one of them will be empty at this point
    result.extend(left[i:])
    result.extend(right[j:])
    return result
