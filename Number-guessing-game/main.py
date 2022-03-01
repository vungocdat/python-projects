# Number Guessing Game
# Player will choose easy (10 lives) or hard (5 lives) mode
# based on the mode chosen you have a certain number of attempts
# to guess the Number

import random
from os import system
import art


# set the number of attemps based on difficulty 5 or 10. -1 for invalid input
def set_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if mode == 'easy':
        return 10
    elif mode == 'hard':
        return 5
    else:
        return -1


# compares user's number and the searched number
def check_guess(a_guess, guessing_number):
    if a_guess > guessing_number:
        return "Too high.\n"
    elif a_guess == guessing_number:
        return "win"
    else:
        return "Too low\n"


# generate a random number and the player needs to guess that
def game():
    system('clear')
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    the_number = random.randint(1, 100)

    # create a variable called attemps
    attempts = set_difficulty()
    while attempts < 0:
        print("Invalid command!")
        attempts = set_difficulty()

    # take user input to make comparison with generated number
    winner = False
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess a number.")
        guess = int(input("Make a guess: "))
        result = check_guess(guess, the_number)
        if result == 'win':
            print(art.win)
            print(f"You got it! The answer was {the_number}.\n")
            winner = True
            attempts = 0
        else:
            print(result)
            attempts -= 1

    if not winner:
        print(art.lose)
        print(f"You've run out of guesses, you lose. The number was {the_number}.")


# play game by calling game function
game()

# after the game finishes ask if the player wants to play again
play_again_check = True
while play_again_check:
    play_again = input("Do you want to play again? 'y' or 'n': ")
    if play_again == 'y':
        play_again_check = False
        game()
    elif play_again == 'n':
        play_again_check = False
        print("Thank you for playing Number Guessing Game! Bye!")
