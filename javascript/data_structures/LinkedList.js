/**
 * Singly Linked List
 *
 * Insert at head: O(1)
 * Append:         O(n)
 * Delete/Search:  O(n)
 */

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  insertAtHead(data) {
    const node = new Node(data);
    node.next = this.head;
    this.head = node;
  }

  append(data) {
    const node = new Node(data);
    if (!this.head) {
      this.head = node;
      return;
    }

    let curr = this.head;
    while (curr.next) {
      curr = curr.next;
    }
    curr.next = node;
  }

  delete(data) {
    if (!this.head) return false;

    if (this.head.data === data) {
      this.head = this.head.next;
      return true;
    }

    let curr = this.head;
    while (curr.next) {
      if (curr.next.data === data) {
        curr.next = curr.next.next;
        return true;
      }
      curr = curr.next;
    }
    return false;
  }

  search(data) {
    let curr = this.head;
    let idx = 0;
    while (curr) {
      if (curr.data === data) return idx;
      curr = curr.next;
      idx++;
    }
    return -1;
  }

  reverse() {
    let prev = null;
    let curr = this.head;
    while (curr) {
      const next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
    }
    this.head = prev;
  }

  toArray() {
    const result = [];
    let curr = this.head;
    while (curr) {
      result.push(curr.data);
      curr = curr.next;
    }
    return result;
  }

  get length() {
    let count = 0;
    let curr = this.head;
    while (curr) {
      count++;
      curr = curr.next;
    }
    return count;
  }
}

module.exports = LinkedList;
