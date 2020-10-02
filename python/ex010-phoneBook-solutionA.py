# 10.01.20 
# Exercise 10 - solution A
# Write a function called phoneBook that given two parameters, 
#the first being an array of hashes containing n number of 
#names and phone numbers and the second being an array of friends names 
#will then will assemble a phone book that maps the 'friends' array of 
#names to their respective phone numbers if they are found in the first array. 
#Each found entry will print the associated entry from your phone book 
#on a new line in the form name=phoneNumber; if an entry is not found, 
#print Not found instead.

#Input 1: [{'sam':99912222},{'tom':11122222},{'harry':12299933}]
#Input 2: ['sam','ed','harry']

#Output:
#sam=99912222
#NOT FOUND
#harry=12299933

def phoneBook(param1, param2):


	#for each string in input2,
	for nameEntry in param2:

		found = False
		
		for i in range(len(param1)):
			
			if nameEntry in param1[i].keys():
				

				print(nameEntry, '=', param1[i][nameEntry], sep='')

				found = True
				break 

		if found == False:
			print('NOT FOUND')


phoneBook([{'sam':99912222, 'Jenny':8675309},{'tom':11122222},{'harry':12299933}], ['sam','ed','harry'])
