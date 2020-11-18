# 11.17.20 sjg 
#Exercise 19 - solution A
#Given a list of integers, return a list of even integers, squared. 

#Input: [8,1,9,10]
#Output: [64,100]

def evenIntegers(intList):

#square a number, ** (power) operator https://kodify.net/python/math/square/#:~:text=There%20are%20several%20ways%20to,multiply%20a%20value%20with%20itself.
#could've also used pow(i, 2)
	return [i**2 for i in intList if i % 2 == 0]


print(evenIntegers([8,1,9,10]))
print(evenIntegers([45,11, 16, 6]))
print(evenIntegers([-34,17,44, 	0]))
#test for empty list
print(evenIntegers([]))
#just skips it, does the for loop zero times
#empty list is valid input