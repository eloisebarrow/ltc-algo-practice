# 09.13.20 sjg - solution A
#Write a function called oddsEvens that given a string, prints its
#even-indexed and odd-indexed characters as space-separated strings on a
#single line.

#Input: Hacker 
#Output: Hce akr


def oddEvens(stringInput):

	even_indexed_chars = stringInput[::2]

	odd_indexed_chars = stringInput[1::2]


	print(even_indexed_chars, odd_indexed_chars, sep=' ')


oddEvens('Hacker')