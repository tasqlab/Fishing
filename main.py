import player
import random
import time
import go_fishing
import os
from sell_fish import *
from functions import *
import shop


go_fishing.in_location = bool(False)
def menu():
    load_game()
    save_game()
    clear()
    print("Welcome to fishing game")
    print("==================================")
    print(f"Name: {player.name}")
    print(f"Money: {player.money}")
    print(f"Total fish: {player.totalfish}")
    print(f"Rod: {player.rod}")
    print(f"Reel: {player.reel}")
    print(f"Boat: {player.boat}")
    print("==================================")
    print("What would you like to do?")
    print("1) Go fishing")
    print("2) Sell fish")
    print("3) Buy gear")
    print("4) Check Inventory")
    print("q) exit")

    option = (input("> "))
    if option == "1": 
        clear()
        go_fishing.in_location = False
        go_fishing.fish()
        menu()

    elif option == "2": 
        clear()
        showsell()
        menu()
        
    elif option == "3": 
        write("Going to BCF...", 0.05)
        clear() 
        shop.main()
        clear() 
        menu()

    elif option == "4": 
        clear()
        player.inv()
        menu()

    elif option ==  "q": 
        save_game()
        quit()

load_game()
menu()

