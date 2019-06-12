import random

print('')
userInput = input('Do you want to roll the dice? ')

if userInput == 'y' or userInput == 'Y':
    print('')
    
    # Get a number from 0 to 6
    diceNumber = int(((random.random() * 2)/3) * 10)
    
    # If it is 0 convert it to 1
    if diceNumber == 0:
        diceNumber = diceNumber + 1
    
    # Get ascii dice image
    path = '/Users/smilyan.pavlov/Projects/Personal/Python/codeup/ascii/%d.txt' % diceNumber
    diceImage = open(path).read()

    # Print dice image
    print(diceImage)
    print('')

else:
    
    print('')
    print('************')
    print('Game over!')
    print('************')
    print('')