"""
Queue (FIFO)
------------
Enqueue: O(1)
Dequeue: O(1)
Peek:    O(1)

Using deque internally because popping from the front of a regular
list is O(n) — it has to shift everything. deque is doubly linked
so both ends are O(1).
"""

from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"
