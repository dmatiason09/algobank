"""
Singly Linked List
------------------
Access:    O(n)
Search:    O(n)
Insert at head: O(1)
Insert at tail: O(n) — could be O(1) with tail pointer but kept it simple
Delete:    O(n)

Classic linked list. Not really useful in Python day-to-day (lists are
arrays under the hood and way more practical) but it's a fundamental
data structure to understand.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, data):
        if not self.head:
            return False

        # special case: deleting head
        if self.head.data == data:
            self.head = self.head.next
            return True

        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return True
            curr = curr.next

        return False

    def search(self, data):
        """Returns the index of the first occurrence, or -1."""
        curr = self.head
        idx = 0
        while curr:
            if curr.data == data:
                return idx
            curr = curr.next
            idx += 1
        return -1

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def to_list(self):
        """Helper to convert to a regular list (mainly for testing)."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def __repr__(self):
        items = self.to_list()
        return " -> ".join(str(x) for x in items) + " -> None"
