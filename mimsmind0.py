import random

def mimsmind(length):
	#generating default value if length is not given
	if length == 0 or type(length) != int: 
		length = 1

	#setting ranges for random number generation
	range_start = 10**(abs(length-1)) 
	range_end = 10**(length)

	#generate random number and length based on ranges
	randomnumber = random.randint(range_start, range_end) 
	numberlength = len(str(randomnumber)) #

	#initialize guesses counter
	guesses = 0 

	#Game Start
	print("Let's play the mimsmind0 game.\n")
	user_guess = input("Guess a {}-digit number: ".format(numberlength))
	
	while True:
		try:
			int(user_guess)
		except:
			user_guess = input("Invalid input. Try again: ")
			continue
		if len(str(user_guess)) != numberlength:
			user_guess = input("Invalid input. Try again: ")
			continue

		user_guess = int(user_guess)
		if user_guess < randomnumber: 
			guesses += 1
			user_guess = input("Try again.  Guess a higher number: ")
		elif user_guess > randomnumber:
			guesses += 1
			user_guess = input("Try again.  Guess a lower number: ")
		elif user_guess == randomnumber:
			guesses += 1
			print("Congratulations.  You guessed the correct number in {} tries".format(guesses))
			break

##############################################################################
def main():
   mimsmind(0)

if __name__ == '__main__':
    main()
