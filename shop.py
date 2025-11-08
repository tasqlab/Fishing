import random
from functions import *
import player

#prices
hook_price = 0.20
sinker_price = 0.20
bobber_price = 0.50

avi_baits = {
    "pilchard": 1,
    "prawn": 0.1,
    "corn": 0.05,
    "worm": 0.05,
}
avi_lures = {
    "soft body": 2,
    "hard body": 15,
    "topwater": 10,
    "spinner": 1,
}

avi_rods = {
    "basic": 20,
    "intermediate": 100,
    "pro": 200
}
avi_reels = {
    "basic": 20,
    "intermediate": 100,
    "pro": 200
}
avi_combos = {
    "basic": 30,
    "intermediate": 150,
    "pro": 300
}

avi_boats = {
    "inflatable kayak": 100,
    "decent boat": 1000,
    "fishing boat": 10000
}

#code
def main():
    options()

def list():
    save_game()
    clear()
    print("What would you like to buy?")
    print(f"You have ${player.money}")
    print("1) Baits")
    print("2) Lures")
    print("3) Rods, reels and combos")
    print("4) Boats")
    print("5) Sinkers and hooks")
    print("6) Bobbers")
    print("q) Back")

def options():
    list()
    option = input("> ")
    if option == "1": 
        write('Heading to Tweed Baits section')
        baits()
    elif option == "2": 
        write('Finding lures section')  
        lures()
    elif option == "3": 
        write('Going to rods, reels and combos')
        rrc()
    elif option == "4": 
        write('Checking out boats') 
        boats()
    elif option == "5": 
        sh()
    elif option == "6":   
        bob()
    elif option == "q": 
        write('Going back home...', 0.05)
    else:
        print("Please enter a valid option")
        time.sleep(1)
        options()

def baits(): 
    global avi_baits
    dct_price(avi_baits)
    print("What would you like to get?")
    choice = input("> ").lower()
    amount = int(input("How many? "))
    if "pil" in choice: 
        buylure("bait", "pilchard", avi_baits.get("pilchard"), amount)
        list()
    if "pra" in choice: 
        buylure("bait", "prawn", avi_baits.get("prawn"), amount)
        list()
    if "co" in choice: 
        buylure("bait", "corn", avi_baits.get("corn"), amount)
        list()
    if "wo" in choice: 
        buylure("bait", "worm", avi_baits.get("worm"), amount)
        list()
    if choice == "q":
        list()

def buylure(type, item, price, amount):
    price = float(price)
    if player.money < price:
        print("Not enough money!")
        return

    tprice = amount * price
    player.money = player.money - tprice

    if type == "bait":
        player.baits[item] = player.baits.get(item, 0) + amount
        print(f"You now have {player.baits[item]} of {item}")
        print(f"and have ${player.money}")
        input("Press enter to continue")
    elif type == "lure":
        player.lures[item] = player.lures.get(item, 0) + amount
        print(f"You now have {player.lures[item]} of {item}")
        print(f"and have ${player.money}")
        input("Press enter to continue")
    else:
        print("error")
    save_game()
    list()

def lures():
    global avi_lures
    dct_price(avi_lures)
    print("What would you like to get?")
    choice = input("> ").lower()
    amount = int(input("How many? "))
    if "sof" in choice: 
        buylure("lure", "soft body", avi_lures.get("soft body"), amount)
        list()
    if "har" in choice: 
        buylure("lure", "hard body", avi_lures.get("hard body"), amount)
        list()
    if "to" in choice: 
        buylure("lure", "topwater", avi_lures.get("topwater"), amount)
        list()
    if "sp" in choice: 
        buylure("lure", "spinner", avi_lures.get("spinner"), amount)
        list()
    if choice == "q":
        list()

def rrc():
    print(f"Your rod: {player.rod}")
    print(f"Your reel: {player.reel}")
    sep()
    print("Rods: ")
    dct_price(avi_rods)
    sep()
    print("Reels: ")
    dct_price(avi_reels)
    sep()
    print("Combos: ")
    dct_price(avi_combos)
    sep()
    print("What would you like to get?")
    rrc_choice()
    
def rrc_choice():
    choice = input("> ")
    if "rod" in choice.lower(): 
        rods()
    if "reel" in choice.lower(): 
        reels()
    if "combo" in choice.lower(): 
        combos()
    else:
        rrc_choice()

def boats():
    dct_price(avi_boats)
    print("What would you like to get?")
    choice = input("> ")


def rods():
    choice = input("Which rod?  ")
    if "bas" in choice and player.money > 19: 
        print("You chose basic rod and bought it for $20")
        player.money -= 20
        player.rod = "basic"
        write(f"You now have ${player.money} and a {player.rod} rod.", 0.03)
        input(" ")
        list()
    elif "int" in choice and player.money > 99: 
        print("You chose intermediate rod and bought it for $100")
        player.money -= 100
        player.rod = "intermediate"
        write(f"You now have ${player.money} and a {player.rod} rod.", 0.03)
        input(" ")
        list()
    elif "pr" in choice and player.money > 199: 
        print("You chose pro rod and bought it for $200")
        player.money -= 200
        player.rod = "pro"
        write(f"You now have ${player.money} and a {player.rod} rod.", 0.03)
        input(" ")
        list()
    else:
        print("You do not have enough money")
        list()

def reels():
    choice = input("Which reel?  ")
    if "bas" in choice and player.money > 19: 
        print("You chose basic reel and bought it for $20")
        player.money -= 20
        player.reel = "basic"
        write(f"You now have ${player.money} and a {player.reel} reel.", 0.03)
        input(" ")
        list()
    elif "int" in choice and player.money > 99: 
        print("You chose intermediate reel and bought it for $100")
        player.money -= 100
        player.reel = "intermediate"
        write(f"You now have ${player.money} and a {player.reel} reel.", 0.03)
        input(" ")
        list()
    elif "pr" in choice and player.money > 199: 
        print("You chose pro reel and bought it for $200")
        player.money -= 200
        player.reel = "pro"
        write(f"You now have ${player.money} and a {player.reel} reel.", 0.03)
    else:
        print("You do not have enough money")
        input(" ")
        list()

def combos():
    choice = input("Which combo?  ")
    if "bas" in choice and player.money > 30: 
        print("You chose basic combo and bought it for $30")
        player.money -= 30
        player.combo = "basic"
        write(f"You now have ${player.money} and a {player.combo} combo.", 0.03)
        input(" ")
        list()
    elif "int" in choice and player.money > 149: 
        print("You chose intermediate combo and bought it for $149")
        player.money -= 149
        player.combo = "intermediate"
        write(f"You now have ${player.money} and a {player.combo} combo.", 0.03)
        input(" ")
        list()
    elif "pr" in choice and player.money > 300: 
        print("You chose pro combo and bought it for $300")
        player.money -= 300
        player.combo = "pro"
        write(f"You now have ${player.money} and a {player.combo} combo.", 0.03)
        input(" ")
        list()
    else:
        print("You do not have enough money")
        time.sleep(1)
        input(" ")
        list()

def sh():
    print("Do you want to...  ")
    print("1) Buy sinkers")
    print("2) Buy hooks")
    print("3) Buy both")
    print("q) Go back")
    shi()

def shi():
    option = input("> ")
    if option == "1":
        count = int(input("How much? "))
        sprice = sinker_price * count
        if player.money > sprice:
            write(f"Buying {count} sinkers for {sprice}")
            player.money -= sprice
            player.sinkers += count
            print(f"You now have {player.sinkers} sinkers")
            print(f"and {player.money}")
            input(" ")
            list()
        else:
            print("Insufficient funds")
            sh()
    if option == "2":
        count = int(input("How much? "))
        hprice = hook_price * count
        if player.money > hprice: 
            write(f"Buying {count} hooks for {hprice}")
            player.money -= hprice
            player.hooks += count
            print(f"You now have {player.hooks} hooks")
            print(f"and {player.money}")
            input(" ")
            list()
        else:
            print("Insufficient funds")
            sh()
    if option == "3":
        count = int(input("How much? "))
        price = (hook_price + sinker_price) * count
        if player.money > price: 
            write(f"Buying {count} hooks and sinkers for {price}")
            player.money -= price
            player.hooks += count
            player.sinkers += count
            input(" ")
            list()
        else:
            print("Insufficient funds")
            sh()
    if option == "q":
        list()
    else:
        shi()
    save_game()

def bob():
    global bobber_price
    count = input('How much? Enter "q" to go back. ')
    if count == "q": 
        list()
    else:
        count = int(count)
        price = bobber_price * count
        if player.money > price: 
            write(f"Buying {count} bobbers for {price}...")
            player.money -= price
            player.bobbers += count
            print(f"- {price}")
            write(f"You now have {player.bobbers} bobbers and ${player.money}")
            input(" ")
            list()
        else:
            print("Insufficient funds")
            bob()




def getprice(type, item):
    if type.lower() == "bait":
        return avi_baits.get(item)
    if type.lower() == "lure":
        return avi_lures.get(item)


## tests
# user.money = 300
# buylure("bait", "prawn", getprice("bait", "prawn"))
# x = getprice("bait", "pilchards")
# print(x)