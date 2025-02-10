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

def report(resources,Money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${Money}")

def sufficiency(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

switchoff = False
Money = 0
enoughResources = True

while not switchoff:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            report(resources,Money)
        elif choice == "off":
            switchoff = True
            # break      to break from this loop
            exit()
        else:
            enoughResources = sufficiency(MENU[choice]["ingredients"])
            if enoughResources:
                print("Please insert coins.")
                Amount = 0
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                Amount = round(quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01,2)
                if Amount < MENU[choice]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    Money += MENU[choice]["cost"]
                    print(f"Here is your {choice}. Enjoy!")
                    change = round(Amount - MENU[choice]["cost"],2)
                    if change > 0:
                        print(f"Here is ${change} dollars in change.")
                    for item in MENU[choice]["ingredients"]:
                        resources[item] -= MENU[choice]["ingredients"][item]


