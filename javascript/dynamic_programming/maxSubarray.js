/**
 * Maximum Subarray (Kadane's Algorithm)
 * Time:  O(n)
 * Space: O(1)
 */

function maxSubarray(arr) {
  if (arr.length === 0) return 0;

  let maxSum = arr[0];
  let current = arr[0];

  for (let i = 1; i < arr.length; i++) {
    current = Math.max(arr[i], current + arr[i]);
    maxSum = Math.max(maxSum, current);
  }

  return maxSum;
}

module.exports = maxSubarray;
