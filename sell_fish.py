import player
from functions import *
import random
from go_fishing import showfish

flathead_price = 0
bream_price = 0
whiting_price = 0
bass_price = 0

def showsell():
    global choice
    clear()
    print("You have: ")
    showfish("==================================")
    print("Options: ")
    print("1) Sell all flathead")
    print("2) Sell all bream")
    print("3) Sell all whiting")
    print("4) Sell all bass")
    print("q) Go back")
    print("Enter your choice")
    prices()
    choice = input("> ")
    choices()

def prices():
    global flathead_price, bream_price, whiting_price, bass_price
    flathead_price = random.randint(25, 35)
    bream_price = random.randint(10, 20)
    whiting_price = random.randint(10, 20)
    bass_price = random.randint(10, 20)

def choices():
    global choice
    if choice == "1":
        sellfish("flathead")
    elif choice == "2":
        sellfish("bream")
    elif choice == "3":
        sellfish("whiting")
    elif choice == "4":
        sellfish("bass")
    elif choice == "q": 
        write("Going back", newline=False)
        write("...", 0.5)
    else: 
        write("Please enter a valid option")
        showsell()
        choices()
    update_totalfish()
    save_game()

def sellfish(fish_type):
    global flathead_price, bream_price, whiting_price, bass_price

    price_map = {
        "flathead": flathead_price,
        "bream": bream_price,
        "whiting": whiting_price,
        "bass": bass_price
    }

    amount = getattr(player, fish_type)
    fish_price = price_map.get(fish_type, 0)

    if not hasattr(player, "money"):
        player.money = 0

    player.money += fish_price * amount
    setattr(player, fish_type, 0)
    time.sleep(1.0)
    write(f"Sold {amount} {fish_type} for ${fish_price * amount}. Total money: ${player.money}")
    input("Press enter to continue")
    showsell()
    save_game()

