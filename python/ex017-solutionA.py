# 10.21.20 - sjg 
# Exercise 17 - solution A
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

	product = 1 #product initialized to 1  bc 0 * anything == 0 https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/

	#multiply all ints in a list together - Traversal method https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
	for x in listInput: 
		product = product * x


	#new list that will house the product of each element except for element at i
	result = []

	for i in range(len(listInput)):

		#account for 0 as an element in the list bc dividing by 0 is undefined. This avoids the ZeroDivisionError
		if listInput[i] == 0:
			result.append('undefined')

		else:

			#divide product of all the ints in list by i to cancel out value of i
			result.append(product//listInput[i]) 	# // floor division aka integer division (using 1 "/" returned floating point numbers) 
													#https://www.quora.com/What-does-floor-division-in-Python-do

	return result 


print(productAllButI([1, 2, 3, 4, 5]))
print(productAllButI([3, 2, 1]))
print(productAllButI([16,2,13,0,99])) 

