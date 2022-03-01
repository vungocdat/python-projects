# Simplified BlackJack game
# A is replaced with 11 and J, Q, K in replaced with 10

import random
from art import logo
from os import system

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card

def score(list_of_cards):
    # if 2 cards are 11 and 10/J/Q/K then it is a win
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    #if there is a A in the list then the value of an A is changed to 1
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)

def comparison(player_score, pc_score):
    if player_score == pc_score:
        return "It's a draw."
    elif player_score == 0:
        return "You've got a Blackjack. You win!"
    elif pc_score == 0:
        return "Pc's got a Blackjack. You lose!"
    elif player_score > 21:
        return "You lose! You went over."
    elif pc_score > 21:
        return "You win! PC went over."
    elif player_score > pc_score:
        return "You win!"
    else:
        return "You lose!"
def game():
    game = True
    player_cards = []
    pc_cards = []

    print(logo)

    for i in range(2):
        player_cards.append(deal_card())
    pc_cards.append(deal_card())

    while game:
        player_score = score(player_cards)
        pc_score = score(pc_cards)
        print(f"\nPlayer's cards: {player_cards}. Player's score: {player_score}.")
        print(f"PC card: {pc_cards}. PC's score: {pc_score}.")

        if player_score == 0 or player_score > 21 or pc_score == 0:
            game = False
        else:
            keep_playing = input("Do you want to draw another card? 'y'or 'n': ")
            if keep_playing == 'y':
                player_cards.append(deal_card())
            elif keep_playing == 'n':
                game = False

    while pc_score != 0 and pc_score < 17:
        pc_cards.append(deal_card())
        pc_score = score(pc_cards)

    print(f"\nPlayer's cards: {player_cards}. Player's score: {player_score}.")
    print(f"PC card: {pc_cards}. PC's score: {pc_score}.")
    print(comparison(player_score, pc_score))

while input("Do you want to play Blackjack? 'y' or 'n': ") == 'y':
    system('clear')
    game()
