# 11.16.20 sjg - solution D
#Exercise 4
#Given an array of strings, return another array containing 
#all of its longest strings.

#Input: ["aba", "aa", "ad", "vcd", "aba"]
#Output: ["aba", "vcd", "aba"]

def lengthOfValue(x):
	
	return len(x)

def longestStringsInArray(listInput):

	listInput.sort(key=lengthOfValue)
	
	length_LastElement = len(listInput[-1])

	#list comprehension version of solution A
	return [element for element in listInput if len(element) == length_LastElement]


print(longestStringsInArray(["aba", "aa", "ad", "vcd", "aba"]))