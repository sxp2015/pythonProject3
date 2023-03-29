import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == (1 if guess == 'heads' else 'tails'):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == ('heads' if guess == '1' else 'tails'):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
