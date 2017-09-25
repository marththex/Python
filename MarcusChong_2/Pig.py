#Pig.py
#plays the game of Pig where one player is human and the other is
#the computer.

import random

print("--------------------------------------")
print("WELCOME TO THE GAME OF PIG")
print("--------------------------------------\n")

my_score = 0
cpu_score = 0
score = 0
roll = 0
cpu_roll = 0

while my_score < 100 and cpu_score < 100:
#Your Turn
	while roll != 1:
		#If previous roll is 1
		if roll == 0:
			roll = 1
		print("--------------------------------------")
		print("YOUR SCORE: " + str(my_score) + " POINTS")
		print("CPU SCORE: " + str(cpu_score) + " POINTS")
		print("PREVIOUS ROLL: " + str(roll))
		print("--------------------------------------\n")
		answer = input("Press 'r' to roll or 'h' to hold: ")
		if answer == 'r' or answer == 'R':
			roll = random.randint(1,6)
			if roll == 1:
				score = 0
			elif roll == 2:
				score += 2
			elif roll == 3:
				score += 3
			elif roll == 4:
				score += 4
			elif roll == 5:
				score += 5
			else:
				score += 6
		elif answer == 'h' or answer == 'H':
			my_score += score
			break
		else:
			print("\nERROR: PLEASE TYPE IN A VALID INPUT")
			
#Reset score and roll		
	score = 0
	if roll == 1:
		roll = 0
	
	
#CPU Turn
	while cpu_roll != 1 and score <= 20:
		cpu_roll = random.randint(1,6)
		if cpu_roll == 1:
			score = 0
		elif cpu_roll == 2:
			score += 2
		elif cpu_roll == 3:
			score += 3
		elif cpu_roll == 4:
			score += 4
		elif cpu_roll == 5:
			cpu_roll += 5
		else:
			cpu_roll += 6
	cpu_score += score
	
	#Reset score and roll			
	score = 0
	if cpu_roll == 1:
		cpu_roll = 0
		
if my_score > cpu_score:
	print("YOU WIN")
else:
	print("YOU LOSE")
