"""
Jump Search
-----------
Time:  O(√n)
Space: O(1)

Works on sorted arrays. Jumps ahead by √n steps then does a linear
scan backwards. Sits between linear and binary search in terms of
performance — useful when jumping back is cheap but binary search's
random access pattern isn't ideal (like linked lists... in theory).
"""

import math


def jump_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    step = int(math.sqrt(n))
    prev = 0

    # jump ahead until we pass the target or hit the end
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # linear scan in the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1
