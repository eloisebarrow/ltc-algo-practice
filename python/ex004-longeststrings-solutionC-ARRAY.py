# 09.16.20 sjg 
#Exercise 4 - solution C
#Given an array of strings, return another array containing 
#all of its longest strings.

#Input: ["aba", "aa", "ad", "vcd", "aba"]
#Output: ["aba", "vcd", "aba"]


def longestStringsInArray(listInput):

	import numpy as np

	#convert list to array
	arr = np.array(listInput)

	#start with length of index 0 of input array
	lengthLongestString = len(arr[0])

	#find largest length of string in input array
	for i in arr:

		if len(i) > lengthLongestString:

			lengthLongestString = len(i)

	#declare empty array for longest strings

	result_array = np.array([])

	for i in arr:

		if len(i) == lengthLongestString:
			#append result_array with value at index i
			result_array = np.append(result_array, i)

	return result_array

print(longestStringsInArray(["aba", "aa", "ad", "vcd", "aba"]))