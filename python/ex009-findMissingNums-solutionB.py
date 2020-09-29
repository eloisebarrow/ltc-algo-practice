# 09.28.20 - sjg 
# Exercise 9 - solution B
# Create a function called findMissingNums that takes in two arrays. 
#Iterate over the first array and IF the number you are iteratring 
#over is NOT present in the second array, push the number into it. 
#Once the loop is complete return the second array.

#Input: [0,1,2,3,4,5,6,7,8,9], [2,3,7,9]
#Output: [ 2, 3, 7, 9, 0, 1, 4, 5, 6, 8 ]

def findMissingNums(listOne, listTwo):


    listTwoDupe = listTwo.copy()


    for number_listOne in listOne:

    	if number_listOne not in listTwo:


             listTwoDupe.append(number_listOne)


    return listTwoDupe

print(findMissingNums([0,1,2,3,4,5,6,7,8,9], [2,3,7,9]))