"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number. If dice roll is equal to 2
or 7 player receive a 10 mon bonus.  
''')

purse = 5000

while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        """
        Changed input to include initials.
        """
        pot = input('JM: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 =random.randint(1, 6)
    dice2 =random.randint(1, 6)
    """
    Added this code to check if special rule was working.
    """
    #Use these to check bonus working correctly make sure they are commented out when not testing.
    #dice1 = 1
    #dice2 = 1

    #dice1 = 2
    #dice2 = 5


    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        """
        Changed input to include initials.
        """
        bet = input('JM: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot from player's purse.
        """
        Original code calculating 10% house fee.
        """
        #print('The house collects a', pot // 10, 'mon fee.')
        #purse = purse - (pot // 10)  # The house fee is 10%.
        """
        Changed code to calculate the 12% fee. Introduced the fee variable to calculate
        the new percentage fee from purse total.
        """
        
        fee = int(pot*0.12)  # The house fee is 12%.
        print('The house collects a', fee, 'mon fee.')
        purse -= fee  
        """
        Add special rule for dice outputs of 2 and 7.
        """
        #If dice total is 2 or 7 display 10 mon bonus message.
        if (dice1 + dice2) in (2,7):
            print(f'The total roll is equal to {dice1+dice2}. You receive a 10 mon bonus!')
            purse +=10
    
        
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
