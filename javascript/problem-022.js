// Check if subarray with 0 sum exists or not

// Given an integer array, check if it contains a subarray having zero-sum

// Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
// Output: Subarray with zero-sum exists
 
// The subarrays with a sum of 0 are:
 
// { 3, 4, -7 }
// { 4, -7, 3 }
// { -7, 3, 1, 3 }
// { 3, 1, -4 }
// { 3, 1, 3, 1, -4, -2, -2 }
// { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

// Note that the problem deals with subarrays that are contiguous i.e. whose elements occupy consecutive positions in the array.

// Brute force solution - O(n^2) time, where n is the size of the input
const sumZero = (arr) => {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
    for (let j = i + 1; j < arr.length - 1; j++) {
      if (sum + arr[j] === 0) return 'Subarray with zero-sum exists';
      sum += arr[j];
    }
    sum = 0;
  }
  return 'Subarray with zero-sum does not exist';
}

console.log(sumZero([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])) // Subarray with zero-sum exists
console.log(sumZero([3, 4, 2, -7])) // Subarray with zero-sum does not exist

// See python/ex021-zerosum.py for efficient solution - O(n) time and space, where n is the size of the input