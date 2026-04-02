/**
 * Heap Sort
 * Time:  O(n log n) always
 * Space: O(1)
 *
 * In-place with good worst-case, but quicksort usually wins
 * in practice because of better cache locality.
 */

function heapSort(arr) {
  const n = arr.length;

  // build max heap
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    heapify(arr, n, i);
  }

  for (let i = n - 1; i > 0; i--) {
    [arr[0], arr[i]] = [arr[i], arr[0]];
    heapify(arr, i, 0);
  }

  return arr;
}

function heapify(arr, heapSize, root) {
  let largest = root;
  const left = 2 * root + 1;
  const right = 2 * root + 2;

  if (left < heapSize && arr[left] > arr[largest]) {
    largest = left;
  }
  if (right < heapSize && arr[right] > arr[largest]) {
    largest = right;
  }

  if (largest !== root) {
    [arr[root], arr[largest]] = [arr[largest], arr[root]];
    heapify(arr, heapSize, largest);
  }
}

module.exports = heapSort;
