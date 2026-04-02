"""
Trie (Prefix Tree)
------------------
Insert:  O(m) where m is word length
Search:  O(m)
Prefix:  O(m)

Great for autocomplete, spell checking, prefix-based lookups.
Each node holds a dict of children keyed by character.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        """Returns True if the exact word exists."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """Returns True if any word starts with this prefix."""
        return self._find_node(prefix) is not None

    def get_words_with_prefix(self, prefix):
        """Returns all words that start with the given prefix."""
        node = self._find_node(prefix)
        if not node:
            return []

        results = []
        self._collect_words(node, prefix, results)
        return results

    def _find_node(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def _collect_words(self, node, current, results):
        if node.is_end:
            results.append(current)
        for ch, child in node.children.items():
            self._collect_words(child, current + ch, results)
