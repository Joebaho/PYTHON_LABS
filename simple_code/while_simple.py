# Guess the correct number in 5 guesses. If you don’t get it right after 5 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-50, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# ALWAYS ASK YOURSELF THESE THREE QUESTIONS WHILE WORKING WITH LOOPS Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 

num = 21
guess = 0
guess_limit=5
guess_number = 0

while guess_number < guess_limit:
    guess = int(input(f'Guess # {guess_number+1}: Choose a number between 1-50:   '))
    if guess <1 or guess >50:
        print('Sorry the number you enter is out of the range! Please try again: ')
    elif guess != num and guess < num:
        print(f'Your guess {guess} is not the right number, and is too low')
        print(f'You have {guess_limit-guess_number-1} guesses left! Please try again!')
    elif guess != num and guess > num:
        print(f'Your guess {guess} is not the right number, and is too high')
        print(f'You have {guess_limit-guess_number-1} guesses left! Please try again')
    elif guess == num:
        print(f'You Win! You Guessed it: {guess} which the correct number!')
        break
    else:
        print(f'Sorry you lose! It was {num}')
    guess_number += 1
if guess != num:
    print(f'Sorry, That was your last guess, and you lose! It was {num} the correct answer')
