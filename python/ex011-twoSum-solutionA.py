# 10.05.20 - sjg 
# Exercise 11 - solution A
# Write a function called twoSum that given an array(list) of integers 
#and a target number, returns two array(list) integers that add up to 
#the target.

#Input: [3, 2, 5, 7, 11, 15], 9
#Output: Return [2, 7]

def twoSum(intList, targetNumber):

	result = []

	intList_copy = intList.copy()
	
	for value_copy in intList_copy:

		for value in intList:
			
			if (value_copy + value == targetNumber) and (value_copy != value):
				
				
				result.append(value_copy)
				
				break


	return result

print(twoSum([3, 2, 5, 7, 11, 15], 9))