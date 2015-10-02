import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)  # Generate a random integer between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:   # Count the number of guesses they take to get there
	print('Take a guess.') # There are four spaces in front of print.
	guess = input()
	try:
		guess = int(guess)
	except ValueError:    # Try not to crash when given invalid inputs
		print("Invalid input.")
		continue;
		
	guessesTaken = guessesTaken + 1

	if guess < number:
		print('Your guess is too low.') # There are eight spaces in front of print.
	elif guess > number:
		print('Your guess is too high.')
	elif guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
else guess != number:
	number = str(number)
	print('Nope. The number I was thinking of was ' + number)
