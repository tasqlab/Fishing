from functions import *

#the user data
name = " "
money = 50
flathead = 0
bream = 0
whiting = 0
bass = 0
toadfish = 0
fishes = ["flathead", "bream", "whiting", "bass"]
totalfish = flathead + bream + whiting + bass

locations = [
    "botany bay",
    "brays bay reserve",
    "hawkesbury river",
    "narrabeen lake",
    "bobbin head"
]

# tackle
boat = False
sinkers = 10
bobbers = 10
hooks = 10

baits = {
    "pilchard": 0,
    "prawn": 20,
    "corn": 40,
    "worm": 10
}

lures = {
    "soft body": 10,
    "hard body": 2,
    "topwater": 0,
    "spinner": 4
}

rod = "starter"
reel = "starter"

def inv():
    sep()
    print("You have: ")
    showfish("==================================")
    print(f"Total fish: {player.totalfish}")
    print(f"{player.rod.title()} rod")
    print(f"{player.reel.title()} reel")
    dct(player.baits)
    dct(player.lures)
    print(f"Hooks: {player.hooks}")
    print(f"Sinkers: {player.sinkers}")
    print(f"Bobbers: {player.bobbers}")
    print(f"Boat: {player.boat}")
    sep()
    input("Press enter to continue")