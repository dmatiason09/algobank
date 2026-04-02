/**
 * Linear Search
 * Time:  O(n)
 * Space: O(1)
 */

function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) return i;
  }
  return -1;
}

module.exports = linearSearch;
