# Coffee machine code

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
    "money": 0
}


def start():
    machine_state = True
    while machine_state:
        sufficient_resources = True
        choice = input("What would you like? (espresso, latte, cappuccino): ")
        if choice == "report":
            print(f"""
            Water: {resources['water']}ml
            Milk: {resources['milk']}ml
            Coffee: {resources['coffee']}g
            Money: ${resources['money']}
            """)
        elif choice == "off":
            print("Taking Machine down for maintainence")
            machine_state = False
        elif choice in MENU:
            beverage = MENU[choice]
            for ingredient in beverage["ingredients"]:
                if beverage["ingredients"][ingredient] > resources[ingredient]:
                    print(f"Not enough {ingredient}\n")
                    sufficient_resources = False
            if sufficient_resources:
                print("\nPlease insert some coins")
                coins = {
                    "quarters" : 0.25,
                    "dimes" : 0.10,
                    "nickels": 0.05,
                    "pennies": 0.01
                }
                money_in = 0
                enough_money = True
                for coin in coins:
                    money_in += coins[coin] * int(input(f"How many {coin}? "))
                if money_in >= MENU[choice]["cost"]:
                    if money_in > MENU[choice]["cost"]: 
                        print(f"Here's your ${money_in - MENU[choice]['cost']} in change")
                else:
                    print("Not enough money!")
                    enough_money = False
                if enough_money:
                    resources["money"] += MENU[choice]["cost"]
                    for ingredient in beverage["ingredients"]:
                        resources[ingredient] -= beverage["ingredients"][ingredient]
                    print(f"\nHere is your {choice} ☕ Enjoy!\n")
        else:
            print("Doesn't exist in the menu, yet")


start()