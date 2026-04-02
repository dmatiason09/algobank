/**
 * Queue (FIFO)
 * Enqueue/Dequeue/Peek: O(1)
 *
 * Using an object with head/tail indices instead of an array
 * because shift() on arrays is O(n). This way both ends are O(1).
 */

class Queue {
  constructor() {
    this._storage = {};
    this._head = 0;
    this._tail = 0;
  }

  enqueue(item) {
    this._storage[this._tail] = item;
    this._tail++;
  }

  dequeue() {
    if (this.isEmpty()) {
      throw new Error('Cannot dequeue from empty queue');
    }
    const item = this._storage[this._head];
    delete this._storage[this._head];
    this._head++;
    return item;
  }

  peek() {
    if (this.isEmpty()) {
      throw new Error('Cannot peek empty queue');
    }
    return this._storage[this._head];
  }

  isEmpty() {
    return this._tail === this._head;
  }

  size() {
    return this._tail - this._head;
  }
}

module.exports = Queue;
