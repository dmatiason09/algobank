"""
Linear Search
--------------
Time:  O(n)
Space: O(1)

Just walks through the array one element at a time.
Not efficient but works on unsorted data, which is its main advantage
over binary search.
"""


def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
