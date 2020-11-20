# 11.19.20 - sjg 
# Exercise 12 - solution B
# Write a function called hasVowels that takes in an array 
#of words and returns a new array of only those words that 
#contain one or more vowels.

#Input: hasVowels(['jon', 'ada', 'ppzpp', 'brgggg', 'eric'])
#Output: ['jon', 'ada', 'eric']


def hasVowels(inputList):
	
	# look for specific letter in word | uinsg 'in' operator | 7.7. The in operator https://www.openbookproject.net/thinkcs/python/english2e/ch07.html
	hasVowels_or_emptyStrings = [word if 'a' in word else word if 'e' in word else word if 'i' in word else word if 'o' in word else word if 'u' in word else '' for word in inputList]
	#don't forget final else
	#confused how to append list with nothing, found link that reminded me when it's not if..else, you can use basic syntax https://stackoverflow.com/questions/29179881/how-can-i-add-nothing-to-the-list-in-list-comprehension
	#use basic syntax: [expr for value in collection if conditional]
	
	#use conditional to weed out the empty strings 
	return [i for i in hasVowels_or_emptyStrings if len(i) > 0]

print(hasVowels(['jon', 'ada', 'ppzpp', 'brgggg', 'eric']))