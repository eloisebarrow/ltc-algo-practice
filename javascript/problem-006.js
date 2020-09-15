const printArr = (input) => {
  let names = ''
  for (let name of input) {
    names += `${name} \n`
  }
  return names
}

console.log(printArr(['sally','monique','caleb'])) 
/*
sally
monique
caleb
*/