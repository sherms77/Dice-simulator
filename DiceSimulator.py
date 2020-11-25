'''
This is a dice simulator.
The user will be asked if they want to roll the dice or quit the game.
If they choose to roll the dice, a random number between one and six will be produced.
After the number has been produced, the user will be asked if they want to play again or quit.
If the user chooses to quit the game, the program will end.
'''

#colorcodes for color.write from sys mod are in textColorsPyShell.py

import random, sys, time
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

color.write("**********WELCOME TO SHERMAN'S DICE SIMULATOR********** \n", "hit")
color.write("\nYou can roll the dice and a random number between one and six will be produced. \n\n", "KEYWORD")

#MainMenu - Start game
def mainMenu():
    color.write("THIS IS THE MAIN MENU\n", "ERROR")
    userChoice = input('\nWould you like to roll the dice or quit? \nPress y and then enter to roll the dice or, \nPress enter to return to the shell: ')
    if userChoice == 'y':
        diceRoll()
'''
080820: REMOVED THIS FROM MENU. IF YOU PRESS ENTER IT WILL RETURN TO THE SHELL.
    elif userChoice == 'q':
        exit()
'''

#DiceSimulator
def diceRoll():
    print('\nThe dice is rolling, please wait.... \n')
    time.sleep(2)
    print('THE DICE HAS ROLLED AND THE NUMBER IS:\n')
    print("------>", random.randint(1,6), "<------ \n")
    menuTwo() #010820 - I am calling the function menuTwo before it is defined below. Unsure how and why this works.

    #color.write(random.randint(1,6), "\n," "STRING") - 080820: color.write does not work with random.randint
  
def menuTwo():
    color.write("You RoLLed the DiCe! Now ChOoSe aGaIn!\n", "COMMENT")    
    userChoice2 = input('\nWould you like to roll the dice again or quit? \nPress y and then enter to roll the dice again or, \nPress enter to return to the shell: ')
    if userChoice2 == 'y':
        diceRoll()
'''
    elif userChoice2 == 'q':
        exit()
'''

mainMenu()


