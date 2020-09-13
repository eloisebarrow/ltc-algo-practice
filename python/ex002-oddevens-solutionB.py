# 09.13.20 sjg - solution B
#Write a function called oddsEvens that given a string, prints its
#even-indexed and odd-indexed characters as space-separated strings on a
#single line.

#Input: Hacker 
#Output: Hce akr 

def oddEvens(stringInput):
 
	evenChars = ''
	oddChars = ''


	for index in range(len(stringInput)):

		if index % 2 == 0:

			evenChars = evenChars + stringInput[index]

		else: 
			
			oddChars = oddChars + stringInput[index]

	print(evenChars, oddChars, sep=' ')


oddEvens('Hacker')