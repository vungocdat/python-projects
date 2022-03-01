# Password Generator Project
# The program will generate a random password on how many letters, numbers and
# symbols the user wants.
# The generator will print 2 passwords
#   1) simple - in this order: letters - symbols - numbers
#   2) More complex: takes the simple version and shuffles it to make it more
#   random

import random

#lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#taking input from the iser
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#define an empty string for the password
password = ""


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for letter in range(0, nr_letters):
  password = password + random.choice(letters)

for symbol in range(0, nr_symbols):
  password = password + random.choice(symbols)

for number in range(0, nr_numbers):
  password = password + random.choice(numbers)

print(f"\nSimple:\n{password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#split char of password into a list, shuffle and concatenate
password_list = list(password)
random.shuffle(password_list)
result = "".join(password_list)
print(f"\nMore complex:\n{result}")


