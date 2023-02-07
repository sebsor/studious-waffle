import random

guess = int(input("Guess what number will be rolled \n"))

dice = random.randint(1,9)

if guess == dice :
    print ("You guessed " + str(guess) + " and the computer chose " + str(dice) + ", so you win!")
else :
    print ("You guessed " + str(guess) + " and the computer chose " + str(dice) + ", so you lose!")