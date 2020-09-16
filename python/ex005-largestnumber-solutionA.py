# 09.16.20 sjg 
#Exercise 5 - solution A
#Write a function called largestNumber that will return the largest value from an array.

#Input: [1,2,5,10]
#Output: 10

def largestNumber(integerList):

	integerList.sort()

	
	result = integerList[-1]


	return result



print(largestNumber([1,2,5,10]))
print(largestNumber([3,480,12384,380,30242234982,3,2310]))
print(largestNumber([7,3,5,7,9,9,5]))
