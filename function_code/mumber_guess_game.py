'''
PYTHON LAB: number_guess-game.py.py

Write a Python program that will :
Guess the correct number enter by a user in 5 guesses. If you don’t get it right after 5 guesses you lose the game.
Give user input box: 1. To capture guesses, he /she will choose number between 1 to 50.
print message to tell user if guess is too high/low ,and let them know the rest of guesses remaining.
print(and input boxes)  If user wins  or If user loses
'''
import random

def guess_game():
    # Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)
    
    # Initialize the number of guesses
    guesses_remaining = 5
    
    # Loop for 5 guesses
    for i in range(5):
        # Get user's guess
        guess = int(input("Guess a number between 1 and 50: "))
        
        # Check if guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly.")
            return
        # Give hint if guess is too high or low
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        # Decrement the number of guesses remaining
        guesses_remaining -= 1
        print(f"You have {guesses_remaining} guesses remaining.")
    
    # If user loses
    print(f"Sorry, you lost. The secret number was {secret_number}.")

# Call the function
guess_game()

##################################################################################################
def get_guess(guess_number):
    """Get the user's guess and ensure it's within the valid range."""
    guess = int(input(f'Guess # {guess_number + 1}: Choose a number between 1-50: '))
    while guess < 1 or guess > 50:
        print('Sorry, the number you entered is out of the range! Please try again: ')
        guess = int(input(f'Guess # {guess_number + 1}: Choose a number between 1-50: '))
    return guess

def check_guess(guess, num):
    """Check the guess against the correct number."""
    if guess < num:
        print(f'Your guess {guess} is not the right number and is too low')
        return False
    elif guess > num:
        print(f'Your guess {guess} is not the right number and is too high')
        return False
    else:
        print(f'You Win! You Guessed it: {guess}, which is the correct number!')
        return True

def play_guessing_game():
    """Main function to run the guessing game."""
    num = 21
    guess_limit = 5
    guess_number = 0
    win = False

    while guess_number < guess_limit:
        guess = get_guess(guess_number)
        win = check_guess(guess, num)
        if win:
            break
        else:
            print(f'You have {guess_limit - guess_number - 1} guesses left! Please try again!')
        guess_number += 1

    if not win:
        print(f'Sorry, that was your last guess, and you lose! The correct answer was {num}')

# Run the game
play_guessing_game()
