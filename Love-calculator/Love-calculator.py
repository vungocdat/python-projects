# LOVE CALCULATOR
#
# Take both people's names and check for the number of times the letters in the
# word TRUE occurs. It will form the first digit
#
# Then check for the number of times the letters in the word LOVE occurs. It
# will form the second digit

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


true_counter = 0
love_counter = 0;

# Combine string then put them into lower case
combine_string = name1 + name2
lower_case_string = combine_string.lower()

# Count TRUE letters in the string
true_counter += lower_case_string.count("t") + lower_case_string.count("r") + lower_case_string.count("u") + lower_case_string.count("e")

# Count LOVE letters in the string
love_counter += lower_case_string.count("l") + lower_case_string.count("o") + lower_case_string.count("v") + lower_case_string.count("e")

# combine true and love digits and change data type into INT
score_string = str(true_counter) + str(love_counter)
score = int(score_string)

# output the results
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
