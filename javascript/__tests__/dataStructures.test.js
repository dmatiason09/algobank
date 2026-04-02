const { Stack, Queue, LinkedList, HashMap } = require('../data_structures');

describe('Stack', () => {
  let stack;
  beforeEach(() => { stack = new Stack(); });

  test('push and pop', () => {
    stack.push(1);
    stack.push(2);
    stack.push(3);
    expect(stack.pop()).toBe(3);
    expect(stack.pop()).toBe(2);
  });

  test('peek returns top without removing', () => {
    stack.push('hello');
    expect(stack.peek()).toBe('hello');
    expect(stack.size()).toBe(1);
  });

  test('isEmpty', () => {
    expect(stack.isEmpty()).toBe(true);
    stack.push(1);
    expect(stack.isEmpty()).toBe(false);
  });

  test('pop on empty throws', () => {
    expect(() => stack.pop()).toThrow();
  });

  test('LIFO order', () => {
    [0, 1, 2, 3, 4].forEach(i => stack.push(i));
    const result = [];
    while (!stack.isEmpty()) result.push(stack.pop());
    expect(result).toEqual([4, 3, 2, 1, 0]);
  });
});

describe('Queue', () => {
  let queue;
  beforeEach(() => { queue = new Queue(); });

  test('enqueue and dequeue', () => {
    queue.enqueue('a');
    queue.enqueue('b');
    queue.enqueue('c');
    expect(queue.dequeue()).toBe('a');
    expect(queue.dequeue()).toBe('b');
  });

  test('peek returns front without removing', () => {
    queue.enqueue(10);
    expect(queue.peek()).toBe(10);
    expect(queue.size()).toBe(1);
  });

  test('isEmpty', () => {
    expect(queue.isEmpty()).toBe(true);
    queue.enqueue(1);
    expect(queue.isEmpty()).toBe(false);
  });

  test('dequeue on empty throws', () => {
    expect(() => queue.dequeue()).toThrow();
  });

  test('FIFO order', () => {
    [0, 1, 2, 3, 4].forEach(i => queue.enqueue(i));
    const result = [];
    while (!queue.isEmpty()) result.push(queue.dequeue());
    expect(result).toEqual([0, 1, 2, 3, 4]);
  });

  test('mixed operations', () => {
    queue.enqueue(1);
    queue.enqueue(2);
    expect(queue.dequeue()).toBe(1);
    queue.enqueue(3);
    expect(queue.dequeue()).toBe(2);
    expect(queue.dequeue()).toBe(3);
  });
});

describe('LinkedList', () => {
  let list;
  beforeEach(() => { list = new LinkedList(); });

  test('append builds list in order', () => {
    list.append(1);
    list.append(2);
    list.append(3);
    expect(list.toArray()).toEqual([1, 2, 3]);
  });

  test('insertAtHead', () => {
    list.append(2);
    list.append(3);
    list.insertAtHead(1);
    expect(list.toArray()).toEqual([1, 2, 3]);
  });

  test('delete head', () => {
    list.append(1);
    list.append(2);
    expect(list.delete(1)).toBe(true);
    expect(list.toArray()).toEqual([2]);
  });

  test('delete middle element', () => {
    list.append(1);
    list.append(2);
    list.append(3);
    list.delete(2);
    expect(list.toArray()).toEqual([1, 3]);
  });

  test('delete returns false when not found', () => {
    list.append(1);
    expect(list.delete(99)).toBe(false);
  });

  test('search', () => {
    list.append(10);
    list.append(20);
    list.append(30);
    expect(list.search(20)).toBe(1);
    expect(list.search(99)).toBe(-1);
  });

  test('reverse', () => {
    list.append(1);
    list.append(2);
    list.append(3);
    list.reverse();
    expect(list.toArray()).toEqual([3, 2, 1]);
  });

  test('reverse empty list does nothing', () => {
    list.reverse();
    expect(list.toArray()).toEqual([]);
  });

  test('length', () => {
    expect(list.length).toBe(0);
    list.append(1);
    list.append(2);
    expect(list.length).toBe(2);
  });
});

describe('HashMap', () => {
  let map;
  beforeEach(() => { map = new HashMap(); });

  test('put and get', () => {
    map.put('name', 'Dennis');
    map.put('age', 25);
    expect(map.get('name')).toBe('Dennis');
    expect(map.get('age')).toBe(25);
  });

  test('update existing key', () => {
    map.put('x', 1);
    map.put('x', 2);
    expect(map.get('x')).toBe(2);
    expect(map.size()).toBe(1);
  });

  test('get missing key throws', () => {
    expect(() => map.get('nope')).toThrow();
  });

  test('remove', () => {
    map.put('a', 1);
    map.put('b', 2);
    expect(map.remove('a')).toBe(1);
    expect(map.contains('a')).toBe(false);
    expect(map.size()).toBe(1);
  });

  test('contains', () => {
    map.put('key', 'val');
    expect(map.contains('key')).toBe(true);
    expect(map.contains('other')).toBe(false);
  });

  test('keys and values', () => {
    map.put('a', 1);
    map.put('b', 2);
    map.put('c', 3);
    expect(map.keys().sort()).toEqual(['a', 'b', 'c']);
    expect(map.values().sort()).toEqual([1, 2, 3]);
  });

  test('handles many entries (resize)', () => {
    const smallMap = new HashMap(4);
    for (let i = 0; i < 50; i++) {
      smallMap.put(`key_${i}`, i);
    }
    expect(smallMap.size()).toBe(50);
    for (let i = 0; i < 50; i++) {
      expect(smallMap.get(`key_${i}`)).toBe(i);
    }
  });

  test('works with number keys', () => {
    map.put(1, 'one');
    map.put(2, 'two');
    expect(map.get(1)).toBe('one');
  });
});
