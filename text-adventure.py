# Landon Cayia and Taylor French
# CS 21 Final Project
# This is a simple, short text adventure game that the user navigates using menu options.


# Importing random module and combat module that we made
import random
import combat
random.seed()


# Startup function is the first function to run when the game starts (Landon)
def startup():
    print('Prison Escape')
    print('Created by Landon Cayia and Taylor French')
    # Allows the player to select an option to start or exit the game
    selection = input('1: New Game  2: Exit ')
    # Controls loop for whether game has started, helps with exception handling
    game_started = False
    while not game_started:
        if selection.isnumeric():
            if selection == '1':
                intro(1)
            elif selection == '2':
                print('Thank you for playing!')
        else:
            selection = input('Please enter a number. 1: New Game  2: Exit ')


# intro function will introduce the player to the game and allow them to choose their stats (Landon)
def intro(mode):
    if mode == 1:
        # Get player's name
        player_name = input('Greetings, challenger! What is your name? ')
        print(player_name, ', welcome to Prison Escape!', sep='')
        print()
        print('In this game, you are allocated 17 total points. You are to use these points on your stats.')
        print()
        print('The available stats to choose from are: Attack, Defense, and Speed')
        print('Attack determines the damage done by your hero.')
        print('Defense determines the damage dealt to your hero.')
        print('Speed determines the chance your hero will dodge, dodge & heal, parry attacks, etc.')
        print()
        print('One stat cannot be higher than 10, and cannot be 0.')
        print()
        # Dictionary containing player's stats of choice.
        player_stats = dict()
        # Constant to limit the number of points the player can assign themselves in total.
        MAX_POINTS = 17
        # Constant to limit the number of points the player can assign to a single stat
        MAX_STAT = 10
        # Total number of points the player assigns themselves, controls loops
        total_points = 0
        # Controls exception handling for stat assignment
        stats_assigned = False
        while not stats_assigned:
            try:
                while total_points < MAX_POINTS:
                    # Get player's attack stat
                    player_stats['attack'] = int(input('Enter your desired attack: '))
                    # Check if attack is greater than the max for a stat, if so, ask again
                    while player_stats['attack'] > MAX_STAT or player_stats['attack'] == 0 and total_points < MAX_POINTS:
                        player_stats['attack'] = int(input('Invalid value. Please enter your desired attack: '))
                    # Accumulate total points
                    total_points += player_stats['attack']
                    # Check if total points are less than the max value
                    if total_points < MAX_POINTS:
                        # Get player defense
                        player_stats['defense'] = int(input('Enter your desired defense: '))
                        # Check if player's defense is greater than the max for a stat
                        while player_stats['defense'] > MAX_STAT and total_points < MAX_POINTS or player_stats['defense'] == 0 and total_points < MAX_POINTS:
                            player_stats['defense'] = int(input('Invalid value. Please enter your desired defense: '))
                        total_points += player_stats['defense']
                    # Check if total points are less than the max value
                    if total_points < MAX_POINTS:
                        # Get player speed
                        player_stats['speed'] = int(input('Enter your desired speed: '))
                        # Check if player's speed is greater than the max for a stat
                        while player_stats['speed'] > MAX_STAT and total_points < MAX_POINTS or player_stats['speed'] == 0 and total_points < MAX_POINTS:
                            player_stats['speed'] = int(input('Invalid value. Please enter your desired speed: '))
                        total_points += player_stats['speed']
                    # Check if total points are less than the max value
                    if total_points < MAX_POINTS:
                        print('You didn\'t spend all of your points. Restarting...')
                        total_points = 0
                    # Check if total points are greater than the max value, if so, reset
                    elif total_points > MAX_POINTS:
                        print('You went over the point limit of 17. Restarting...')
                        total_points = 0
                    # If the correct number of points has been assigned
                    else:
                        print()
                        print('Here are your stats:', player_stats)
                        stats_assigned = True
            # Exception handling, if there is a Value Error, reset
            except ValueError:
                print('You entered character(s) that are not integers. Please try again.')
                total_points = 0
        storyline(player_name, player_stats)


# storyline is the main story sequence of the game. (Landon/Taylor)
def storyline(name, stats):
    # Loop to keep the game running when the player is alive
    print(name, ', you are a human. You have been captured by an elven/dwarven faction and sent to prison, ', sep='',
          end='')
    print('sentenced to death by combat.')
    input('The guards bring you to an arena, forced to fight another human. Press enter to continue.')
    print()
    health = combat.battle_tutorial(stats)
    if health == 'game_over':
        print('Sorry, but you died. It\'s Game Over. :( We hope you\'ll play again!')
    print('You have won your first battle. You will fight again tomorrow.')
    print('You will now be brought back to your cell.')
    print('*** Sleeping ***')
    print()
    print('A spirit has come to your cell and gives you a sword and shield!')
    print('But you must immediately fight a dwarf...')
    health = combat.battle('dwarf', stats, health)
    print('You defeated the dwarf, but the battle is far from over...')
    print('You must now find/fight your way out of the prison.')
    # Goes to prison hallway sequence
    print('From your cell there are two hallways you can choose from: Hallway 1 or Hallway 2. One of these has an enemy'
          ' while the other provides safe passage to the next part of the prison.')
    hallway = int(input("Enter '1' to choose Hallway 1 or enter '2' to choose Hallway 2."))
    # First hallway choice is 1.
    if hallway == 1:
        print('You chose correctly. From here there are two hallways you can choose from: Hallway 3 or Hallway 4. One '
              'of these has an enemy while the other provides safe passage to the next part of the prison.')
        hallway = int(input("Enter '3' to choose Hallway 3 or enter '4' to choose Hallway 4."))
        if hallway == 3:
            print('You chose correctly. You can see light near the end of both of the next hallways. From here there '
                  'are two hallways you can choose from: Hallway 7 or Hallway 8. One of these has an enemy while the '
                  'other allows you to escape the prison without facing an enemy.')
            hallway = int(input("Enter '7' to choose Hallway 7 or enter '8' to choose Hallway 8."))
            if hallway == 7:
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                health = combat.battle('boss', stats, health)
            if hallway == 8:
                rand = encounter()
                if rand <= 50:
                    print('You have encountered a dwarf.')
                    health = combat.battle('dwarf', stats, health)
                elif rand > 50:
                    print('You have encountered an elf.')
                    health = combat.battle('elf', stats, health)
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                health = combat.battle('boss', stats, health)
        if hallway == 4:
            rand = encounter()
            if rand <= 50:
                print('You have encountered a dwarf.')
                health = combat.battle('dwarf', stats, health)
            elif rand > 50:
                print('You have encountered an elf.')
                health = combat.battle('elf', stats, health)
            print('You can see light near the end of both of the next hallways. From here there are two hallways you '
                  'can choose from: Hallway 9 or Hallway 10. One of these has an enemy while the other provides safe '
                  'passage to the next part of the prison.')
            hallway = int(input("Enter '9' to choose Hallway 9 or enter '10' to choose Hallway 10."))
            if hallway == 9:
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                health = combat.battle('boss', stats, health)
            if hallway == 10:
                rand = encounter()
                if rand <= 50:
                    print('You have encountered a dwarf.')
                    health = combat.battle('dwarf', stats, health)
                elif rand > 50:
                    print('You have encountered an elf.')
                    health = combat.battle('elf', stats, health)
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                health = combat.battle('boss', stats, health)
    # First hallway choice is 2.
    if hallway == 2:
        rand = encounter()
        if rand <= 50:
            print('You have encountered a dwarf.')
            health = combat.battle('dwarf', stats, health)
        elif rand > 50:
            print('You have encountered an elf.')
            health = combat.battle('elf', stats, health)
        print('From here there are two hallways you can choose from: Hallway 5 or Hallway 6. One of these has an enemy '
              'while the other provides safe passage to the next part of the prison.')
        hallway = int(input("Enter '5' to choose Hallway 5 or enter '6' to choose Hallway 6."))
        if hallway == 5:
            print('You chose correctly. You can see light near the end of both of the next hallways. From here there '
                  'are two hallways you can choose from: Hallway 11 or Hallway 12. One of these has an enemy while the '
                  'other allows you to escape the prison without facing an enemy.')
            hallway = int(input("Enter '11' to choose Hallway 11 or enter '12' to choose Hallway 12."))
            if hallway == 11:
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                health = combat.battle('boss', stats, health)
            if hallway == 12:
                rand = encounter()
                if rand <= 50:
                    print('You have encountered a dwarf.')
                    health = combat.battle('dwarf', stats, health)
                elif rand > 50:
                    print('You have encountered an elf.')
                    health = combat.battle('elf', stats, health)
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                health = combat.battle('boss', stats, health)
        if hallway == 6:
            rand = encounter()
            if rand <= 50:
                print('You have encountered a dwarf.')
                health = combat.battle('dwarf', stats, health)
            elif rand > 50:
                print('You have encountered an elf.')
                health = combat.battle('elf', stats, health)
            print('You can see light near the end of both of the next hallways. From here there are two hallways you '
                  'can choose from: Hallway 13 or Hallway 14. One of these has an enemy while the other provides safe '
                  'passage to the next part of the prison.')
            hallway = int(input("Enter '13' to choose Hallway 13 or enter '14' to choose Hallway 14."))
            if hallway == 13:
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                health = combat.battle('boss', stats, health)
            if hallway == 14:
                rand = encounter()
                if rand <= 50:
                    print('You have encountered a dwarf.')
                    health = combat.battle('dwarf', stats, health)
                elif rand > 50:
                    print('You have encountered an elf.')
                    health = combat.battle('elf', stats, health)
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
# When the game is won*****


# encounter generates a random number from 1 to 100 to determine which enemy (dwarf/elf) is encountered. (Taylor)
def encounter():
    rand = random.randint(1, 100)
    return rand


startup()
