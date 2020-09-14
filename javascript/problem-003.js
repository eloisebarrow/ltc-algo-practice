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