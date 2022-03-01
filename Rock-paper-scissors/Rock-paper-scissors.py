# Rock, paper scissors game.
#
# rock beats scissors
# scissors beat paper
# paper beats rock


import random




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.")

my_choice = int(input())
if my_choice < 0 or my_choice > 2:
  print("Invalid option. You lose")
else:
  pc_choice = random.randint(0, 2)

# rock = 0, paper = 1, scissors = 2
  choice = [rock, paper, scissors]
  print(choice[my_choice])
  print(f"Computer chose:\n{choice[pc_choice]}")

  if pc_choice > my_choice:
    if pc_choice == 2 and my_choice == 0:
      print("You win")
    else:
      print("You lose")
  elif pc_choice == my_choice:
    print("It's a draw")
  else:
    if my_choice == 2 and pc_choice == 0:
      print("You lose")
    else:
      print("You win")

# decision tree
# Code 1st attemtp
## if player choose rock
#if my_choice == 0:
#  if pc_choice == 0:
#    print("It's a draw")
#  elif pc_choice == 1:
#    print("You lose")
#  elif pc_choice == 2:
#    print("You win")
#
## if player choose paper
#if my_choice == 1:
#  if pc_choice == 1:
#    print("It's a draw")
#  elif pc_choice == 2:
#    print("You lose")
#  elif pc_choice == 0:
#    print("You win")
#
## if player choose scissors
#if my_choice == 2:
#  if pc_choice == 2:
#    print("It's a draw")
#  elif pc_choice == 0:
#    print("You lose")
#  elif pc_choice == 1:
#    print("You win")
