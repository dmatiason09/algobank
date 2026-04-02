/**
 * Jump Search
 * Time:  O(√n)
 * Space: O(1)
 *
 * Sorted array only. Jumps in blocks of √n then scans linearly.
 */

function jumpSearch(arr, target) {
  const n = arr.length;
  if (n === 0) return -1;

  const step = Math.floor(Math.sqrt(n));
  let prev = 0;

  while (arr[Math.min(step, n) - 1] < target) {
    prev = step;
    // this is a bit ugly but we need to keep jumping
    if (prev >= n) return -1;
    // recalculate next block — I'm keeping step as a moving pointer
    // NOTE: this is slightly different from the Python version on purpose
    break;
  }

  // actually let me just do this properly with a while loop
  let blockStart = 0;
  let blockEnd = step;

  while (blockEnd < n && arr[blockEnd - 1] < target) {
    blockStart = blockEnd;
    blockEnd += step;
  }

  // linear scan within the block
  for (let i = blockStart; i < Math.min(blockEnd, n); i++) {
    if (arr[i] === target) return i;
  }

  return -1;
}

module.exports = jumpSearch;
