# 09.14.20 sjg
#Write a function called isAnagram 
#that, given 2 strings, returns true 
#if the strings are anagrams
#isAnagram("cinema", "iceman") == True
#isAnagram("randum" "werdz") == False

def isAnagram(string1, string2): 
	

	#string1, sorted A-Z 
	string1_sorted = sorted(string1)

	#string2, sorted A-Z 
	string2_sorted = sorted(string2)


	# if identical - true, else - not anagram
	if string1_sorted == string2_sorted:
		return True

	else:
		return False


print(isAnagram('stressed', 'desserts'))
print(isAnagram('randum', 'werdz'))




