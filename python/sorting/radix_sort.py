"""
Radix Sort
----------
Time:  O(nk) where k is the number of digits
Space: O(n + k)

Sorts by processing individual digits, least significant first.
Uses counting sort as a subroutine for each digit position.
Only handles non-negative integers here.
"""


def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        _counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def _counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # build output array (iterate backwards for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    for i in range(n):
        arr[i] = output[i]
