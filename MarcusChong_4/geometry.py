#geometry.py
#compute the area of a circle, the
#circumference of a circle, the volume of a sphere, and the volume of a cylinder given
#proper inputs. 

import math

#Functions
def area(radius):
	return math.pi*radius*radius
	
def circumference(radius):
	return 2*math.pi*radius
	
def volumeSphere(radius):
	return (4/3)*math.pi*radius*radius*radius
	
def volumeCylinder(radius, height):
	return math.pi*radius*radius*height
	
#Test Code
a = input("Type in the radius of the circle and I will give you the area.\n")
float_a = float(a)
a = float_a
print(area(a))

c = input("Type in the radius of the circle and I will give you the circumference.\n")
float_c = float(c)
c = float_c
print(circumference(c))

vS = input("Type in the radius of the sphere and I will give you the volume.\n")
float_vS = float(vS)
vS = float_vS
print(volumeSphere(vS))

vCr = input("Lastly, I will give you the volume of the cylinder.\nType in the radius of the cylinder.")
vCh = input("Type in the height of the cylinder.")
float_vCr = float(vCr)
vCr = float_vCr
float_vCh = float(vCh)
vCh = float_vCh
print(volumeCylinder(vCr,vCh))

print("DONE!")
	