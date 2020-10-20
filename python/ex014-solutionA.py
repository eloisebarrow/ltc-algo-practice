# 10.20.20 - sjg 
# Exercise 14 - solution A
# Write a function called uniqueVals that will return an array of unique values, no duplicates allowed. 
#It will accept 2 arguments, the first will be the desired length of the returned array and the 
#second will the be the max value in the random set.

#########

#assumption: each of 2 arguments is an int
def uniqueVals(int1, int2):

	#list of unique values
	result = []

	import random		
	
	#startingInt = 0 only works if int2 is >= 0, doesn't work if argument #2 (int2) is negative
	#don't need to worry about using abs(int1) since int1 must be at least 0, and user is prompted if int1 is less than 0
	#initially thought startingInt could be negative of abs(int2)
	#BUT it has to be in relation to int1 (length of list) to make sure no ValueError: Sample larger than population or is negative
	
	#i added *2 (instead of just startingInt = int2 - int1) to add more variety to random numbers generated
	#but startingInt = int2 - int1 would work, too
	startingInt = int2 - int1*2

	#sequence: ordered set
	sequence = range(startingInt, int2+1)


	print("uniqueVals(",int1,",",int2,") returns:", sep="")
			
	if int1 >= 0:
			
		#2nd param of random.sample() function is length of list, which is int1
		#syntax of sample: random.sample(sequence, lengthList)
		result = random.sample(sequence, int1)

		return result 

	elif int1 < 0:

		reenter_int1 = \
		print("First argument ","(", int1, ")", " is negative. Re-enter first argument and make sure it is greater than or equal to zero, since the first argument is equal to the desired length of the returned list.", sep="")

		return reenter_int1


print(uniqueVals(5,10))
print("\n")
print(uniqueVals(0,0))
print("\n")
print(uniqueVals(-1,10)) #elif int1 < 0, error case if int1 (argument #1) is < 0, bc length must be >= 0
print("\n")
print(uniqueVals(2,2))
print("\n")
print(uniqueVals(5,3))
print("\n")
print(uniqueVals(1,-10)) #when argument #2 is negative, original solution does not hold, i.e. where first param/starting point of range() of sequence == 0
print("\n")
print(uniqueVals(23,-17)) 
print("\n")
print(uniqueVals(7,-1700)) 
