import random

def roll_Dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total
def main():
    player1 = input('Enter player One name ')
    player2 = input('Enter player two name ')

    roll1= roll_Dice()
    roll2= roll_Dice()

    print(player1," rolled " ,roll1)
    print(player2," rolled " ,roll2)
    if roll1>roll2:
        print(player1,"win !!")
    elif roll2>roll1:
        print(player2,"Win !!")
    else:
        print('Its tie')

main()
 
