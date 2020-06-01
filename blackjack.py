import random

def drawCard():
    randNum = random.randint (2,11)
    print ("You drew a " + str(randNum))
    return randNum
score = 0
while True:
    answer = input("Do you want to draw a card? Y/N ")
    if answer == "Y":
        randomNum = drawCard()
        score += randomNum
        print ("Your updated score is " + str(score))
    elif score > 21:
        print ("You bust!")
    else:
        print("You're done")
        break
