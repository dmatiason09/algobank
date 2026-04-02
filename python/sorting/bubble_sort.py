"""
Bubble Sort
-----------
Time:  O(n²) average and worst case
Space: O(1)

Simple but inefficient for large datasets. The early exit optimization
helps when the array is nearly sorted though.
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
