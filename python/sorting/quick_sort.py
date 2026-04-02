"""
Quick Sort
----------
Time:  O(n log n) average, O(n²) worst (rare with good pivot)
Space: O(log n) due to recursion stack

Fast in practice. Worst case happens when the pivot is always the
smallest or largest element — using median-of-three or random pivot
helps avoid this but I kept it simple here with last element as pivot.
"""


def quick_sort(arr):
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr, low, high):
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pivot_idx - 1)
        _quick_sort_helper(arr, pivot_idx + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
