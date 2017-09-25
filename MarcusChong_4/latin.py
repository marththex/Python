#latin.py
#Write a module, latin.py, with a function nameToPig, that takes 2 input parameters,
#firstName and lastName, and returns the names in pig Latin as a list.

def nameToPig(firstName, lastName):
	#Reverses first name
	revFirstName = firstName[::-1]

	#Reverses last name
	revLastName  = lastName[::-1]	
	
	return revFirstName + "ay " + revLastName + "ay"

fName = input("Please type in your first name:\n")
lName = input("Please type in your last name:\n")

print(nameToPig(fName, lName))
	