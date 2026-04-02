"""
Binary Search
-------------
Time:  O(log n)
Space: O(1) iterative, O(log n) recursive

Requires sorted input. Halves the search space each step.
I included both versions since interviews sometimes ask for one or the other.
"""


def binary_search(arr, target):
    """Iterative version — generally preferred to avoid stack overhead."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # avoids overflow in other languages

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
