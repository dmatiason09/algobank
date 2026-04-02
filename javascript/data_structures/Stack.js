/**
 * Stack (LIFO)
 * Push/Pop/Peek: O(1)
 */

class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    if (this.isEmpty()) {
      throw new Error('Cannot pop from empty stack');
    }
    return this.items.pop();
  }

  peek() {
    if (this.isEmpty()) {
      throw new Error('Cannot peek empty stack');
    }
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }
}

module.exports = Stack;
