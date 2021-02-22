// Find pair with given sum in the array:

// Given an unsorted integer array, find a pair with a given sum in it.

// Input:
 
// arr = [8, 7, 2, 5, 3, 1]
// sum = 10
 
// Output:
 
// Pair found at index 0 and 2 (8 + 2)
 
// or
 
// Pair found at index 1 and 4 (7 + 3)

const sumPair = (arr, sum) => {
  let complements = {};
  for (let i = 0; i < arr.length; i++) {
    let current = arr[i];
    let complement = sum - current;
    if (complements[complement]) {
      return `Pair found at ${arr.indexOf(complement)} and ${arr.indexOf(current)} (${complement} + ${current})`;
    }
    complements[current] = complement;
  }
  
  return 'None found'
}

console.log(sumPair([8, 7, 2, 5, 3, 1], 10)) // Pair found at index 0 and 2 (8 + 2)

// Time complexity: O(n) (linear) where n is the size of the input. Requires O(n) extra space.