# Calculator
# Take 2 number from the input and make a operation
# based on the operator
# this project is made to practice return statement and dictionary

from art import logo
from os import system

#add
def add(num1, num2):
    return num1 + num2

#subtrack
def subtrack(num1, num2):
    return num1 - num2

#multiplication
def multi(num1, num2):
    return num1 * num2

#division
def div(num1, num2):
    return num1 / num2

# a dictionary with functions as values
operations = {
    "+": add,
    "-": subtrack,
    "*": multi,
    "/": div
}


def calculator():
    print(logo)
    
    num1 = float(input("Enter a number: "))
    
    while True:
        for i in operations:
            print(i)
        operator = input("Enter the operation: ")
        num2 = float(input("Enter a number: "))

        function = operations[operator]
        result = function(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")

        if input("Type 'y' to continue with {result} else the calculator resets. ") == 'y':
            num1 = result
        else:
            system('clear')
            calculator()

calculator()

