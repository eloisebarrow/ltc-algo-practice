function phoneBook(input,mapped) {
    const contacts = [];
    const hash = {};
    const inputLen = input.length - 1;
    
    for (let i = 0; i <= inputLen; i += 1) {
      const contact = Object.keys(input[i]);
      hash[contact[0]] = input[i][contact];
    }
    for (let i = 0; i <= inputLen; i += 1) {
      let string = '';
      if (hash[mapped[i]]) {
        string += `${mapped[i]} = ${hash[mapped[i]]}`;
      } else {
        string += 'Not found';
      }
      contacts.push(string);
    }
    return contacts.join('\n')
} 

console.log(phoneBook([{sam:99912222},{tom:11122222},{harry:12299933}], ['sam','ed','harry']))
// sam=99912222
// NOT FOUND
// harry:12299933