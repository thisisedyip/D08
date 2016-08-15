import random

def strings_to_list(test_str):
	test_list = []
	for digit in test_str:
		test_list.append(int(digit))
	return test_list

def all_counter(randomnumber_list, user_guess_list):
	#initializing counters
	bulls = 0
	total_repeats = 0

	#counting bulls
	bulls_list = [i-j for i, j in zip(randomnumber_list, user_guess_list)]
	for each in bulls_list:
		if each == 0:
			bulls += 1

	#counting cows
	for val in randomnumber_list:
		if val in user_guess_list:
			total_repeats += 1
	cows = total_repeats - bulls

	return bulls, cows

def mimsmind(length):
	#generating default value if length is not given
	if length == 0 or type(length) != int: 
		length = 3

	#setting ranges for random number generation
	range_start = int(str(0).zfill(length))
	range_end = 10**(length)-1

	#generate random number and length based on ranges
	randomnumber = random.randint(range_start, range_end) 
	
	#set leadingzeroes for randomnumber
	randomnumber_str = str(randomnumber).zfill(length)
	numberlength = len(randomnumber_str)
	randomnumber_list = strings_to_list(randomnumber_str)

	#initialize counters
	guesses = 0 

	#initialize max rounds:
	max_rounds_value = 2**length + length
	max_rounds = 2**length + length

	#Game Start
	print("Let's play the mimsmind1 game.  You have {} guesses\n".format(max_rounds))
	user_guess_str = (input("Guess a {}-digit number: ".format(numberlength)))
	while True and max_rounds > 0:
		try:
			int(user_guess_str)
		except:
			user_guess_str = input("Invalid input. Try again: ")
			continue
		if len(user_guess_str) != numberlength:
			user_guess_str = input("Invalid input. Try again: ")
			continue
		
		user_guess_list = strings_to_list(user_guess_str)
		if user_guess_str != randomnumber_str:
			guesses += 1
			max_rounds -= 1

			#calculating bulls and cows
			bulls, cows = all_counter(randomnumber_list, user_guess_list)

			#printing result
			user_guess_str = input("{} bull(s), {} cow(s).  Try again: ".format(bulls, cows))
		elif user_guess_str == randomnumber_str:
			guesses += 1
			print("Congratulations.  You guessed the correct number in {} tries".format(guesses))
			break
	if max_rounds == 0:
			print("Sorry.  You did not guess the number in {} tries.  The correct number is {}.".format(max_rounds_value, randomnumber))
		



##############################################################################
def main():
   mimsmind(0)
if __name__ == '__main__':
    main()
