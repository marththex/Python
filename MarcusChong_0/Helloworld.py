import sys

x = input("What is the Radius of the Circle: ")
try:
	floatX = float(x)
except ValueError:
	print("That's not a valid number")
	sys.exit()

while(floatX < 0.0):
	print("Error: Please type in a valid number")
	x = input()
	floatX = float(x)
	
cirX = float(2*3.14*floatX)
areaX = float(3.14*floatX*floatX)
print("Circumference: ")
print(cirX)
print("Area: ")
print(areaX)

