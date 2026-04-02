/**
 * Binary Search Tree
 *
 * Insert/Search/Delete: O(log n) avg, O(n) worst
 */

class BSTNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(val) {
    if (!this.root) {
      this.root = new BSTNode(val);
      return;
    }
    this._insert(this.root, val);
  }

  _insert(node, val) {
    if (val < node.val) {
      if (!node.left) node.left = new BSTNode(val);
      else this._insert(node.left, val);
    } else {
      if (!node.right) node.right = new BSTNode(val);
      else this._insert(node.right, val);
    }
  }

  search(val) {
    return this._search(this.root, val);
  }

  _search(node, val) {
    if (!node) return false;
    if (val === node.val) return true;
    if (val < node.val) return this._search(node.left, val);
    return this._search(node.right, val);
  }

  delete(val) {
    this.root = this._delete(this.root, val);
  }

  _delete(node, val) {
    if (!node) return null;

    if (val < node.val) {
      node.left = this._delete(node.left, val);
    } else if (val > node.val) {
      node.right = this._delete(node.right, val);
    } else {
      if (!node.left) return node.right;
      if (!node.right) return node.left;

      let successor = node.right;
      while (successor.left) successor = successor.left;
      node.val = successor.val;
      node.right = this._delete(node.right, successor.val);
    }
    return node;
  }

  inorder() {
    const result = [];
    this._inorder(this.root, result);
    return result;
  }

  _inorder(node, result) {
    if (node) {
      this._inorder(node.left, result);
      result.push(node.val);
      this._inorder(node.right, result);
    }
  }

  preorder() {
    const result = [];
    this._preorder(this.root, result);
    return result;
  }

  _preorder(node, result) {
    if (node) {
      result.push(node.val);
      this._preorder(node.left, result);
      this._preorder(node.right, result);
    }
  }

  height() {
    return this._height(this.root);
  }

  _height(node) {
    if (!node) return -1;
    return 1 + Math.max(this._height(node.left), this._height(node.right));
  }
}

module.exports = BST;
