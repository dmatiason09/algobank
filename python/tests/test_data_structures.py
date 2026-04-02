import pytest
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.linked_list import LinkedList
from data_structures.hash_map import HashMap


class TestStack:
    def test_push_and_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2

    def test_peek(self):
        s = Stack()
        s.push("hello")
        assert s.peek() == "hello"
        assert s.size() == 1  # peek shouldn't remove

    def test_is_empty(self):
        s = Stack()
        assert s.is_empty() is True
        s.push(1)
        assert s.is_empty() is False

    def test_pop_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.peek()

    def test_lifo_order(self):
        s = Stack()
        for i in range(5):
            s.push(i)
        result = [s.pop() for _ in range(5)]
        assert result == [4, 3, 2, 1, 0]


class TestQueue:
    def test_enqueue_and_dequeue(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        q.enqueue("c")
        assert q.dequeue() == "a"
        assert q.dequeue() == "b"

    def test_peek(self):
        q = Queue()
        q.enqueue(10)
        assert q.peek() == 10
        assert q.size() == 1

    def test_is_empty(self):
        q = Queue()
        assert q.is_empty() is True
        q.enqueue(1)
        assert q.is_empty() is False

    def test_dequeue_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_fifo_order(self):
        q = Queue()
        for i in range(5):
            q.enqueue(i)
        result = [q.dequeue() for _ in range(5)]
        assert result == [0, 1, 2, 3, 4]

    def test_mixed_operations(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        q.enqueue(3)
        assert q.dequeue() == 2
        assert q.dequeue() == 3


class TestLinkedList:
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]

    def test_insert_at_head(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(3)
        ll.insert_at_head(1)
        assert ll.to_list() == [1, 2, 3]

    def test_delete_head(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert ll.delete(1) is True
        assert ll.to_list() == [2]

    def test_delete_middle(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.delete(2) is True
        assert ll.to_list() == [1, 3]

    def test_delete_tail(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.delete(3) is True
        assert ll.to_list() == [1, 2]

    def test_delete_not_found(self):
        ll = LinkedList()
        ll.append(1)
        assert ll.delete(99) is False

    def test_delete_from_empty(self):
        ll = LinkedList()
        assert ll.delete(1) is False

    def test_search(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        assert ll.search(20) == 1
        assert ll.search(99) == -1

    def test_reverse(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.reverse()
        assert ll.to_list() == [3, 2, 1]

    def test_reverse_empty(self):
        ll = LinkedList()
        ll.reverse()
        assert ll.to_list() == []

    def test_len(self):
        ll = LinkedList()
        assert len(ll) == 0
        ll.append(1)
        ll.append(2)
        assert len(ll) == 2


class TestHashMap:
    def test_put_and_get(self):
        hm = HashMap()
        hm.put("name", "Dennis")
        hm.put("age", 25)
        assert hm.get("name") == "Dennis"
        assert hm.get("age") == 25

    def test_update_existing_key(self):
        hm = HashMap()
        hm.put("x", 1)
        hm.put("x", 2)
        assert hm.get("x") == 2
        assert hm.size() == 1  # shouldn't duplicate

    def test_get_missing_key_raises(self):
        hm = HashMap()
        with pytest.raises(KeyError):
            hm.get("nope")

    def test_remove(self):
        hm = HashMap()
        hm.put("a", 1)
        hm.put("b", 2)
        val = hm.remove("a")
        assert val == 1
        assert hm.contains("a") is False
        assert hm.size() == 1

    def test_remove_missing_raises(self):
        hm = HashMap()
        with pytest.raises(KeyError):
            hm.remove("nope")

    def test_contains(self):
        hm = HashMap()
        hm.put("key", "val")
        assert hm.contains("key") is True
        assert hm.contains("other") is False

    def test_keys_and_values(self):
        hm = HashMap()
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)
        assert sorted(hm.keys()) == ["a", "b", "c"]
        assert sorted(hm.values()) == [1, 2, 3]

    def test_handles_many_entries(self):
        """Make sure resizing works without losing data."""
        hm = HashMap(capacity=4)  # small initial capacity to force resizes
        for i in range(50):
            hm.put(f"key_{i}", i)

        assert hm.size() == 50
        for i in range(50):
            assert hm.get(f"key_{i}") == i

    def test_integer_keys(self):
        hm = HashMap()
        hm.put(1, "one")
        hm.put(2, "two")
        assert hm.get(1) == "one"
