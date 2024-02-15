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


def define_the_coffee_type(sz_type):
    coffee_type = ""
    if sz_type == "espresso":
        coffee_type = "espresso"
    elif sz_type == "latte":
        coffee_type = "latte"
    elif sz_type == "cappuccino":
        coffee_type = "cappuccino"
    elif sz_type == "off":
        print("Turn off the machine!!")
        return
    print(f"your order is {coffee_type}.")


CoffeeType = input("Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ")
define_the_coffee_type(CoffeeType)
