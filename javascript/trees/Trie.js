/**
 * Trie (Prefix Tree)
 *
 * Insert/Search/StartsWith: O(m) where m = word length
 */

class TrieNode {
  constructor() {
    this.children = {};
    this.isEnd = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let node = this.root;
    for (const ch of word) {
      if (!node.children[ch]) {
        node.children[ch] = new TrieNode();
      }
      node = node.children[ch];
    }
    node.isEnd = true;
  }

  search(word) {
    const node = this._findNode(word);
    return node !== null && node.isEnd;
  }

  startsWith(prefix) {
    return this._findNode(prefix) !== null;
  }

  getWordsWithPrefix(prefix) {
    const node = this._findNode(prefix);
    if (!node) return [];

    const results = [];
    this._collect(node, prefix, results);
    return results;
  }

  _findNode(prefix) {
    let node = this.root;
    for (const ch of prefix) {
      if (!node.children[ch]) return null;
      node = node.children[ch];
    }
    return node;
  }

  _collect(node, current, results) {
    if (node.isEnd) results.push(current);
    for (const [ch, child] of Object.entries(node.children)) {
      this._collect(child, current + ch, results);
    }
  }
}

module.exports = Trie;
