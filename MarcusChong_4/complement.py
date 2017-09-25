#complement.py
#Write a module, complement.py, with a function, complement, that returns the
#complement of a DNA string. Also provide a function, revComplement that takes a
#DNA sequence as string input and returns the reverse complement of the sequence as a
#string. Recall that the valid alphabet is {A,C,T,G} and that A-T and G-C are
#complements. A reverse complement is found by reversing the input string and replacing
#every nucleotide with its complement. This means that your revComplement method
#should use your complement method internally rather than duplicating code. Your
#methods should do appropriate error checking and return an error message as appropriate.
#Test your functions with input from the user.

def complement(dna):
	comp = ""
	for x in dna:
		if x == "A" or x == "a":
			comp += "T"
		elif x == "C" or x == "c":
			comp += "G"
		elif x == "T" or x == "t":
			comp += "A"
		elif x == "G" or x == "g":
			comp += "C" 
		else:
			return "Error: NOT A VALID DNA STRING"
	return comp
			
			

def reverseComplement(dna):
	revdna = ""
	revcomp = ""
	dnaLength = len(dna)
	#Reverses the DNA string
	while dnaLength > 0:
		revdna += dna[dnaLength-1]
		dnaLength-= 1
	return complement(revdna)
	
testComp = input("Type in a DNA string and I will give you its complement.\n")
print(complement(testComp))
testRevComp = input("Type in a DNA string and I will give you its reverse complement.\n")
print(reverseComplement(testRevComp))

	