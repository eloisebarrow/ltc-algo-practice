# 09.18.20 - sjg 
# Exercise 7 - solution A2
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


#not accounting for spaces or punctuation marks
def isPalindrome(string):

	#reverse a string (not fastest execution time for reversing string)
	string_reversed = "".join(reversed(string))
	
	if string == string_reversed:
		return True

	else: return False
	
print(isPalindrome("tacocat"))
print(isPalindrome("nottacocat"))