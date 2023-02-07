
# MITT FÖRSTA FÖRSÖK (efter mycket googlande och felsökande).
import random

playerChoice = input("Rock, paper, scissors, GO!\n")
print("You chose" + " " + playerChoice)

options = ["rock", "paper", "scissors"]

npcChoice = random.choice(options)
 
print("The computer chose" + " " + npcChoice)


if playerChoice.lower() == "rock" and npcChoice == "paper" :
    print("Rock vs Paper! Computer wins!")
elif playerChoice.lower() == "rock" and npcChoice == "scissors" :
    print("Rock vs Scissors! Player wins")
elif playerChoice.lower() == "scissors" and npcChoice == "paper" : 
    print("Scissors vs Paper! Player wins!")
elif playerChoice.lower() == "scissors" and npcChoice == "rock" : 
    print("Scissors vs Rock! Computer wins!")
elif playerChoice.lower() == "paper" and npcChoice == "rock" :
    print("Paper vs Rock! Player wins")
elif playerChoice.lower() == "paper" and npcChoice == "scissors" :
    print("Paper vs Scissors! Computer wins")
else :
    print("There was a tie. Try again!")

#print("Output: " + playerChoice + " | " + npcChoice)
