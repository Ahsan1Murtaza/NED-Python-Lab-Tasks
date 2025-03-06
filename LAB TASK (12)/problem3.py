# Q.3 Define two lists dice1 and dice2, holding numbers from 1 to 6 ,Design a python program  that start playing with two dices for two players.
from random import *

dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]

while True:
    player1_first=choice(dice1)
    player1_second=choice(dice2)

    player2_first=choice(dice1)
    player2_second=choice(dice2)

    print(f"Player One {player1_first},{player1_second}")
    print(f"Player Two {player2_first},{player2_second}")

    n=input("Do you want again? (yes)").lower()
    if n!="yes":
        break
