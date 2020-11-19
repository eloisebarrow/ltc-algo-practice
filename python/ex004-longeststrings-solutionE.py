# 11.18.20 sjg - solution E
#Exercise 4
#Given an array of strings, return another array containing 
#all of its longest strings.

#Input: ["aba", "aa", "ad", "vcd", "aba"]
#Output: ["aba", "vcd", "aba"]


def lengthOfValue(x):
	
	return len(x)


def longestStringsInArray(listInput):

	listInput.sort(key=lengthOfValue)

	# DOESN'T WORK: [listInput.remove(element) for element in listInput if len(element) != len(listInput[-1])]
	# Why? Bc listInput.remove(element) returns None.

	# "initializing remove list" | https://www.geeksforgeeks.org/python-remove-all-values-from-a-list-present-in-other-list/
	remove_list = [i for i in listInput if len(i) != len(listInput[-1])]
													# length of last element == len(listInput[-1]

	return [i for i in listInput if i not in remove_list]



print(longestStringsInArray(["aba", "aa", "ad", "vcd", "aba"]))