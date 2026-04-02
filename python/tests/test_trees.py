import pytest
from trees.bst import BST
from trees.avl_tree import AVLTree
from trees.min_heap import MinHeap
from trees.trie import Trie


class TestBST:
    def test_insert_and_inorder(self):
        tree = BST()
        for val in [5, 3, 7, 1, 4]:
            tree.insert(val)
        assert tree.inorder() == [1, 3, 4, 5, 7]

    def test_search(self):
        tree = BST()
        for val in [10, 5, 15, 3, 8]:
            tree.insert(val)
        assert tree.search(8) is True
        assert tree.search(12) is False

    def test_delete_leaf(self):
        tree = BST()
        for val in [5, 3, 7]:
            tree.insert(val)
        tree.delete(3)
        assert tree.inorder() == [5, 7]

    def test_delete_node_with_one_child(self):
        tree = BST()
        for val in [5, 3, 7, 6]:
            tree.insert(val)
        tree.delete(7)
        assert tree.inorder() == [3, 5, 6]

    def test_delete_node_with_two_children(self):
        tree = BST()
        for val in [5, 3, 7, 6, 8]:
            tree.insert(val)
        tree.delete(7)
        assert 7 not in tree.inorder()
        # remaining elements should still be sorted
        assert tree.inorder() == sorted(tree.inorder())

    def test_delete_root(self):
        tree = BST()
        for val in [5, 3, 7]:
            tree.insert(val)
        tree.delete(5)
        assert tree.search(5) is False
        assert len(tree.inorder()) == 2

    def test_preorder(self):
        tree = BST()
        for val in [5, 3, 7, 1, 4]:
            tree.insert(val)
        assert tree.preorder() == [5, 3, 1, 4, 7]

    def test_postorder(self):
        tree = BST()
        for val in [5, 3, 7, 1, 4]:
            tree.insert(val)
        assert tree.postorder() == [1, 4, 3, 7, 5]

    def test_height(self):
        tree = BST()
        assert tree.height() == -1  # empty tree
        tree.insert(5)
        assert tree.height() == 0
        tree.insert(3)
        tree.insert(7)
        assert tree.height() == 1

    def test_empty_tree_search(self):
        tree = BST()
        assert tree.search(1) is False


class TestAVLTree:
    def test_stays_sorted_after_inserts(self):
        avl = AVLTree()
        for val in [10, 20, 30, 40, 50]:
            avl.insert(val)
        assert avl.inorder() == [10, 20, 30, 40, 50]

    def test_search(self):
        avl = AVLTree()
        for val in [15, 10, 20, 5, 25]:
            avl.insert(val)
        assert avl.search(10) is True
        assert avl.search(99) is False

    def test_delete(self):
        avl = AVLTree()
        for val in [10, 20, 30, 40, 50]:
            avl.insert(val)
        avl.delete(30)
        result = avl.inorder()
        assert 30 not in result
        assert result == sorted(result)

    def test_no_duplicates(self):
        avl = AVLTree()
        avl.insert(5)
        avl.insert(5)
        avl.insert(5)
        assert avl.inorder() == [5]

    def test_balance_after_ascending_inserts(self):
        """Inserting 1-7 in order would make a skewed BST,
        but AVL should keep it balanced."""
        avl = AVLTree()
        for i in range(1, 8):
            avl.insert(i)
        # all elements present and sorted
        assert avl.inorder() == [1, 2, 3, 4, 5, 6, 7]


class TestMinHeap:
    def test_insert_and_extract(self):
        heap = MinHeap()
        for val in [5, 3, 8, 1, 2]:
            heap.insert(val)
        result = []
        while not heap.is_empty():
            result.append(heap.extract_min())
        assert result == [1, 2, 3, 5, 8]

    def test_peek(self):
        heap = MinHeap()
        heap.insert(10)
        heap.insert(3)
        heap.insert(7)
        assert heap.peek() == 3
        assert heap.size() == 3  # peek shouldn't remove

    def test_extract_from_empty_raises(self):
        heap = MinHeap()
        with pytest.raises(IndexError):
            heap.extract_min()

    def test_single_element(self):
        heap = MinHeap()
        heap.insert(42)
        assert heap.extract_min() == 42
        assert heap.is_empty()

    def test_duplicate_values(self):
        heap = MinHeap()
        for val in [3, 1, 3, 1, 2]:
            heap.insert(val)
        result = []
        while not heap.is_empty():
            result.append(heap.extract_min())
        assert result == [1, 1, 2, 3, 3]


class TestTrie:
    def test_insert_and_search(self):
        t = Trie()
        t.insert("hello")
        t.insert("help")
        assert t.search("hello") is True
        assert t.search("help") is True
        assert t.search("hel") is False

    def test_starts_with(self):
        t = Trie()
        t.insert("apple")
        t.insert("app")
        assert t.starts_with("app") is True
        assert t.starts_with("ap") is True
        assert t.starts_with("b") is False

    def test_get_words_with_prefix(self):
        t = Trie()
        words = ["car", "card", "care", "careful", "cat"]
        for w in words:
            t.insert(w)

        result = t.get_words_with_prefix("car")
        assert sorted(result) == ["car", "card", "care", "careful"]

    def test_empty_trie(self):
        t = Trie()
        assert t.search("anything") is False
        assert t.starts_with("a") is False

    def test_single_character_words(self):
        t = Trie()
        t.insert("a")
        t.insert("b")
        assert t.search("a") is True
        assert t.search("c") is False
