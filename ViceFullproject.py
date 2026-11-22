money = 60000
garage = []

shop = [
    {"name": "Porsche", "price": 5000},
    {"name": "Audi", "price": 20000},
    {"name": "BMW", "price": 50000},
    {"name": "Lamborghini", "price": 100000}
]

def show_shop():
    print("\n--- CAR SHOP ---")
    n = 1
    for item in shop:
        print(n, ".", item["name"], "- $", item["price"])
        n += 1

def buy_car():
    global money
    show_shop()
    ch = int(input("Choose Car (1-4): "))
    car = shop[ch - 1]
    if money >= car["price"]:
        print("Bought", car["name"])
        money -= car["price"]
        garage.append(car["name"])
    else:
        print("Not Enough Money! Mission Karo!")

def do_mission():
    global money
    print("\n1. Pizza Delivery (+$1000)")
    print("2. Bank Robbery (+$7000)")
    m = int(input("Choose Mission: "))
    if m == 1:
        money += 1000
        print("Pizza Delivered! +$1000")
    elif m == 2:
        money += 7000
        print("Bank Robbed! +$7000")
    print("Money:", money)

def sell_car():
    global money
    if len(garage) == 0:
        print("Garage Khali Hai!")
    else:
        print("Garage:", garage)
        sold = garage.pop(0)
        money += 25000
        print(sold, "Sold! +$25000 Money:", money)

def save_game():
    f = open("vice_save.txt", "w")
    f.write(str(money) + "\n" + str(garage))
    f.close()
    print("Game Saved!")

# MAIN MENU
while True:
    print("\n=== VICE HEARTS ===")
    print("Money:", money, "| Garage:", garage)
    print("1. Car Shop")
    print("2. Mission")
    print("3. Sell Car")
    print("4. Save Game")
    print("5. Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        buy_car()
    elif choice == 2:
        do_mission()
    elif choice == 3:
        sell_car()
    elif choice == 4:
        save_game()
    elif choice == 5:
        print("Bye! VICE HEARTS!")
        break
    else:
        print("Wrong Choice!")