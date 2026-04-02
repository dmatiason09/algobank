"""
Hash Map (with chaining)
------------------------
Insert:  O(1) average, O(n) worst
Lookup:  O(1) average, O(n) worst
Delete:  O(1) average, O(n) worst

Rolling my own hash map to understand how it works under the hood.
Uses separate chaining (linked lists per bucket) for collision handling.
Resizes when load factor exceeds 0.75.

Obviously in real Python code you'd just use a dict.
"""

INITIAL_CAPACITY = 16
LOAD_FACTOR_THRESHOLD = 0.75


class HashMap:
    def __init__(self, capacity=INITIAL_CAPACITY):
        self._capacity = capacity
        self._size = 0
        self._buckets = [[] for _ in range(capacity)]

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self._buckets[idx]

        # update if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

        if self._size / self._capacity > LOAD_FACTOR_THRESHOLD:
            self._resize()

    def get(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def remove(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return v

        raise KeyError(key)

    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def keys(self):
        all_keys = []
        for bucket in self._buckets:
            for k, v in bucket:
                all_keys.append(k)
        return all_keys

    def values(self):
        all_vals = []
        for bucket in self._buckets:
            for k, v in bucket:
                all_vals.append(v)
        return all_vals

    def size(self):
        return self._size

    def _hash(self, key):
        return hash(key) % self._capacity

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def __repr__(self):
        pairs = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{k!r}: {v!r}")
        return "HashMap({" + ", ".join(pairs) + "})"
