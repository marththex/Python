import statistics

#define variables
value = 0
total = 0
num_list = []

#Prompts the user for positive integer values and stores them in a list (Stops after a negative interger input)
while value >= 0:
	
	try:
		value = input("Type in a positive integer value to add to the list \nor a negative interger to end the list:\n")
		int_value = int(value)
		value = int_value	
		if value < 0:
			#Checks to see if there is at least 2 values to compute the average and the standard deviation
			if len(num_list) < 2:
				value = 0
				print("Error: There needs to be at least two values in the list \nto computer the average and the standard deviation\n")
			else:
				break
		else:
			num_list.append(value)
	except ValueError:
				print("That's not a valid input\n")
				value = 0
		
#Sorts and prints list in order 
sorted_list = sorted(num_list)
print("List of sorted positive intergers in the list:")
for x in sorted_list:
	print(x)
	total += x #Computes total to calculate the mean

#Compute and print the mean
list_length = len(sorted_list)
mu = total/list_length
print("Average: " + str(mu))

#Compute and print the standard deviation
stdev = statistics.stdev(sorted_list)
print("Standard Deviation: " + str(stdev))

