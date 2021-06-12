import random

roll = random.randint(1,6)

userGuess = int(input('Enter you guess'))

if userGuess == roll:
    print('Guessed it correctly')
else:
    print('Wrong Guess buddy ' + ' ,it was a ' + str(roll) )    
