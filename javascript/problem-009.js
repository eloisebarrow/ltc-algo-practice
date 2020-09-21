function findMissingNums(arr1, arr2) {
    arr1.forEach((d,i) => {
       if( !arr2.includes(arr1[i])) { arr2.push(i) }
    })
    return arr2
}

console.log(findMissingNums([0,1,2,3,4,5,6,7,8,9], [2,3,7,9]))
// [ 2, 3, 7, 9, 0, 1, 4, 5, 6, 8 ]