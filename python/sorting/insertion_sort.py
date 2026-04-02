"""
Insertion Sort
--------------
Time:  O(n²) worst, O(n) best (already sorted)
Space: O(1)

Really good for small arrays or nearly sorted data. Python's Timsort
actually uses insertion sort for small runs internally.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
