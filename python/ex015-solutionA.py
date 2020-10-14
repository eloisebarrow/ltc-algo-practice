# 10.13.20 - sjg 
# Exercise 15 - solution A
# Write a function called greatestCommomFactor that, 
#given two distinct positive integers,
#returns the greatest common factor of those two values

#Input: greatestCommonFactor(9,12)
#Output: 3

#Input: greatestCommonFactor(6,18)
#Output: 6

#Input: greatestCommonFactor(11,4)
#Output: 1

def greatestCommonFactor(posInt1, posInt2):
	
	#range of posInt1, plus posInt1
	range_posInt1 = list(range(1,posInt1+1))

	# list of factors
	factors_posInt1 = []

	#iterating i through range_posInt1, starting i == 1, if int % i is zero, 
	#then divisible, meaning it's a factor, so add i in those cases to list of factors
	#dont use a break statement bc each integer needs to be checked within the range list

	for i in range_posInt1:
		if posInt1 % i == 0:
			factors_posInt1.append(i)

	#range of posInt2, plus posInt2
	range_posInt2 = list(range(1,posInt2+1))

	#factors_posInt2 - list of factors, create empty list
	factors_posInt2 = []

	for i in range_posInt2: 
		if posInt2 % i == 0:
			factors_posInt2.append(i)

	#define int variable, result, which will house the greatest common factor between the 2 parameters,
	# and default value being 1 bc for posInts, the smallest factor of a pos # would be 1
	result = 1


	#iterating through the factors of posInt1, 
	for factor_posInt1 in factors_posInt1:
		#if particular value is present in factors_posInt2
		if factor_posInt1 in factors_posInt2:

		#set result equal to that factor
			result = factor_posInt1
		
		#no break statement bc need to go through entire for loop to get answer

	print("The greatest common factor of", posInt1, "and", posInt2, "is:")
	return result


print(greatestCommonFactor(9,12))
print(greatestCommonFactor(6,18))
print(greatestCommonFactor(11,4))