"""
Min Heap (Binary Heap)
----------------------
Insert:      O(log n)
Extract min: O(log n)
Peek min:    O(1)

Array-based implementation. Parent of index i is at (i-1)//2,
children are at 2i+1 and 2i+2.

Python has heapq in the standard library but building it from
scratch helps understand how priority queues actually work.
"""


class MinHeap:
    def __init__(self):
        self._data = []

    def insert(self, val):
        self._data.append(val)
        self._bubble_up(len(self._data) - 1)

    def extract_min(self):
        if not self._data:
            raise IndexError("extract from empty heap")

        min_val = self._data[0]
        last = self._data.pop()

        if self._data:
            self._data[0] = last
            self._bubble_down(0)

        return min_val

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def size(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._data[idx] < self._data[parent]:
                self._data[idx], self._data[parent] = self._data[parent], self._data[idx]
                idx = parent
            else:
                break

    def _bubble_down(self, idx):
        n = len(self._data)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest != idx:
                self._data[idx], self._data[smallest] = self._data[smallest], self._data[idx]
                idx = smallest
            else:
                break

    def to_list(self):
        return list(self._data)
