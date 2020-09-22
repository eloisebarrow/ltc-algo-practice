const twoSum = (arr, target) => {
  const hash = {};
  for (let i = 0; i < arr.length; i += 1) {
    const val = arr[i];
    const complement = target - val;
    if (hash[complement] !== undefined) {
      return [val, complement];
    }
    hash[val] = i;
  }
  return null;
}

console.log(twoSum([3, 2, 5, 7, 11, 15], 9)) // [2, 7]