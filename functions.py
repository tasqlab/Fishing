import sys
import time
import os
import json
import player
import math

def write(text, delay=0.01, newline=True):
    text = str(text)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def sep(len=60):
    for i in range(len - 1):
        print("=", end="")
    print("=")

def dct(dct):
    for item, amount in dct.items(): 
        print("{} ({})".format(item, amount))
def dct_price(dct):
    for item, amount in dct.items():
        print("{} ${}".format(item, amount).title())

def save_game():
    update_totalfish()
    data = {
        "money": player.money,
        "bream": player.bream,
        "flathead": player.flathead,
        "whiting": player.whiting,
        "bass": player.bass,
        "totalfish": player.totalfish,
        "rod" : player.rod,
        "reel": player.reel,
        "baits": player.baits,
        "lures": player.lures,
        "sinkers": player.sinkers,
        "bobbers": player.bobbers,
        "hooks": player.hooks,
        "name": player.name
    }
    with open("savefile.json", "w") as f:
        json.dump(data, f)
    print("Game saved!")

def load_game():
    try:
        with open("savefile.json", "r") as f:
            data = json.load(f)
            player.money = data.get("money", 0)
            player.bream = data.get("bream", 0)
            player.flathead = data.get("flathead", 0)
            player.whiting = data.get("whiting", 0)
            player.bass = data.get("bass", 0)
            player.totalfish = data.get("totalfish", 0)
            player.rod = data.get("rod", "starter")
            player.reel = data.get("reel", "starter")
            player.baits = data.get("baits", player.baits)
            player.lures = data.get("lures", player.lures)
            player.hooks = data.get("hooks", 10)
            player.bobbers = data.get("bobbers", 10)
            player.sinkers = data.get("sinkers", 10)
            player.name = data.get("name", "User")
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
        print("What is your name?")
        player.name = input("> ").title()
        player.money = 50
        player.bream = 0
        player.flathead = 0
        player.whiting = 0
        player.bass = 0
        player.totalfish = 0

def update_totalfish():
    player.totalfish = player.flathead + player.bream + player.whiting + player.bass

def showfish(text="======================="):
    print(f"{player.flathead} fleathead")
    print(f"{player.bream} bream")
    print(f"{player.whiting} whiting")
    print(f"{player.bass} bass")
    print(text)
