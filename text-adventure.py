# Landon Cayia and Taylor French
# CS 21 Final Project
# This is a simple, short text adventure game that the user navigates using menu options.


# Startup function is the first function to run when the game starts. (Landon)
def startup():
    print('Prison Escape')
    print('Created by Landon Cayia and Taylor French')
    selection = menu()
    if selection == '1':
        intro(1)
    elif selection == '2':
        print('Thank you for playing!')


# Menu function will allow the player to select a menu option when they start the game. (Landon)
def menu():
    print('1: New Game')
    print('2: Exit')
    selection = input('Select an option: ')
    return selection


# intro function will introduce the player to the game and allow them to choose their stats. (Landon)
def intro(mode):
    if mode == 1:
        player_name = input('Greetings, challenger! What is your name? ')
        print(player_name, ', welcome to Prison Escape!', sep='')
        print('In this game, you are allocated 17 total points. You are to use these points on your stats.')
        print('The available stats to choose from are: Attack, Defense, and Speed')
        print('Attack determines the damage done by your hero.')
        print('Defense determines the damage dealt to your hero.')
        print('Speed determines the chance your hero will dodge, dodge & heal, parry attacks, etc.')
        player_stats = dict()
        MAX_POINTS = 17
        total_points = 0
        while total_points < MAX_POINTS:
            player_stats['attack'] = int(input('Enter your desired attack: '))
            while player_stats['attack'] > 17:
                player_stats['attack'] = int(input('That\'s too high. Please enter your desired attack: '))
            else:
                total_points += player_stats['attack']
            if total_points < MAX_POINTS:
                player_stats['defense'] = int(input('Enter your desired defense: '))
                while player_stats['defense'] > 17 and total_points < MAX_POINTS:
                    player_stats['defense'] = int(input('That\'s too high. Please enter your desired defense: '))
                else:
                    total_points += player_stats['defense']
            else:
                player_stats['defense'] = 0
            if total_points < MAX_POINTS:
                player_stats['speed'] = int(input('Enter your desired speed: '))
                while player_stats['speed'] > 17 and total_points < MAX_POINTS:
                    player_stats['speed'] = int(input('That\'s too high. Please enter your desired speed: '))
                else:
                    total_points += player_stats['speed']
            else:
                player_stats['speed'] = 0
            if total_points < MAX_POINTS:
                print('You didn\'t spend all your points. Restarting...')
                total_points = 0
            elif total_points > MAX_POINTS:
                print('You went over the point limit of 17. Restarting...')
                total_points = 0
        storyline(player_name, player_stats)


# storyline is the main story sequence of the game.
def storyline(name, stats):
    print(name, ', you are a human. You have been captured by an elven/dwarven faction and sent to prison, ', sep='', end='')
    print('sentenced to death by combat!')
    print('The guards bring you to an arena, forced to fight another human.')
    battle('human', stats)
    print('You have won your first battle. You will fight again tomorrow.')
    print('You will now be brought back to your cell.')
    print('*** Sleeping ***')
    print()
    print('A spirit has come to your cell and gives you a sword and shield!')
    print('But you must immediately fight a dwarf...')
    battle('dwarf', stats)
    print('You defeated the dwarf, but the battle is far from over...')
    print('You must now find/fight your way out of the prison.')
    # Goes to prison hallway sequence


startup()
