/**
 * Interpolation Search
 * Time:  O(log log n) average for uniform data, O(n) worst
 * Space: O(1)
 *
 * Estimates position instead of always picking the middle.
 * Sorted array with uniformly distributed values is the ideal case.
 */

function interpolationSearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;

  while (low <= high && target >= arr[low] && target <= arr[high]) {
    if (low === high) {
      return arr[low] === target ? low : -1;
    }

    const pos = low + Math.floor(
      ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
    );

    if (pos < low || pos > high) return -1;

    if (arr[pos] === target) return pos;

    if (arr[pos] < target) {
      low = pos + 1;
    } else {
      high = pos - 1;
    }
  }

  return -1;
}

module.exports = interpolationSearch;
