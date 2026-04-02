/**
 * Min Heap
 *
 * Insert:      O(log n)
 * Extract min: O(log n)
 * Peek:        O(1)
 */

class MinHeap {
  constructor() {
    this.data = [];
  }

  insert(val) {
    this.data.push(val);
    this._bubbleUp(this.data.length - 1);
  }

  extractMin() {
    if (this.data.length === 0) {
      throw new Error('Heap is empty');
    }

    const min = this.data[0];
    const last = this.data.pop();

    if (this.data.length > 0) {
      this.data[0] = last;
      this._bubbleDown(0);
    }

    return min;
  }

  peek() {
    if (this.data.length === 0) {
      throw new Error('Heap is empty');
    }
    return this.data[0];
  }

  size() {
    return this.data.length;
  }

  isEmpty() {
    return this.data.length === 0;
  }

  _bubbleUp(idx) {
    while (idx > 0) {
      const parent = Math.floor((idx - 1) / 2);
      if (this.data[idx] < this.data[parent]) {
        [this.data[idx], this.data[parent]] = [this.data[parent], this.data[idx]];
        idx = parent;
      } else {
        break;
      }
    }
  }

  _bubbleDown(idx) {
    const n = this.data.length;
    while (true) {
      let smallest = idx;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;

      if (left < n && this.data[left] < this.data[smallest]) smallest = left;
      if (right < n && this.data[right] < this.data[smallest]) smallest = right;

      if (smallest !== idx) {
        [this.data[idx], this.data[smallest]] = [this.data[smallest], this.data[idx]];
        idx = smallest;
      } else {
        break;
      }
    }
  }
}

module.exports = MinHeap;
