# 09.17.20 - sjg 
# Exercise 6
# Write a function called printArr that will print the items of an array.

#Input: ['sally','monique','caleb']
#Output: 

#sally
#monique
#caleb

def printArr(arrayInput):


	import numpy as np

	arr = np.array(arrayInput)


	for i in arr:

		print(i, end="\n")


	return arr


printArr(['sally','monique','caleb'])
print('\n')

#WHO IS SHE
#name that song!
printArr(['monica','erica','rita','tina','sandra','mary','jessica','you'])