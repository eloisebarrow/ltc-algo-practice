# 09.21.20 - sjg
# Exercise 8 
# Write a function called likes which takes in an array, 
#containing the names of people who like an item. It must return 
#the display text as shown in the examples and 
#is dependent on the number of elements in the array.

#Input: likes([])
#Output: "no one likes this"

#Input: likes(["Peter"])
#Output: "Peter likes this"

#Input: likes(["Jacob", "Alex"])
#Output: "Jacob and Alex like this"

#Input: likes(["Max", "John", "Mark"])
#Output: "Max, John and Mark like this"

#Input: likes(["Alex", "Jacob", "Mark", "Max"])
#Output: "Alex, Jacob and 2 others like this"

def likes(listInput):

	# 0 people, if length == 0 
	if len(listInput) == 0:
		return "no one likes this"

	# 1 people
	elif len(listInput) == 1:
		return  listInput[0] + " likes this"

	# 2 people
	elif len(listInput) == 2:
		return listInput[0] + " and " + listInput[1] + " like this"

	# 3 people
	elif len(listInput) == 3:
		return listInput[0] + ", " + listInput[1] + " and " + listInput[2] + " like this"

	# 4+ people
	else: 

		others_int_to_str = str(len(listInput[2:]))

		return listInput[0] + ", " + listInput[1] + " and " + others_int_to_str + " others like this"


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))