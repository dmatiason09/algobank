const { BST, MinHeap, Trie } = require('../trees');

describe('BST', () => {
  let tree;
  beforeEach(() => { tree = new BST(); });

  test('insert and inorder', () => {
    [5, 3, 7, 1, 4].forEach(v => tree.insert(v));
    expect(tree.inorder()).toEqual([1, 3, 4, 5, 7]);
  });

  test('search', () => {
    [10, 5, 15, 3, 8].forEach(v => tree.insert(v));
    expect(tree.search(8)).toBe(true);
    expect(tree.search(12)).toBe(false);
  });

  test('delete leaf', () => {
    [5, 3, 7].forEach(v => tree.insert(v));
    tree.delete(3);
    expect(tree.inorder()).toEqual([5, 7]);
  });

  test('delete node with one child', () => {
    [5, 3, 7, 6].forEach(v => tree.insert(v));
    tree.delete(7);
    expect(tree.inorder()).toEqual([3, 5, 6]);
  });

  test('delete node with two children', () => {
    [5, 3, 7, 6, 8].forEach(v => tree.insert(v));
    tree.delete(7);
    expect(tree.inorder()).not.toContain(7);
    const result = tree.inorder();
    expect(result).toEqual([...result].sort((a, b) => a - b));
  });

  test('delete root', () => {
    [5, 3, 7].forEach(v => tree.insert(v));
    tree.delete(5);
    expect(tree.search(5)).toBe(false);
    expect(tree.inorder().length).toBe(2);
  });

  test('preorder', () => {
    [5, 3, 7, 1, 4].forEach(v => tree.insert(v));
    expect(tree.preorder()).toEqual([5, 3, 1, 4, 7]);
  });

  test('height', () => {
    expect(tree.height()).toBe(-1);
    tree.insert(5);
    expect(tree.height()).toBe(0);
    tree.insert(3);
    tree.insert(7);
    expect(tree.height()).toBe(1);
  });

  test('empty tree search', () => {
    expect(tree.search(1)).toBe(false);
  });
});

describe('MinHeap', () => {
  let heap;
  beforeEach(() => { heap = new MinHeap(); });

  test('insert and extract in order', () => {
    [5, 3, 8, 1, 2].forEach(v => heap.insert(v));
    const result = [];
    while (!heap.isEmpty()) result.push(heap.extractMin());
    expect(result).toEqual([1, 2, 3, 5, 8]);
  });

  test('peek', () => {
    heap.insert(10);
    heap.insert(3);
    heap.insert(7);
    expect(heap.peek()).toBe(3);
    expect(heap.size()).toBe(3);
  });

  test('extract from empty throws', () => {
    expect(() => heap.extractMin()).toThrow();
  });

  test('single element', () => {
    heap.insert(42);
    expect(heap.extractMin()).toBe(42);
    expect(heap.isEmpty()).toBe(true);
  });

  test('duplicates', () => {
    [3, 1, 3, 1, 2].forEach(v => heap.insert(v));
    const result = [];
    while (!heap.isEmpty()) result.push(heap.extractMin());
    expect(result).toEqual([1, 1, 2, 3, 3]);
  });
});

describe('Trie', () => {
  let trie;
  beforeEach(() => { trie = new Trie(); });

  test('insert and search', () => {
    trie.insert('hello');
    trie.insert('help');
    expect(trie.search('hello')).toBe(true);
    expect(trie.search('help')).toBe(true);
    expect(trie.search('hel')).toBe(false);
  });

  test('startsWith', () => {
    trie.insert('apple');
    trie.insert('app');
    expect(trie.startsWith('app')).toBe(true);
    expect(trie.startsWith('ap')).toBe(true);
    expect(trie.startsWith('b')).toBe(false);
  });

  test('getWordsWithPrefix', () => {
    ['car', 'card', 'care', 'careful', 'cat'].forEach(w => trie.insert(w));
    const result = trie.getWordsWithPrefix('car');
    expect(result.sort()).toEqual(['car', 'card', 'care', 'careful']);
  });

  test('empty trie', () => {
    expect(trie.search('anything')).toBe(false);
    expect(trie.startsWith('a')).toBe(false);
  });

  test('single character words', () => {
    trie.insert('a');
    trie.insert('b');
    expect(trie.search('a')).toBe(true);
    expect(trie.search('c')).toBe(false);
  });
});
