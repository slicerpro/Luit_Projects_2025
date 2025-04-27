import random

roll = random.randint(1,6)

guess = int(input("guess the dice roll:\n"))
if guess == roll:
    print("Correct!, they rolled a " + str(roll))
else:
    print("Incorrect!, they rolled a " + str(roll))