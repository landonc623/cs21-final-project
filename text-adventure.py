# Landon Cayia and Taylor French
# CS 21 Final Project
# This is a simple, short text adventure game that the user navigates using menu options.


# Startup function is the first function to run when the game starts. (Landon)
def startup():
    print('Welcome to Game Name!')
    print('Created by Landon Cayia and Taylor French')
    selection = menu()
    if selection == '1':
        storyline(1)
    elif selection == '2':
        storyline(2)
    elif selection == '3':
        storyline(3)
    elif selection == '4':
        print('Thank you for playing!')


# Menu function will allow the player to select a menu option when they start the game. (Landon)
def menu():
    print('1: New Game')
    print('2: Enter Code')
    print('3: Credits')
    print('4: Exit')
    selection = input('Select an option: ')
    return selection

# Code function will allow the player to enter a code to advance to a certain point in the game (given by the game
# for easy access when a certain portion of the game has already been completed.
def code():
    codes = {
        ""
    } # This dictionary will contain the preset codes to advance to a certain point in the game.


def storyline(option):
    if option == '2':
        progress = code()