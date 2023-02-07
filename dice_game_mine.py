import time
import random
def playerNames(a, b) :
    print('Hello', a, 'and', b)

player1 = input('What is your name, player one?\n')
player2 = input('And what is your name, player two?\n')

time.sleep(3)

playerNames(player1, player2)

time.sleep(1)

roll1 = random.randint(1, 6)
print(player1, 'rolled a', roll1)

time.sleep(1)

roll2 = random.randint(1, 6)
print(player2, 'rolled a', roll2)

time.sleep(2)

if roll1 > roll2 :
    print(player1, 'wins!')
elif roll1 < roll2 :
    print(player2, 'wins!')
else :
    print('It was a draw.')