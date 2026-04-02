"""
Heap Sort
---------
Time:  O(n log n) always
Space: O(1) — in-place unlike merge sort

Builds a max heap and then extracts elements one by one.
Good worst-case guarantee and doesn't need extra memory,
but in practice quicksort tends to be faster due to cache behavior.
"""


def heap_sort(arr):
    n = len(arr)

    # build max heap (start from last non-leaf node)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)

    return arr


def _heapify(arr, heap_size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _heapify(arr, heap_size, largest)
