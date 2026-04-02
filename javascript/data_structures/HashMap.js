/**
 * Hash Map (separate chaining)
 *
 * Put/Get/Remove: O(1) average, O(n) worst
 *
 * Resizes when load factor > 0.75. Using a simple hash function
 * that works for strings and numbers — not cryptographic obviously.
 */

const INITIAL_CAPACITY = 16;
const LOAD_FACTOR = 0.75;

class HashMap {
  constructor(capacity = INITIAL_CAPACITY) {
    this._capacity = capacity;
    this._size = 0;
    this._buckets = new Array(capacity).fill(null).map(() => []);
  }

  put(key, value) {
    const idx = this._hash(key);
    const bucket = this._buckets[idx];

    // check if key exists and update
    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket[i][1] = value;
        return;
      }
    }

    bucket.push([key, value]);
    this._size++;

    if (this._size / this._capacity > LOAD_FACTOR) {
      this._resize();
    }
  }

  get(key) {
    const idx = this._hash(key);
    const bucket = this._buckets[idx];

    for (const [k, v] of bucket) {
      if (k === key) return v;
    }

    throw new Error(`Key not found: ${key}`);
  }

  remove(key) {
    const idx = this._hash(key);
    const bucket = this._buckets[idx];

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        const val = bucket[i][1];
        bucket.splice(i, 1);
        this._size--;
        return val;
      }
    }

    throw new Error(`Key not found: ${key}`);
  }

  contains(key) {
    try {
      this.get(key);
      return true;
    } catch {
      return false;
    }
  }

  keys() {
    const result = [];
    for (const bucket of this._buckets) {
      for (const [k] of bucket) {
        result.push(k);
      }
    }
    return result;
  }

  values() {
    const result = [];
    for (const bucket of this._buckets) {
      for (const [, v] of bucket) {
        result.push(v);
      }
    }
    return result;
  }

  size() {
    return this._size;
  }

  _hash(key) {
    const str = String(key);
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      // djb2-ish hash
      hash = (hash * 31 + str.charCodeAt(i)) | 0;
    }
    return Math.abs(hash) % this._capacity;
  }

  _resize() {
    const oldBuckets = this._buckets;
    this._capacity *= 2;
    this._buckets = new Array(this._capacity).fill(null).map(() => []);
    this._size = 0;

    for (const bucket of oldBuckets) {
      for (const [key, value] of bucket) {
        this.put(key, value);
      }
    }
  }
}

module.exports = HashMap;
