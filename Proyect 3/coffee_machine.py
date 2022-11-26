import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    for i in resources:
        print(f"{i} : {resources[i]}")
    print(f"Total profit: {earned_money}")


def check_resources(coffee):
    if MENU[coffee]["ingredients"]["water"] > resources["water"]:
        return True
    elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        return True
    if coffee != 'espresso':
        if MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            return True


def check_money(coffee):
    global earned_money
    quarters = float(input("Quarters: ")) * 0.25
    dimes = float(input("Dimes: ")) * 0.1
    nickles = float(input("Nickles ")) * 0.05
    pennies = float(input("Pennies: ")) * 0.1
    money = quarters + dimes + nickles + pennies
    if money < MENU[coffee]["cost"]:
        return True
    if money > MENU[coffee]["cost"]:
        money -= MENU[coffee]["cost"]
        print(f"Your change is: {round(money, 3)}")
        earned_money += MENU[coffee]["cost"]
    elif money == MENU[coffee]["cost"]:
        earned_money += MENU[coffee]["cost"]


def reduce_resources(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    if coffee != 'espresso':
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]


def prepare_coffee(coffee):
    if coffee != "espresso" and coffee != "latte" and coffee != "cappuccino":
        print("Invalid option, try again!")
        return None
    if check_resources(coffee):
        print("Sorry, there's no enough resources to prepare your coffee")
        return None
    if check_money(coffee):
        print("Sorry, it's not enough money")
        return None
    reduce_resources(coffee)
    print(f"Here's your {coffee}, enjoy!")


earned_money = 0
while True:
    os.system("CLS")
    option = input("What would you like to drink? espresso/latte/cappuccino: ")
    if option == 'off':
        exit()
    elif option == 'report':
        report()
    else:
        prepare_coffee(option)
    os.system("PAUSE")
