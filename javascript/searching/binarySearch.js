/**
 * Binary Search
 * Time:  O(log n)
 * Space: O(1) iterative / O(log n) recursive
 *
 * Array must be sorted.
 */

function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    const mid = low + Math.floor((high - low) / 2);

    if (arr[mid] === target) return mid;
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return -1;
}

function binarySearchRecursive(arr, target, low = 0, high = arr.length - 1) {
  if (low > high) return -1;

  const mid = low + Math.floor((high - low) / 2);

  if (arr[mid] === target) return mid;
  if (arr[mid] < target) {
    return binarySearchRecursive(arr, target, mid + 1, high);
  }
  return binarySearchRecursive(arr, target, low, mid - 1);
}

module.exports = { binarySearch, binarySearchRecursive };
