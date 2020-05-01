#LIBRARIES
import random

#VARIABLES
Enemies = 3
Lives = 5
answer = 0
guess = 0

#FUNCTIONS
def livesinfo():
    print("\n\nLives left " + str(Lives) + "\nEnemies left " + str(Enemies) + "\n\n")

def pickBox():
    answer = random.randint(1,3)
    print("[?]  [?]  [?]")
    print("Box1 Box2 Box3")
    print("Pick a Box that you think the enemy is hiding behind")
    print("Enter 1, 2, or 3")
    guess = input()
    while guess < 1 or guess > 3:
        print("Enter 1, 2, or 3")
        guess = input()
    print("Thank you for your selection")
    if guess == answer:
        print("\n\n********You killed an enemy*******\n\n")
        global Enemies 
        Enemies -= 1
    else:
        print("\n\n********Killed by an enemy in Box" + str(answer) + "************")
        global Lives  
        Lives -= 1
        killcam(answer)
    livesinfo()

def killcam(answer):
    if answer == 1: 
        print("[O]  [?]  [?]")
    if answer == 2: 
        print("[?]  [0]  [?]")
    if answer == 3:
        print("[?]  [?]  [0]")
    print("\n")

#PROGRAM FLOW
livesinfo()
while Enemies > 0:
    pickBox()
    if Lives == 0:
        print("GAME OVER")
        exit()
print("***YOU WON***")
