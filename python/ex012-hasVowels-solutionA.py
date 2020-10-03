# 10.02.20 - sjg 
# Exercise 12 - solution A
# Write a function called hasVowels that takes in an array 
#of words and returns a new array of only those words that 
#contain one or more vowels.

#Input: hasVowels(['jon', 'ada', 'ppzpp', 'brgggg', 'eric'])
#Output: ['jon', 'ada', 'eric']


def hasVowels(inputList):

	#strings from input that have vowels
	result = []

	#list of vowels
	vowels = ['a', 'e', 'i', 'o', 'u']

	for word in inputList:
	
		#if a e i o or u is in word, add word to result list

		if vowels[0] in word:

			result.append(word)
			

		elif vowels[1] in word:
		
			result.append(word)


		elif vowels[2] in word:

			result.append(word)

		elif vowels[3] in word:

			result.append(word)

		elif vowels[4] in word:
			
			result.append(word)
	

	return result


print(hasVowels(['jon', 'ada', 'ppzpp', 'brgggg', 'eric']))