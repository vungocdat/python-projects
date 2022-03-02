# Coffee machine implemented as OOP
# everything (classes) is preset the code I made starts from line 8

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1) print out the report

# create a coffee maker and money machine object to ger reports (for ingredients and profit)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# 2) check if the resourcer are sufficient
# 3) process payment - add profit
# 4) make a coffee - make coffee from resources

# coffee_maker.is_resource_sufficient method takes MenuItem object as input
# menu.find_drink method takes string as input and returns MenuItem object
menu = Menu()

machine_working = True
while machine_working:
    print(f"Options: {menu.get_items()}")
    order = input("What would you like? ")
    if order == 'off':
        machine = False
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
        print("\n")
    else:
        drink = menu.find_drink(order)
        # 2) check for resources and # 3) process payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # 4) make coffee from resources
            coffee_maker.make_coffee(drink)
