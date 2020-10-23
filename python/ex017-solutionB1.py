# 10.22.20 - sjg 
# Exercise 17 - solution B1
#Given a list (or array) of integers, return a new list such that 
#each element at index i of the new list is the 
#product of all the numbers in the original list except the one at i.

#Input: [1, 2, 3, 4, 5]
#Output: [120, 60, 40, 30, 24]

#Input: [3, 2, 1]
#Output: [2, 3, 6]

#Added difficulty:
#Answer cannot include division.

def productAllButI(listInput):

	#shallow copy https://www.geeksforgeeks.org/python-list-copy-method/
	list_copy = listInput.copy()

	result = []

	import numpy as np

	for i in range(len(listInput)):
	#if copy contains value at listInput[i] (can use if-in membership) https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
		if listInput[i] in list_copy:

			#remove value at index i from copy
			#remove() removes a list element by value https://medium.com/better-programming/4-ways-to-remove-elements-from-a-list-in-python-3b8f4afd1b83
			list_copy.remove(listInput[i])

			#then multiply the remaining elements in copy 
			product = np.prod(list_copy)

			#then add product to result (result[i] will match up to listInput[i]) indices since starts out as copy of each other
			result.append(product)

			#reset list_copy to the full list, or else the for loop will just keep removing elements from same list, til it's empty 
			#e.g. wrong answer without resetting list_copy to full list, for first case would be: [120, 60, 20, 5, 1.0]
			list_copy = listInput.copy()


	return result 



print(productAllButI([1, 2, 3, 4, 5]))
print(productAllButI([3, 2, 1]))
print(productAllButI([16,2,13,0,99])) 