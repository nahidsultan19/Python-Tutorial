secret_word = 10
guess = ''
guess_count = 0
guess_limit = 5
out_of_guess = False

while guess != secret_word and not(out_of_guess):
	if guess_count < guess_limit:
		guess = int(input('Enter your guess: '))
		guess_count +=1
	else:
		out_of_guess = True

if out_of_guess:
	print('Sorry, You are lose!')
else:
	print('You Win!')