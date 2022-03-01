# Blind auction
# take bidders names and theirs prices from the input then show the highest
# bidder name and his / her price

from art import logo
from os import system

#creating empty dictionary
auction = {}

def add_bidder(specified_dictionary):
    name = input("Bidder's name: ")
    price = int(input(f"{name}'s bid: $"))
    specified_dictionary[name] = price


print(logo)
add_bidder(auction)

#add another bidder
end = False
while not end:
    another_bidder = input("\nAre there any other bidders? Type 'yes' or 'no'\n").lower()
    if another_bidder == "yes":
        system('clear')
        print(logo)
        add_bidder(auction)
    elif another_bidder == "no":
        end = True
        #returns key (name) with highest value
        highest_bidder = max(auction, key=auction.get)
        highest_price = auction[highest_bidder]
        system('clear')
        print(f"The winner is {highest_bidder} who bidded ${highest_price}.")
    else:
        print(f"{another_bidder} is an invalid command.")

