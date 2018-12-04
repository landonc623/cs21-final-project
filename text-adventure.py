# Landon Cayia and Taylor French
# CS 21 Final Project
# This is a simple, short text adventure game that the user navigates using menu options.


import random
import combat
random.seed()


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


# storyline is the main story sequence of the game. (Landon/Taylor)
def storyline(name, stats):
    print(name, ', you are a human. You have been captured by an elven/dwarven faction and sent to prison, ', sep='', end='')
    print('sentenced to death by combat.')
    print('The guards bring you to an arena, forced to fight another human.')
    health = combat.battle_tutorial(stats)
    print('You have won your first battle. You will fight again tomorrow.')
    print('You will now be brought back to your cell.')
    print('*** Sleeping ***')
    print()
    print('A spirit has come to your cell and gives you a sword and shield!')
    print('But you must immediately fight a dwarf...')
    combat.battle('dwarf', stats, health)
    print('You defeated the dwarf, but the battle is far from over...')
    print('You must now find/fight your way out of the prison.')
    # Goes to prison hallway sequence
    print('From your cell there are two hallways you can choose from: Hallway 1 or Hallway 2. One of these has an enemy while the other provides safe passage to the next part of the prison.')
    hallway = int(input("Enter '1' to choose Hallway 1 or enter '2' to choose Hallway 2."))
    # First hallway choice is 1.
    if hallway = 1:
        print('You chose correctly. From here there are two hallways you can choose from: Hallway 3 or Hallway 4. One of these has an enemy while the other provides safe passage to the next part of the prison.')
        hallway = int(input("Enter '3' to choose Hallway 3 or enter '4' to choose Hallway 4."))
        if hallway = 3:
            print('You chose correctly. You can see light near the end of both of the next hallways. From here there are two hallways you can choose from: Hallway 7 or Hallway 8. One of these has an enemy while the other allows you to escape the prison without facing an enemy.')
            hallway = int(input("Enter '7' to choose Hallway 7 or enter '8' to choose Hallway 8."))
            if hallway = 7:
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
            if hallway = 8:
                rand = encounter()
                if rand <= 50:
                    print('You have encountered a dwarf.')
                    combat.battle('dwarf', stats, health)
                elif rand > 50:
                    print('You have encountered an elf.')
                    combat.battle('elf', stats, health)
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
        if hallway  = 4:
            rand = encounter()
            if rand <= 50:
                print('You have encountered a dwarf.')
                combat.battle('dwarf', stats, health)
            elif rand > 50:
                print('You have encountered an elf.')
                combat.battle('elf', stats, health)
            print('You can see light near the end of both of the next hallways. From here there are two hallways you can choose from: Hallway 9 or Hallway 10. One of these has an enemy while the other provides safe passage to the next part of the prison.')
            hallway = int(input("Enter '9' to choose Hallway 9 or enter '10' to choose Hallway 10."))
            if hallway = 9:
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
            if hallway = 10:
                rand = encounter()
                if rand <= 50:
                    print('You have encountered a dwarf.')
                    combat.battle('dwarf', stats, health)
                elif rand > 50:
                    print('You have encountered an elf.')
                    combat.battle('elf', stats, health)
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
    # First hallway choice is 2.
    if hallway = 2:
        rand = encounter()
        if rand <= 50:
            print('You have encountered a dwarf.')
            combat.battle('dwarf', stats, health)
        elif rand > 50:
            print('You have encountered an elf.')
            combat.battle('elf', stats, health)
        print('From here there are two hallways you can choose from: Hallway 5 or Hallway 6. One of these has an enemy while the other provides safe passage to the next part of the prison.')
        hallway = int(input("Enter '5' to choose Hallway 5 or enter '6' to choose Hallway 6."))
        if hallway = 5:
            print('You chose correctly. You can see light near the end of both of the next hallways. From here there are two hallways you can choose from: Hallway 11 or Hallway 12. One of these has an enemy while the other allows you to escape the prison without facing an enemy.')
            hallway = int(input("Enter '11' to choose Hallway 11 or enter '12' to choose Hallway 12."))
            if hallway = 11:
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
            if hallway = 12:
                rand = encounter()
                if rand <= 50:
                    print('You have encountered a dwarf.')
                    combat.battle('dwarf', stats, health)
                elif rand > 50:
                    print('You have encountered an elf.')
                    combat.battle('elf', stats, health)
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
        if hallway = 6:
            rand = encounter()
            if rand <= 50:
                print('You have encountered a dwarf.')
                combat.battle('dwarf', stats, health)
            elif rand > 50:
                print('You have encountered an elf.')
                combat.battle('elf', stats, health)
            print('You can see light near the end of both of the next hallways. From here there are two hallways you can choose from: Hallway 13 or Hallway 14. One of these has an enemy while the other provides safe passage to the next part of the prison.')
            hallway = int(input("Enter '13' to choose Hallway 13 or enter '14' to choose Hallway 14."))
            if hallway = 13:
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
            if hallway = 14:
                rand = encounter()
                if rand <= 50:
                    print('You have encountered a dwarf.')
                    combat.battle('dwarf', stats, health)
                elif rand > 50:
                    print('You have encountered an elf.')
                    combat.battle('elf', stats, health)
                print('Congratulations on escaping the prison! But you still have one enemy left: the final boss!')
                combat.battle('boss', stats, health)
# encounter generates a random number from 1 to 100 to determine which enemy (dwarf/elf) is encountered. (Taylor)
def encounter():
    rand = random.randint(1,100)
    return rand

startup()
