#Quadratic.py
#The program should prompt the user for the
#coefficients a,b,c of a quadratic function. The program should then calculate and display the roots of the
#function using the quadratic formula.
import math

exit = 'n'

while (exit != 'y' and exit != 'Y'): 
	a = input("What is the coefficent of a\n")
	while True:
			try:
				floatA = float(a)
				break
			except ValueError:
				print("That's not a valid number")
				a = input("What is the coefficent of a\n")
				
	b = input("What is the coefficent of b\n")
	while True:
			try:
				floatB = float(b)
				break
			except ValueError:
				print("That's not a valid number")
				b = input("What is the coefficent of b\n")
				
	c = input("What is the coefficent of c\n")
	while True:
			try:
				floatC = float(c)
				break
			except ValueError:
				print("That's not a valid number")
				c = input("What is the coefficent of c\n")
	
	#If the discriminant is positive or zero
	if ((floatB*floatB)-4*floatA*floatC) >= 0: 
		#If denominator is zero
		if(floatA == 0):
			if (-floatB + math.sqrt((floatB*floatB)-4*floatA*floatC)) == 0:
				print("The root for this function is: 0.")
			elif (-floatB - math.sqrt((floatB*floatB)-4*floatA*floatC)) == 0:
				print("The root for this function is: 0.")
			else:
				print("There are no real roots")
		#If denominator in nonzero
		else:
			root1 = (-floatB + math.sqrt((floatB*floatB)-4*floatA*floatC))/ (2*floatA)
			root2 = (-floatB - math.sqrt((floatB*floatB)-4*floatA*floatC))/ (2*floatA)
			print("The roots for this function are: " + str(root1) + " and  " + str(root2) + ".")
	#If the discriminant is negative
	else:
		print("There are no real roots")
	
	exit = input("Would you like to exit the program?(Press 'Y' for yes or 'N' for no)\n")
	while (exit != 'Y' and exit != 'y' and exit != 'n' and exit != 'N'):
		print("Please type in a valid input")
		exit = input("Would you like exit the program?(Press 'Y' for yes or 'N' for no)\n")