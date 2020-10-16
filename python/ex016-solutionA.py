# 10.15.20 - sjg 
# Exercise 16 - solution A
# Write a function called stringCompress that, 
#given a string of only letters, returns a
#string that represents a numerically compressed format of the string.

#Input: stringCompress("abbcccddddec")
#Output: a2b3c4dec

#Input: stringCompress("abcd")
#Output: abcd

def stringCompress(stringInput):

	compressedString = ''

	#default to 1, bc there's at least always 1 count of a specific char in a string
	counter = 1


	for i in range(len(stringInput)):
		
		#if at beginning index and first char does not match second char
		if i == 0 and stringInput[i] != stringInput[i+1]:

			#add the char, don't add the counter since it's not repeating
			compressedString += stringInput[i]

		#condition is so there's no IndexError	
		#zero indexed, so if i is less than the -1 index
		#current character and the character right after it == each other

		#this accounts for all repeating chars at end of string bc counter originally set to 1,
		##so any +1's to the counter are to record the char that comes after the current iteration
		elif i < len(stringInput)-1 and stringInput[i] == stringInput[i+1]:
				
			counter += 1
			
		#if not index[0] and not index[-1], and char @ current iteration
		# does not match char @ (current iteration + 1)

		elif i < len(stringInput)-1 and stringInput[i] != stringInput[i+1]:

			#if i put within above elif*, it would be something like "a2b2c3c2d3d4d" - repetitive for > 2 repeating for a char	
				# *elif i < len(stringInput)-2 and stringInput[i] == stringInput[i+1]:
				#above elif statement has to iterate through all matching consecutive chars first

			if counter == 1: 
				compressedString += stringInput[i] #bc dont need int counter if 1 in front

			else: 

				compressedString += str(counter) + stringInput[i] 

			#reset counter - if i put it within elif statement where == it'll reset before done
			# isn't ok to reset anyway, since starts w/ 1 anyway?
			#ask mjl
			counter = 1


		#add elif for not at i == len(stringInput)-1 but not consecutive matching
		#the previous if and elif statements do not account for printing character at index -1

		#this rounds out answering the 2 given inputs/outputs, but not "abbcccddddecccccc"
		elif i == len(stringInput)-1 and stringInput[i] != stringInput[i-1]:
		

			compressedString = compressedString + stringInput[i] #bc dont need int counter if 1 in front


		#add elif for not at i == len(stringInput)-1 [a.k.a. last index] and consecutive matching

		elif i == len(stringInput)-1 and stringInput[i] == stringInput[i-1]:

#			#no need for counter += 1 because the first elif statement counts the consecutive chars already
			#but DO need elif for printing what comes at the end 

			compressedString = compressedString + str(counter) + stringInput[i]


	print("numerically compressed format of '", stringInput, "' is:", sep='')
	return compressedString 


print(stringCompress("abbcccddddec"))
print("\n")
print(stringCompress("abcd"))
print("\n")
#added another to test case where repeating char starting at index 0 and repeating @ index -1
print(stringCompress("aaabbcccddddecccccc"))
