#temp.py
#Write a module, temp.py, with two functions, fahrenheitToCelsius and
#celsiusToFahrenheit, each of which take a numeric value representing a
#Fahrenheit/Celsius temperature and return the appropriate conversion. Test your
#functions with input from the user and display the results to the console.

def fahrenheitToCelsius(degreeF):
	return (degreeF-32)/(9.0/5.0)

def celsiusToFahrenheit(degreeC):
	return (9.0/5.0)*degreeC+32
	
f = input("Type in a temperture in Fahreheit and I will convert it to Celsius.\n")
floatf = float(f)
f = floatf
print(str(fahrenheitToCelsius(f)) + " Degrees Celsius")

c = input("Type in a temperture in Celsius and I will convert it to Fahreheit.\n")
floatc = float(c)
c = floatc
print(str(celsiusToFahrenheit(c)) + " Degrees Fahreheit")

