/**
 * Counting Sort
 * Time:  O(n + k) where k = range of values
 * Space: O(k)
 *
 * Non-comparison sort. Only works with non-negative integers.
 */

function countingSort(arr) {
  if (arr.length === 0) return arr;

  const max = Math.max(...arr);
  const count = new Array(max + 1).fill(0);

  for (const num of arr) {
    count[num]++;
  }

  let idx = 0;
  for (let val = 0; val < count.length; val++) {
    for (let c = 0; c < count[val]; c++) {
      arr[idx] = val;
      idx++;
    }
  }

  return arr;
}

module.exports = countingSort;
