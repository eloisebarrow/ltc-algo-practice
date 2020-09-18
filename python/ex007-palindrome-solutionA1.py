# 09.18.20 - sjg 
# Exercise 7 - solution A1
# Write a function called isPalindrome that, 
#given a string, returns true
#if the string is a palindrome, and false if not

#Input: isPalindrome("tacocat") 
#Output: True

#Input: isPalindrome("nottacocat")
#Output: False

#Additional levels of difficulty:
#Input: isPalindrome("Race car")
#Output: True

#Input: isPalindrome("a man, a plan, a canal - panama")
#Output: True


#current solution not accounting for spaces or punctuation marks
def isPalindrome(string):

	#fastest execution time for reversing string - slice that steps backwards, -1. string[::-1]
	string_reversed = string[::-1]

	if string == string_reversed:
		return True

	else: return False


print(isPalindrome("tacocat"))
print(isPalindrome("nottacocat"))