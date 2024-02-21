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
    global resources
    resources["water"] -= MENU[sz_type]["ingredients"]["water"]
    resources["milk"] -= MENU[sz_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[sz_type]["ingredients"]["coffee"]
    print(f"Here is your {sz_type} ☕ Enjoy.")


def show_ingredients_amount():
    print(f"""
    water: {resources["water"]}
    milk: {resources["milk"]}
    coffee: {resources["coffee"]}
    money: ${TotalMoneyGotten}
    """)


def check_the_coffee_ingredient(sz_type):
    if resources["water"] < MENU[sz_type]["ingredients"]["water"]:
        return [False, "water"]
    if resources["milk"] < MENU[sz_type]["ingredients"]["milk"]:
        return [False, "milk"]
    if resources["coffee"] < MENU[sz_type]["ingredients"]["coffee"]:
        return [False, "coffee"]
    return [True, ""]


def do_transaction(coffee_type):
    print("Please insert coins.")
    quarter_number = float(input("How many quarters?: "))
    dime_number = float(input("How many dimes?: "))
    nickel_number = float(input("How many nickel?: "))
    penny_number = float(input("How many pennies?: "))
    total_amount_money = 0.25 * quarter_number + dime_number * 0.1 + nickel_number * 0.05 + penny_number * 0.01
    if MENU[coffee_type]["cost"] > total_amount_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif MENU[coffee_type]["cost"] < total_amount_money:
        refund = total_amount_money - MENU[coffee_type]["cost"]
        print(f"Here is ${round(refund, 2)} dollars in change.”")
    global TotalMoneyGotten
    TotalMoneyGotten += MENU[coffee_type]["cost"]
    return True


while MachineOn:
    UserAnswer = input("What would you like? (espresso/latte/cappuccino): ")
    if UserAnswer == "report":
        show_ingredients_amount()
    elif UserAnswer == "off":
        print("Turn off the machine!!")
        MachineOn = False
    elif UserAnswer == "espresso" or UserAnswer == "latte" or UserAnswer == "cappuccino":
        sufficient = check_the_coffee_ingredient(UserAnswer)
        if not sufficient[0]:
            print(f"Sorry there is not enough {sufficient[1]}.")
            continue
        isEnoughMoney = do_transaction(UserAnswer)
        if not isEnoughMoney:
            continue
        make_the_coffee(UserAnswer)
