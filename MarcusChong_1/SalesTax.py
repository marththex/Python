#SalesTax.py
#The program should prompt the user for the purchase price of an item 
#and the sales tax rate. It should then display the total price of the item.
import sys
exit = 'n'

while (exit != 'y' and exit != 'Y'):
	price = input("What is the purchase price of the item? \n")
	while True:
		try:
			floatPrice = float(price)
			#If price is positive
			if floatPrice > 0:
				break
			#If price is not positive
			else: 
				print("Please type in a value greater than zero.")
				price = input("What is the purchase price of the item? \n")
		except ValueError:
			print("That's not a valid number")
			price = input("What is the purchase price of the item? \n")
	
	sales_tax = input("What is the sales tax rate? (e.g. .157 for 15.7%) \n")
	while True:	
		try:
			floatsales_tax = float(sales_tax)
			#If tax rate is positive
			if floatsales_tax > 0:
				break
			#If tax rate is not positive
			else:
				print("Please type in a value greater than zero.")
				sales_tax = input("What is the sales tax rate? (e.g. .157 for 15.7%) \n")
		except ValueError:
			print("That's not a valid number")
			sales_tax = input("What is the sales tax rate? (e.g. .157 for 15.7%) \n")

	total = floatPrice*(1+floatsales_tax) #Calulates the total price

	print("The total price of the item is: " + str(total))
	exit = input("Would you like to exit the program?(Press 'Y' for yes or 'N' for no)\n")
	while (exit != 'Y' and exit != 'y' and exit != 'n' and exit != 'N'):
		print("Please type in a valid input")
		exit = input("Would you like exit the program?(Press 'Y' for yes or 'N' for no)\n")
				