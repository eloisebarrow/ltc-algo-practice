/********************  UNFINISHED *************/

// Given an integer array, print all subarrays with zero-sum

// Input:  { 4, 2, -3, -1, 0, 4 }
 
// Subarrays with zero-sum are
 
// { -3, -1, 0, 4 }
// { 0 }
 
 
// Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
// Subarrays with zero-sum are
 
// { 3, 4, -7 }
// { 4, -7, 3 }
// { -7, 3, 1, 3 }
// { 3, 1, -4 }
// { 3, 1, 3, 1, -4, -2, -2 }
// { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

const printSubarrays = (arr) => {
  // let subarrays = [];
  for (let i = 0; i <= arr.length; i++) {
    let sum = 0;
    let current = arr[i];
    // let currentArray = [current];
    sum += current;
    for (let j = i + 1; j <= arr.length - 1; j++) {
      // currentArray.push(arr[j]);
      sum += arr[j];
      if (sum === 0) subarrays.push(currentArray);
      // sum += arr[j];
    }
  }
  return subarrays.forEach(arr => {
    console.log(arr)
  })
}

printSubarrays([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])