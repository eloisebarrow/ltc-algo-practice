const hasVowels = (arr) => {
    let vowels = ["a", "e", "i", "o", "u"]
    const vowelWords = [];
    arr.forEach( word => {
        for(let j = 0; j < vowels.length; j++) {
          console.log('this is word', word, vowels[j])
          if(word.includes(vowels[j])) {
            vowelWords.push(word)
            return 
          }
        }
    })
    return vowelWords
}

console.log(hasVowels(['jon', 'ada', 'ppzpp', 'brgggg', 'eric'])) // ['jon', 'ada', 'eric']