MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

MachineOn = True
TotalMoneyGotten = 0


def make_the_coffee(sz_type):
    print(f"your order is {sz_type}.")
    sufficient = check_the_coffee_ingredient(sz_type)
    if not sufficient[0]:
        print(f"Sorry there is not enough {sufficient[1]}.")


def show_ingredients_amount():
    print(f"""
    water: {resources["water"]}
    milk: {resources["milk"]}
    coffee: {resources["coffee"]}
    money: {TotalMoneyGotten}
    """)


def check_the_coffee_ingredient(sz_type):
    if resources["water"] < MENU[sz_type]["ingredients"]["water"]:
        return [False, "water"]
    if resources["milk"] < MENU[sz_type]["ingredients"]["milk"]:
        return [False, "milk"]
    if resources["coffee"] < MENU[sz_type]["ingredients"]["coffee"]:
        return [False, "coffee"]
    return [True, ""]


while MachineOn:
    UserAnswer = input("What would you like? (espresso/latte/cappuccino): ")
    if UserAnswer == "report":
        show_ingredients_amount()
    elif UserAnswer == "off":
        print("Turn off the machine!!")
        MachineOn = False
    elif UserAnswer == "espresso" or UserAnswer == "latte" or UserAnswer == "cappuccino":
        make_the_coffee(UserAnswer)
