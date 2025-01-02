Menu={
    "Latte":{
        "Ingredients":{
            "Water":200,
            "Milk":150,
            "Coffee":24,
        },
        "Cost":150
    },
    "Espresso":{
        "Ingredients":{
            "Water":50,
            "Coffee":18,
        },
        "Cost":100,
    },
    "Cappuccino":{
        "Ingredients":{
            "Water":250,
            "Milk":100,
            "Coffee":24,
        },
        "Cost":200,
    }
}
Profit=0
resources={
    "Water":500,
    "Milk":200,
    "Coffee":100,
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert Coins...")
    total=0
    coins_five=int(input("How many 5rs coin?:"))
    coins_ten=int(input("How many 10rs coin?:"))
    coins_twenty=int(input("How many 20rs coin?:"))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total
def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global Profit
        Profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your Rs {change} in change...")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]=coffee_ingredients[item]
    print(f"Here is your {coffee_name}.. Enjoy!!")
is_on=True
while is_on:
    choice=input("What would you like to have? (Latte/Espresso/Cappuccino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water={resources ['Water']}ml")
        print(f"Milk={resources ['Milk']}ml")
        print(f"Coffee={resources ['Coffee']}g")
        print(f"Money=Rs {Profit}")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['Ingredients']):
            payment=process_coins()
            if is_payment_successful(payment,coffee_type['Cost']):
                make_coffee(choice,coffee_type['Ingredients'])


