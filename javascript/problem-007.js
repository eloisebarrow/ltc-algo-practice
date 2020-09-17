const reversed = (s) => {
  let output = ''
  for (let i = s.length - 1; i >= 0; i--) {
    output += s[i]
  }
  return output
}

const isPalindrome = (input) => {
  input = input.toLowerCase().split(' ').join('')
  return input === reversed(input)
}

console.log(isPalindrome("tacocat")) // true
console.log(isPalindrome("nottacocat")) // false
console.log(isPalindrome("Race car")) // true
// console.log(isPalindrome("a man, a plan, a canal - panama")) // true