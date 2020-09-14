// PROBLEM 1

// Given a two-digit integer, return the sum of its digits.
const addDigits = (n) => {
  n = n.toString().split('')
  return parseInt(n[0]) + parseInt(n[1])
}

console.log(addDigits(29)) // 11
console.log(addDigits(30)) // 3 

// PROBLEM 2

// Write a function called oddsEvens that given a string, prints its even-indexed and odd-indexed characters as space-separated strings on a single line.

const oddsEvens = (input) => {
  let left = '';
  let right = '';
  for (let i = 0; i < input.length; i += 1) {
    if (i % 2 === 0) {
      left += input[i];
    } else {
      right += input[i];
    }
  }
  return `${left} ${right}`;
}

console.log(oddsEvens('Hacker')) // Hce akr

// PROBLEM 3

const isAnagram = (str1, str2) => {
  let obj1 = {}
  for (let i = 0; i < str1.length; i++) {
    let current = str1[i]
    obj1[current] = (obj1[current] || 0) + 1
  }
  for (let i = 0; i < str2.length; i++) {
    let current = str2[i]
    if (obj1[current] > 0) {
      obj1[current]--
    } else {
      return false;
    }
    return true
  }
}

console.log(isAnagram("cinema", "iceman")) // true
console.log(isAnagram("randum", "werdz")) // false

// PROBLEM 4

const longestStrings = () => {

}

console.log(longestStrings(["aba", "aa", "ad", "vcd", "aba"])) // ["aba", "vcd", "aba"]

// PROBLEM 5

const largestNumber = () => {

}

console.log(largestNumber([1,2,5,10])) // 10