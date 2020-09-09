// DAY 1

// Given a two-digit integer, return the sum of its digits.
const addDigits = (n) => {
  n = n.toString().split('')
  return parseInt(n[0]) + parseInt(n[1])
}

console.log(addDigits(29)) // 11
console.log(addDigits(30)) // 3 