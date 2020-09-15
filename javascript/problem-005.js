// PROBLEM 5

const largestNumber = (arrNums) => {
  let largest = 0;
  for (let i = 0; i < arrNums.length; i++) {
    arrNums[i] > largest ? largest = arrNums[i] : null
  }
  return largest
}

console.log(largestNumber([1,2,5,10])) // 10