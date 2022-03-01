# Maze
# 
# Simple text game where you choose an action in order to get out of the maze
# before the monster who is chasing you catch you.
#
# The code is not ideal. It is written mainly to practice if-statement and
# nested ifs


print('''
\                           /
 \                         /
  \                       /
   ]                     [    ,'|
   ]                     [   /  |
   ]___               ___[ ,'   |
   ]  ]\             /[  [ |:   |
   ]  ] \           / [  [ |:   |
   ]  ]  ]         [  [  [ |:   |
   ]  ]  ]__     __[  [  [ |:   |
   ]  ]  ] ]\ _ /[ [  [  [ |:   |
   ]  ]  ] ] (#) [ [  [  [ :===='
   ]  ]  ]_].nHn.[_[  [  [
   ]  ]  ]  HHHHH. [  [  [
   ]  ] /   `HH("N  \ [  [
   ]__]/     HHH  "  \[__[
   ]         NNN         [
   ]         N/"         [
   ]         N H         [
  /          N            \ 
 /           q,            \ 
/                           \ 
''')

print("\nMAZE\n\n")

print("You are in the maze running from the monster which is right behind you.")
action = input('The path splits in 2. Will you choose "left" or "right?" -> ').lower()
if action == "right":
  print("\nIt is a dead end. The monster caught you. Game over.")

elif action == "left":
  print('\nThere is a hole in front of you what will you do?')
  action = input('You can: "jump" "go around" -> ').lower()
  if action == "jump":
    print("\nYou didn't jump high enough and fell into the hole. Game over.")
  elif action == "go around":
    print("\nYou go around the hole and you see 2 buttons (red, blue) and a door. One button will open it.")
    action = input('Which one will you push? "red" "blue"? -> ').lower()
    if action == "blue":
      print("\nThe door remained closed and the monster caught you. Game over.")
    elif action == "red":
      print("\nYou pushed the red button. The door opened and you continue to run.")
      print("You stand in front of final door that requires to solve a puzzle in order to open it.")
      print("Solve this: 2 + 2 * 2 + 2 / 2")
      action = int(input("Your answer is: "))
      # If player type text instead of number -> error and the game ends
      if action != 7:
        print("\nWrong answer. The door remaind closed. The monster caught you. Game over.")
      else:
        print('''
  _______
 |       |
(|  YOU  |)
 |  WIN  |
  \     /
   `---'
   _|_|_
        ''')
        print("\nYou opened the last door and escaped from the maze and the monster! You have won! Congratulations!")
    else:
      print("\nInvalid command. The mosnter caught you. Game over.")
  else:
    print("\nInvalid command. The mosnter caught you. Game over.")
else:
  # In case the user insert invalid command the game ends.
  print("\nInvalid command. The mosnter caught you. Game over.")
