import random
from functions import *
import player
import time
import setup
def lucks():
    if player.rod == "starter":   
        rodluck = 1
    elif player.rod == "basic":   
        rodluck = 2
    elif player.rod == "intermediate":   
        rodluck = 5
    elif player.rod == "pro":   
        rodluck = 10

    if player.reel == "starter":   
        reelluck = 1
    elif player.reel == "basic":   
        reelluck = 2
    elif player.reel == "intermediate":   
        reelluck = 5
    elif player.reel == "pro":   
        reelluck = 10

    if player.boat != False: boatluck = 5
    else: boatluck = 0

    totalluck = rodluck + reelluck + boatluck
    return totalluck



def addfish(fish):
    if fish == "bream": 
        player.bream += 1
    if fish == "flathead": 
        player.flathead += 1
    if fish == "whiting": 
        player.whiting += 1
    if fish == "bass": 
        player.bass += 1


def fish():
    global in_location
    global totalluck
    if player.rod == "starter":   
        rodluck = 1
    elif player.rod == "basic":   
        rodluck = 2
    elif player.rod == "intermediate":   
        rodluck = 5
    elif player.rod == "pro":   
        rodluck = 10

    if player.reel == "starter":   
        reelluck = 1
    elif player.reel == "basic":   
        reelluck = 2
    elif player.reel == "intermediate":   
        reelluck = 5
    elif player.reel == "pro":   
        reelluck = 10

    if player.boat != False: boatluck = 5
    else: boatluck = 0

    totalluck = rodluck + reelluck + boatluck
    player.rod = player.rod
    if in_location == False: 
        location = random.choice(player.locations).title()
        write(f"Going to {location}")
        write("Setting up gear...", 0.1)
        setup.setup()
        input("Press enter to start fishing!")
    else: 
        setup.bait()
    for i in range(1): 
      write("Cast!", newline=False)
      input()
      clear()   
    for i in range(random.randint(15, 25) - int((totalluck / 2))): 
      input("Jig")
      clear()   
    cfish = random.choice(player.fishes)
    write(f"You just hooked onto a {cfish}!", 0.03)
    for i in range(random.randint(15, 25) - int((totalluck / 2))): 
        write("Reel it in!", newline=False)
        input()
    clear()
    got = [True, False, False, False, False]
    for i in range(int(totalluck / 2)): 
        got.append(True)
    gotc = random.choice(got)
    if gotc == True:
        write("You got it!")
        if cfish == "toadfish":
            write("You need to release it...", 0.03)
        else: 
            addfish(cfish) 
            write("You now have: ")
            showfish()
    elif gotc == False:
        write(f"The {cfish} got away...", 0.1)
    time.sleep(0.9)
    after()

def after():
    global in_location
    again = input("Cast again?(y/n) ")

    if again.lower() == "y":
        in_location = True
        fish()
    elif again.lower() =="n":
        write("Going back home", newline=False)
        write("...", 0.5)
    elif again.lower() =="":
        after() 
    else: 
        print("Please enter a valid option")
        after()
    save_game()

