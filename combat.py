# Landon Cayia and Taylor French
# CS 21 Final Project
# combat.py contains all the files and functions required for combat in "text-adventure.py". Must be imported.


# Random functions needed to determine whether a dodge is successful or not.
import random


# battle_tutorial handles the player's first battle. (Landon/Taylor)
def battle_tutorial(hero):
    # This is a tutorial.
    battling = True
    human = dict()
    human['attack'] = 1
    human['defense'] = 1
    human['speed'] = 1
    hero_health = 10
    human_health = 10
    print('This is your first battle, so the system will be explained.')
    print('Combat is turn based, and you always move first.')
    print('Your performance in various categories of battle will be dependent on the stats you assigned yourself.')
    print('Normal damage is set as character attack/opponent defense, which gets subtracted from HP. Every character has 10 HP.')
    print('Stat modifiers chosen at the beginning of the game will be factored in.')
    print('You have 5 options each turn:')
    print('Sword Swing: Hero deals normal damage, and receives full damage.')
    print('Shield Bash: Hero receives half normal damage, and deals back half received (quarter normal) damage to enemy.')
    print('Heal: Hero heals back half full health, and receives full damage.')
    print('Dodge: Success is random, chances are based on speed. If successful, hero receives no damage. If unsuccessful, hero receives twice normal damage.')
    print('Dodge + Heal: Random, based on speed, requires higher speed than dodge for higher success rate.'
          'If successful, hero receives no damage and heals half health. If unsuccessful, hero receives triple normal damage.')
    while battling:
        turn = 0
        normal_offense = hero['attack'] / human['defense']
        normal_defense = human['attack'] / hero['defense']
        move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
        if move == '1':
            human_health -= normal_offense
            hero_health -= normal_defense
            turn += 1
        elif move == '2':
            received = normal_defense / 2
            hero_health -= received
            human_health -= received / 2
            turn += 1
        elif move == '3':
            hero_health += 5
            hero_health -= normal_defense
            turn += 1
        elif move == '4':
            # How does dodge system work with speed?
            rand = random.randint(1, 10)
            if hero['speed'] >= rand:
                # ???
            elif hero['speed'] < rand:
                received = normal_defense * 2
                hero_health -= received
            turn += 1
        elif move == '5':
            # Same as above
            rand = random.randint(1, 10)
            if hero['speed'] >= rand:
                hero_health += 5
            elif hero['speed'] < rand:
                received = normal_defense * 3
                hero_health -= received
            turn += 1
        if human_health <= 0:
            battling = False
            return hero_health


# battle function handles battles with various enemies, accepting the type of enemy and the player's stat dictionary as parameters. (Landon/Taylor)
def battle(enemy, hero, hero_health):
    if enemy == 'dwarf':
        battling = True
        dwarf = dict()
        dwarf['attack'] = 1
        dwarf['defense'] = 6
        dwarf['speed'] = 2
        dwarf_health = 10
        while battling:
            turn = 0
            normal_offense = hero['attack'] / dwarf['defense']
            normal_defense = dwarf['attack'] / hero['defense']
            move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
            if move == '1':
                dwarf_health -= normal_offense
                hero_health -= normal_defense
                turn += 1
            elif move == '2':
                received = normal_defense / 2
                hero_health -= received
                dwarf_health -= received / 2
                turn += 1
            elif move == '3':
                hero_health += 5
                hero_health -= normal_defense
                turn += 1
            elif move == '4':
                rand = random.randint(1, 10)
                if hero['speed'] >= rand:
                    # ???
                elif hero['speed'] < rand:
                    received = normal_defense * 2
                    hero_health -= received
                turn += 1
            elif move == '5':
                rand = random.randint(1, 10)
                if hero['speed'] >= rand:
                    hero_health += 5
                elif hero['speed'] < rand:
                    received = normal_defense * 3
                    hero_health -= received
                turn += 1
            if human_health <= 0:
                battling = False
                return hero_health

    elif enemy == 'elf':
        battling = True
        elf = dict()
        elf['attack'] = 5
        elf['defense'] = 1
        elf['speed'] = 5
        elf_health = 10
        while battling:
            turn = 0
            normal_offense = hero['attack'] / elf['defense']
            normal_defense = elf['attack'] / hero['defense']
            move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
            if move == '1':
                elf_health -= normal_offense
                hero_health -= normal_defense
                turn += 1
            elif move == '2':
                received = normal_defense / 2
                hero_health -= received
                elf_health -= received / 2
                turn += 1
            elif move == '3':
                hero_health += 5
                hero_health -= normal_defense
                turn += 1
            elif move == '4':
                rand = random.randint(1, 10)
                if hero['speed'] >= rand:
                    # ???
                elif hero['speed'] < rand:
                    received = normal_defense * 2
                    hero_health -= received
                turn += 1
            elif move == '5':
                rand = random.randint(1, 10)
                if hero['speed'] >= rand:
                    hero_health += 5
                elif hero['speed'] < rand:
                    received = normal_defense * 3
                    hero_health -= received
                turn += 1
            if human_health <= 0:
                battling = False
                return hero_health

    elif enemy == 'boss':
        battling = True
        boss = dict()
        boss['attack'] = 5
        boss['defense'] = 6
        boss['speed'] = 5
        boss_health = 10
        while battling:
            turn = 0
            normal_offense = hero['attack'] / boss['defense']
            normal_defense = boss['attack'] / hero['defense']
            move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
            if move == '1':
                boss_health -= normal_offense
                hero_health -= normal_defense
                turn += 1
            elif move == '2':
                received = normal_defense / 2
                hero_health -= received
                boss_health -= received / 2
                turn += 1
            elif move == '3':
                hero_health += 5
                hero_health -= normal_defense
                turn += 1
            elif move == '4':
                rand = random.randint(1, 10)
                if hero['speed'] >= rand:
                    # ???
                elif hero['speed'] < rand:
                    received = normal_defense * 2
                    hero_health -= received
                turn += 1
            elif move == '5':
                rand = random.randint(1, 10)
                if hero['speed'] >= rand:
                    hero_health += 5
                elif hero['speed'] < rand:
                    received = normal_defense * 3
                    hero_health -= received
                turn += 1
            if human_health <= 0:
                battling = False
                return hero_health
