// PROBLEM 4

const longestStrings = (strs) => {
  let output = []
  let longest = 0
  for (let i = 0; i < strs.length; i++) {
    let current = strs[i]
    if (current.length > longest) {
      longest = current.length;
      output = [current]
    } else if (current.length === longest) {
      output.push(current)
    }
  }
  return output;
}

console.log(longestStrings(["aba", "aa", "ad", "vcd", "aba"])) // ["aba", "vcd", "aba"]