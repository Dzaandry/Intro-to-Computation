k = int(input('Give a number, the program will find its square root'))
guess = k / 2.0
numGuesses = 0
epsilon = 0.01
while abs(guess**2 - k) >= epsilon:
	numGuesses += 1
	guess = guess - (guess**2 - k)/(2*guess)
print('number of guesses:', numGuesses)
print('square root of', k, 'is about', guess)