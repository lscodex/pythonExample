# -*- coding: utf-8 -*-
import sys

# quit programs 
def quit():
	choice = raw_input('Press "q" to quit: ')
	if choice == 'q':
		sys.exit(0)
	else:
		catchPrimeNumber()




def isPrimeNumber(primeNum):
	if primeNum > 1:   #  must greater than one
		if(primeNum==2):
			print(primeNum,"This number is not prime number!")
			return False
		for i in range(2,primeNum):   # a range of entered value
			if (primeNum % i) == 0: # equl to zero 
				print(primeNum,"this number is not prime number!")
				return False
			else:
				print(primeNum,"Yep, it is prime number")
				return True
	else:
		print(primeNum," Sorry that but you entered 1! ")
		return True

def catchPrimeNumber():
	primeNum = int(raw_input("Please, enter to number: \n"))  # waiting user to enter number
	isPrimeNumber(primeNum) # called function
	for i in range(2,primeNum + 1): # show the prime numbers up to the user's numbers.
		for j in  range (2,i):
			if(i % j) == 0:
				break
 			else:
				print(i)
				break
	quit()

catchPrimeNumber()

