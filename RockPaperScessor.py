import random

compterChoice = random.choice(['Rock','Paper','Scessor'])

userChoice= input('Enter your Choice - (Rock/Paper/Scessor)\n')

if compterChoice == userChoice:
    print('its a Tie')
elif userChoice == 'Rock' and compterChoice == 'Scessor':
    print('You Win' + ' Computer had a ' + compterChoice)
elif userChoice == 'Scessor' and compterChoice == 'Paper':
    print('You Win' + ' Computer had a ' + compterChoice)
elif userChoice == 'Paper' and compterChoice == 'Rock':
    print('You Win' + ' Computer had a ' + compterChoice) 
else:
    print('You Loose :( computer wins :)' + ' Computer had a ' + compterChoice)               