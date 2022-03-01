# The program will take an year from the input and decide if it is a leap year
# or not

# on every year that is evenly divisible by 4
# EXCEPT every year that is evenly divisible by 100
# UNLESS the year is also evenly divisible by 400

print("Leap year or not?")
year = int(input("Select the year: "))

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    elif year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")
