# 09.16.20 sjg 
#Exercise 5 - solution C
#Write a function called largestNumber that will return the largest value from an array.

#Input: [1,2,5,10]
#Output: 10


def largestNumber(integerList):

	result = max(integerList)

	return result


print(largestNumber([1,2,5,10]))
print(largestNumber([234324,2,34,345]))
