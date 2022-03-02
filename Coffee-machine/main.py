# Coffee machine
# user insert coins and choose what kind of coffee to make
# coffee machine has limited resources. if resources are not enough the machine returns the coins
# each kind of coffee requires different amount of resources

# when resources are full (water and milk in ml, coffee in g)

MAX_WATER = 300
MAX_MILK = 200
MAX_COFFEE = 100

resources = {
    "water": MAX_WATER,
    "milk": MAX_MILK,
    "coffee": MAX_COFFEE
}

# Money the coffee machine made so far
money = 0

# menu will be static that ( data will not change)
MENU = {
    "espresso": {
        "materials": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.5
    },
    "latte": {
        "materials": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "price": 2.5
    },
    "cappuccino": {
        "materials": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "price": 3.0
    }
}


# get_order will get input from the user
def get_order():
    return input("What would you like? 'espresso', 'latte', 'cappuccino'\n")


# show resources
def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g\n")


# refill resources to its max capacity
def refill_resources():
    print("Refilling . . .")
    resources["water"] = MAX_WATER
    resources["milk"] = MAX_MILK
    resources["coffee"] = MAX_COFFEE
    print("Done!\n")


# check if there is enough resources
# if there is enough resources the function returns True, if there is not it then returns False
def enough_resources(drink_material):
    for i in drink_material:
        if drink_material[i] > resources[i]:
            print(f"There is not enough {i}.")
            return False
    return True


# print the price of chosen drink and ask for coins
def insert_coins(drink_name):
    print(f"Your {drink_name} costs ${MENU[drink_name]['price']}")
    print("The machines accepts only coins.")
    total = int(input("How many quarters do you want to insert?: ")) * 0.25
    total += int(input("How many dimes do you want to insert?: ")) * 0.1
    total += int(input("How many nickles do you want to insert?: ")) * 0.05
    total += int(input("How many pennies do you want to insert?: ")) * 0.01
    return total


def process_money(user_payment, drink_cost):
    global money
    money += drink_cost
    change = round(user_payment - drink_cost, 2)
    print(f"Here's your change: ${change}")


def make_coffee(drink_name, drink_material):
    for i in drink_material:
        resources[i] -= drink_material[i]
    print(f"Here is you {drink_name}! Thank you!\n")


# main loop
machine_is_on = True
while machine_is_on:

    # getting user input
    # while loop will ensure that user will give a valid input
    # options:
    #   for user: espresso, latte, cappuccino
    #   maintenance: report, refill, turnoff
    order = get_order()
    valid_order = False
    while not valid_order:
        if order == "espresso" or order == "latte" or order == "cappuccino" or order == "report" or order == "refill" \
                or order == 'turnoff':
            valid_order = True
        else:
            print(f"Invalid input -> {order}")
            order = get_order()

    # execute the command if 'order' variable contains valid string
    if order == "turnoff":
        machine_is_on = False
    elif order == "report":
        print_resources()
        print(f"Total profit: ${money}\n")
    elif order == "refill":
        refill_resources()
        print_resources()
    else:  # user ordered a drink
        drink = MENU[order]
        cost = drink["price"]
        # materials (drink["materials"]) are given to the function
        if enough_resources(drink["materials"]):
            payment = insert_coins(order)
            if payment < cost:
                print("Not enough money. Money refunded.")
            else:
                process_money(payment, cost)
                make_coffee(order, drink["materials"])
