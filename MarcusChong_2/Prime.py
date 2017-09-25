#Prime.py
#prompts the user for two integers, a and b, and outputs whether
#or not a and b are relatively prime. 

a = input("Type in an interger for a: \n")
b = input("Type in an interger for b: \n")

int_a = int(a)
int_b = int(b)
int_t = 0
gcd = 0

#Euclid's Method (Great Common Divisor)
while  int_b != 0:
	int_t = int_a
	int_a = int_b
	int_b = int_t % int_b

gcd= int_a

if(gcd == 1):
	print(a + " and " + b + " are relatively prime.")
	
else:
	print(a + " and " + b + " are not relatively prime.")