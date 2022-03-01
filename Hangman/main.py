# Hangman project
#
# Player will guess a word. if the word is guessed right the player wins
# otherwise the player loses.

import random
import hangman_art as art
import hangman_words as words
import os

# Step 1 - create a word list and generate a random word from the list
random_word = words.word_list[random.randint(0, len(words.word_list) - 1)].lower()
# Step 1.1 - create a list of "_" for the random word
guess_word = []
for letter in random_word:
    guess_word.append("_")

# Step 2 - player guesses a word. Make the guess lowercase
# Step 3 - loop through the word and see if the guess match any of the letter
# an replace it (using range function)
# Step 4 - make while loop to be able to play. End the game if the word is
# guessed (my solution was to set count to the length of the word and decrese
# the count when it is guessed till it reaches 0)

# Step 5 ASCII art and set up lifes
life = 6

# Step 6 - remake while loop to include life count
# Step 7 - declare an empty string and concatenate it with guess_word
# Step 8 - create modules for asci art and words
# Step 9 - upgrade user experience: banner, show guessed letters, clear screen
# after every answer

game_is_on = True
word = " "
tries = ""

os.system('clear')
print(art.logo)
while game_is_on:
    print(art.stages[life])
    print(f"{word.join(guess_word)}\n")
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    tries += guess + " "
    print(art.logo)
    print(f"\nYou guessed: {tries}")
    if guess in random_word:
        for position in range(len(random_word)):
            if guess == random_word[position]:
                guess_word[position] = guess
    else:
        life -= 1
    if "_" not in guess_word:
        print(art.stages[life])
        game_is_on = False
        print(f"{word.join(guess_word)}")
        print("You have won!")
    elif life == 0:
        print(art.stages[life])
        game_is_on = False
        print(f"{word.join(guess_word)}")
        print("You have lost!")
        print(f"The word was: {random_word}")
