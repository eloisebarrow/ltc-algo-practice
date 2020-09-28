# 09.28.20 - sjg
# Exercise 9 - solution A
# Create a function called findMissingNums that takes in two arrays. 
#Iterate over the first array and IF the number you are iteratring 
#over is NOT present in the second array, push the number into it. 
#Once the loop is complete return the second array.

#Input: [0,1,2,3,4,5,6,7,8,9], [2,3,7,9] 
#Output: [ 2, 3, 7, 9, 0, 1, 4, 5, 6, 8 ]

def findMissingNums(listOne, listTwo):

    #copy to append
    listTwoDupe = listTwo.copy()

    #Iterate over the first array
    for number_listOne in listOne:
         
        found = False

        for number_listTwo in listTwo:
    
            if number_listOne == number_listTwo:
            
                #boolean for match, if true dont append           
                found = True
                break
       
        #outside of nested for loop
        if found == False:  
            listTwoDupe.append(number_listOne)  
        

    return listTwoDupe


print(findMissingNums([0,1,2,3,4,5,6,7,8,9], [2,3,7,9]))