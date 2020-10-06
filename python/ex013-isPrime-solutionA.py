# 10.06.20 - sjg 
# Exercise 13 - solution A
# Write a function called isPrime, that takes in a positive integer 
#and returns True if number is Prime, otherwise false

#Input: isPrime(10)
#Output: False

#Input: isPrime(13)
#Output: True

def isPrime(posInt):

	#result = True, unless proven otherwise! define outside for loop
	result = True

	for inBetweenNumber in range(2, posInt):
		if posInt % inBetweenNumber == 0:
			#false bc in range i to posInt-i, posInt is 
			#divisble by something other than 1 and itself
			result = False
			break
		#break out of for loop once result = False, bc no need to compute remaining

	#account for 1 as input, since 1 is not a prime number
	if posInt == 1:

		result = False


	return result

print(isPrime(10))
print(isPrime(13))
print(isPrime(1))
print(isPrime(2))