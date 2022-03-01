# Higher lower game
# player will choose which of two has higher followers on instagram
# for correct answer: +1 point
# for wrong answer the game ends and shows the total score

import art
import random

from os import system
from data import data

#print(data[1]['name'])
#data_length = len(data) - 1

#take a dictionary and converts values into a comma-separated string (follower_count excluded)
def convert_to_string(dictionary):
    a_list = []
    for i in dictionary:
        # the key follower count is an INT plus it is a secret so it must be left out
        if i != "follower_count":
            a_list.append(dictionary[i])
    string =", ".join(a_list)
    return string

# initialization
game_is_on = True
score = 0
# select a dictionary from the list then cinvert it into a comma-separated string
data_a = random.choice(data)
while game_is_on:
    compare_a = convert_to_string(data_a)

    data_b = random.choice(data)
    while data_b == data_a:
        data_b = random.choice(data)
    compare_b = convert_to_string(data_b)

    # if A has more followers, the variable will be set to True
    a_more_followers = False
    if data_a["follower_count"] > data_b["follower_count"]:
        a_more_followers = True
    system('clear')
    print(art.logo)
    print(f"Your score: {score}")
    print(f"Compare A: {compare_a}.")
    print(art.vs)
    print(f"Against B: {compare_b}.")
    
    #check for valid input
    valid_input = False
    while not valid_input:
        action = input("Who has more followers on Instagram? Type 'a' or 'b': ")
        if action == 'a' or action == 'b':
            valid_input = True

    if a_more_followers and action == 'a':
        score += 1
    elif not a_more_followers and action == 'b':
        data_a = data_b
        score += 1
    else:
        game_is_on = False

# eng game
system('clear')
print(art.game_over)
print(f"Your total score: {score}.")
print("\nThank you! Bye :)")
