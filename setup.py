import player
from functions import *

def setup():
    global baitchoice
    player.hooks -= 1
    player.sinkers -= 1
    write(f"Attach your {player.rod} rod together", 0.03, newline=False)
    input("")
    write("Tie on the sinker", 0.03, newline=False)
    input("")
    write("Tie on the hook", 0.03, newline=False)
    input("")
    bait()
    bobber()
    show()

def bait(): 
    global baitchoice
    while True:
        clear()
        print("What bait/lure will you use?", 0.03)
        dct(player.baits)
        dct(player.lures)
        baitchoice = input("> ")
        if baitchoice in player.baits: 
            write(f"Hook on the {baitchoice}", 0.03)
            player.baits[baitchoice] -= 1
            break
        elif baitchoice in player.lures: 
            write(f"Hook on the {baitchoice}", 0.03)
            player.lures[baitchoice] -= 1
            break
        else:
            print("Please enter a valid bait/lure", 0.03)
    print("You now have:")
    
def show():
    if baitchoice in player.baits: print(f"{player.baits[baitchoice]} {baitchoice} remaining")
    else: print(f"{player.lures[baitchoice]} {baitchoice} remaining")
    print(f"{player.sinkers} sinkers")
    print(f"{player.hooks} hooks")
    print(f"{player.bobbers} bobbers")

def bobber():
    while True:
        bob = input("Use a bobber? (y/n) ").lower()
        if bob == "y":
            player.bobbers -= 1
            print("Adding bobber...")
            break
        elif bob == "n":
            print("Okay, no bobber this time")
            break
        else: 
            print("Please enter a valid option")

if __name__ == "__main__":
    bobber()
