# Landon Cayia and Taylor French
# CS 21 Final Project
# combat.py contains all the files and functions required for combat in "text-adventure.py". Must be imported.


# Random functions needed to determine whether a dodge is successful or not.
import random


# Global max health constant
MAX_HEALTH = 10


# battle_tutorial handles the player's first battle (Landon/Taylor)
def battle_tutorial(hero):
    # This is a tutorial
    battling = True
    # Dictionary of human stats
    human = dict()
    human['attack'] = 1
    human['defense'] = 1
    human['speed'] = 1
    # Health for player and enemy
    hero_health = 10
    human_health = 10
    print('Combat is turn based, and you always move first.')
    print('When you or the enemy uses a move, the other member of the battle will use a default attack unless there is '
          'a dodge.')
    input('Your performance in various categories of battle will be dependent on the stats you assigned yourself. Press'
          ' enter to continue.')
    print()
    print('You have 5 options each turn:')
    print('Sword Swing: Hero deals normal damage, and receives full damage.')
    print('Shield Bash: Hero receives half normal damage, and deals back half received (quarter normal) damage to enemy'
          '.')
    print('Heal: Hero heals back half full health, and receives full damage.')
    print('Dodge: Success is random, chances are based on speed. If successful, hero receives no damage. If '
          'unsuccessful, hero receives twice normal damage.')
    print('Dodge + Heal: Random, based on speed, requires higher speed than dodge for higher success rate.'
          'If successful, hero receives no damage and heals half health. If unsuccessful, hero receives triple normal '
          'damage.')
    input('Press enter to continue.')
    print()
    print('Enemy: Human')
    print('Attack: Very Low')
    print('Defense: Very Low')
    print('Speed: Very Low')
    # Normal damage calculations
    normal_offense = hero['attack'] / human['defense']
    normal_defense = human['attack'] / hero['defense']
    # Initialize turn counter
    turn = 1
    # Battle sequence loop
    while battling:
        try:
            move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
        except ValueError:
            print('That is not a valid option. Please enter a number 1-5.')
        else:
            # Player moves
            if move == '1':
                print('You used Sword Swing, and the human used its normal attack on you.')
                dealt = normal_offense
                human_health -= dealt
                received = normal_defense
                hero_health -= received
            elif move == '2':
                print('You used Shield Bash, and did a little damage to the human.')
                received = normal_defense / 2
                hero_health -= received
                dealt = received / 2
                human_health -= dealt
            elif move == '3':
                print('You used Heal, and recovered half your health. The human used its normal attack on you.')
                heal_health = 5
                hero_health += heal_health
                received = normal_defense
                hero_health -= received
            elif move == '4':
                rand = random.randint(1, 10)
                print('You attempted to Dodge.')
                if hero['speed'] >= rand:
                    print('Dodge successful.')
                elif hero['speed'] < rand:
                    received = normal_defense * 2
                    hero_health -= received
                    print('Dodge failed. The human\'s normal attack hit harder than usual.')
            elif move == '5':
                print('You attempted to Dodge + Heal.')
                rand = random.randint(1, 20)
                heal_health = 5
                if hero['speed'] >= rand:
                    hero_health += heal_health
                    # If heal brings health above 10, reset to 10
                    if hero_health >= MAX_HEALTH:
                        hero_health = 10
                    print('Dodge + Heal successful.')
                elif hero['speed'] < rand:
                    received = normal_defense * 3
                    hero_health -= received
                    print('Dodge + Heal failed. The human\'s normal attack hit very hard.')
            print('Your health is now', format(hero_health, '.2f'))
            print('The human\'s health is now', format(human_health, '.2f'))
            input('Press enter to continue.')
            print()
            # Check to see if the human is dead, if so return hero health
            if human_health <= 0:
                return hero_health
            # If the hero dies, returns game_over to end game
            if hero_health <= 0:
                hero_health = 'game_over'
                print()
                return hero_health
            # Accumulate turn counter
            turn += 1


# battle function handles battles with various enemies, accepting the type of enemy and the player's stat dictionary as
# parameters. (Landon/Taylor)
def battle(enemy, hero, hero_health):
    if enemy == 'dwarf':
        # ---------------------------- EXPLAIN DWARF BATTLE ---------------------------------
        battling = True
        # Dictionary of dwarf stats
        dwarf = dict()
        dwarf['attack'] = 1
        dwarf['defense'] = 6
        dwarf['speed'] = 2
        # Health for enemy
        dwarf_health = 10
        # Dwarf-specific mechanics
        dwarf_powerup = 0
        regen = False
        # Normal damage calculations
        normal_offense = hero['attack'] / dwarf['defense']
        normal_defense = dwarf['attack'] / hero['defense']
        # Initialize turn counter
        turn = 1
        print()
        print('Enemy: Dwarf')
        print('Attack: Very Low')
        print('Defense: High')
        print('Speed: Low')
        while battling:
            if regen:
                dwarf_health += 0.5
                print('The dwarf\'s regen added 0.5 health, the dwarf\'s health is now', dwarf_health)
            try:
                move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
            except ValueError:
                print('That is not a valid option. Please enter a number 1-5.')
            else:
                # Player moves
                if move == '1':
                    print('You used Sword Swing, and the dwarf used its normal attack on you.')
                    dealt = normal_offense
                    dwarf_health -= dealt
                    received = normal_defense
                    hero_health -= received
                elif move == '2':
                    print('You used Shield Bash, and did a little damage to the dwarf.')
                    received = normal_defense / 2
                    hero_health -= received
                    dealt = received / 2
                    dwarf_health -= dealt
                elif move == '3':
                    print('You used Heal, and recovered half your health. The dwarf used its normal attack on you.')
                    heal_health = 5
                    hero_health += heal_health
                    received = normal_defense
                    hero_health -= received
                elif move == '4':
                    rand = random.randint(1, 10)
                    print('You attempted to Dodge.')
                    if hero['speed'] >= rand:
                        print('Dodge successful.')
                    elif hero['speed'] < rand:
                        received = normal_defense * 2
                        hero_health -= received
                        print('Dodge failed. The dwarf\'s normal attack hit harder than usual.')
                elif move == '5':
                    print('You attempted to Dodge + Heal.')
                    rand = random.randint(1, 20)
                    heal_health = 5
                    if hero['speed'] >= rand:
                        hero_health += heal_health
                        # If heal brings health above 10, reset to 10
                        if hero_health >= MAX_HEALTH:
                            hero_health = 10
                        print('Dodge + Heal successful.')
                    elif hero['speed'] < rand:
                        received = normal_defense * 3
                        hero_health -= received
                        print('Dodge + Heal failed. The dwarf\'s normal attack hit very hard.')
                print('Your health is now', format(hero_health, '.2f'))
                print('The dwarf\'s health is now', format(dwarf_health, '.2f'))
                input('Press enter to continue.')
                print()
                # Check if the dwarf is dead, if so, returns hero's remaining health
                if dwarf_health <= 0:
                    return hero_health
                # If the hero dies, returns game_over to end game
                if hero_health <= 0:
                    hero_health = 'game_over'
                    print()
                    return hero_health
                # Dwarf move random generator
                dwarf_random = random.randint(1, 100)
                # Checks number of turns, dwarf behaves differently based on this
                if turn < 5:
                    if dwarf_random < 26:
                        dwarf_move = '1'
                    elif dwarf_random < 51:
                        dwarf_move = '2'
                    elif dwarf_random < 76:
                        dwarf_move = '3'
                    elif dwarf_random < 89:
                        dwarf_move = '4'
                    else:
                        dwarf_move = '5'
                else:
                    if dwarf_random < 6:
                        dwarf_move = '1'
                    elif dwarf_random < 11:
                        dwarf_move = '2'
                    elif dwarf_random < 16:
                        dwarf_move = '3'
                    elif dwarf_random < 61:
                        dwarf_move = '4'
                    else:
                        dwarf_move = '5'
                # Dwarf moves
                if dwarf_move == '1':
                    print('Dwarf used Regen. It will recover some health every turn.')
                    regen = True
                    dealt = normal_offense
                    dwarf_health -= dealt
                elif dwarf_move == '2':
                    print('Dwarf used Power-Up. The power of the dwarf\'s Axe Swing increased.')
                    dwarf_powerup += 1
                    dealt = normal_offense
                    dwarf_health -= dealt
                elif dwarf_move == '3':
                    print('Dwarf used Spider-Dwarf. Its speed increased.')
                    dwarf['speed'] *= 2
                    dealt = normal_offense
                    dwarf_health -= dealt
                elif dwarf_move == '4':
                    print('Dwarf attempted to dodge.')
                    rand = random.randint(1, 10)
                    if dwarf['speed'] >= rand:
                        print('Dodge successful.')
                    elif dwarf['speed'] < rand:
                        dealt = normal_defense * 2
                        dwarf_health -= dealt
                        print('Dodge failed. Your normal attack hit harder than usual.')
                elif dwarf_move == '5':
                    print('Dwarf used Axe Swing.')
                    received = normal_defense * dwarf_powerup
                    hero_health -= received
                    dealt = normal_offense
                    dwarf_health -= dealt
                print('Your health is now', format(hero_health, '.2f'))
                print('The dwarf\'s health is now', format(dwarf_health, '.2f'))
                input('Press enter to continue.')
                print()
                if dwarf_health <= 0:
                    return hero_health
                # If the hero dies, returns game_over to end game
                if hero_health <= 0:
                    hero_health = 'game_over'
                    print()
                    return hero_health
                # Accumulate turn counter
                turn += 1

    elif enemy == 'elf':
        battling = True
        # Dictionary of elf stats
        elf = dict()
        elf['attack'] = 5
        elf['defense'] = 1
        elf['speed'] = 5
        # Health for enemy
        elf_health = 10
        # Normal damage calculations
        normal_offense = hero['attack'] / elf['defense']
        normal_defense = elf['attack'] / hero['defense']
        # Initialize turn counter
        turn = 1
        print()
        print('Enemy: Elf')
        print('Attack: Moderate')
        print('Defense: Very Low')
        print('Speed: Moderate')
        while battling:
            try:
                move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
                # Checks whether it's the first turn or not, if so, asks player to move again
                if turn == 1 and move == 1:
                    print('Can\'t use Sword Swing on the first turn.')
                    move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
            except ValueError:
                print('That is not a valid option. Please enter a number 1-5.')
            else:
                # Player moves
                if move == '1':
                    print('You used Sword Swing, and the elf used its normal attack on you.')
                    dealt = normal_offense
                    elf_health -= dealt
                    received = normal_defense
                    hero_health -= received
                elif move == '2':
                    print('You used Shield Bash, and did a little damage to the elf.')
                    received = normal_defense / 2
                    hero_health -= received
                    dealt = received / 2
                    elf_health -= dealt
                elif move == '3':
                    print('You used Heal, and recovered half your health. The elf used its normal attack on you.')
                    heal_health = 5
                    hero_health += heal_health
                    received = normal_defense
                    hero_health -= received
                elif move == '4':
                    rand = random.randint(1, 10)
                    print('You attempted to Dodge.')
                    if hero['speed'] >= rand:
                        print('Dodge successful.')
                    elif hero['speed'] < rand:
                        received = normal_defense * 2
                        hero_health -= received
                        print('Dodge failed. The elf\'s normal attack hit harder than usual.')
                elif move == '5':
                    print('You attempted to Dodge + Heal.')
                    rand = random.randint(1, 20)
                    heal_health = 5
                    if hero['speed'] >= rand:
                        hero_health += heal_health
                        # If heal brings health above 10, reset to 10
                        if hero_health >= MAX_HEALTH:
                            hero_health = 10
                        print('Dodge + Heal successful.')
                    elif hero['speed'] < rand:
                        received = normal_defense * 3
                        hero_health -= received
                        print('Dodge + Heal failed. The elf\'s normal attack hit very hard.')
                print('Your health is now', format(hero_health, '.2f'))
                print('The elf\'s health is now', format(elf_health, '.2f'))
                input('Press enter to continue.')
                print()
                # Check if the elf is dead, if so, returns hero's remaining health
                if elf_health <= 0:
                    return hero_health
                # If the hero dies, returns game_over to end game
                if hero_health <= 0:
                    hero_health = 'game_over'
                    print()
                    return hero_health
                # elf move random generator
                elf_random = random.randint(1, 100)
                # Checks number of turns, elf behaves differently based on this
                if turn == 0:
                    if elf_random < 21:
                        elf_move = '1'
                    elif elf_random < 41:
                        elf_move = '2'
                    elif elf_random < 61:
                        elf_move = '3'
                    elif elf_random < 81:
                        elf_move = '4'
                    else:
                        elf_move = '5'
                else:
                    if elf_random < 26:
                        elf_move = '2'
                    elif elf_random < 51:
                        elf_move = '3'
                    elif elf_random < 76:
                        elf_move = '4'
                    else:
                        elf_move = '5'
                # Elf moves
                if elf_move == '1':
                    print('Elf used Bow and Arrow.')
                    received = normal_defense * 1.5
                    hero_health -= received
                    dealt = normal_offense
                    elf_health -= dealt
                elif elf_move == '2':
                    print('Elf used Sword Swing.')
                    received = normal_defense
                    hero_health -= received
                    dealt = normal_offense
                    elf_health -= dealt
                elif elf_move == '3':
                    print('Elf used Heal.')
                    heal_health = 5
                    elf_health += heal_health
                    if elf_health > 10:
                        elf_health = 10
                    dealt = normal_offense
                    elf_health -= dealt
                elif elf_move == '4':
                    print('Elf attempted to Parry.')
                    rand = random.randint(1, 10)
                    if elf['speed'] >= rand:
                        print('Dodge successful.')
                    elif elf['speed'] < rand:
                        dealt = normal_defense * 2
                        elf_health -= dealt
                        print('Dodge failed. Your normal attack hit harder than usual.')
                elif elf_move == '5':
                    print('Elf attempted to Parry + Heal.')
                    rand = random.randint(1, 20)
                    heal_health = 5
                    if elf['speed'] >= rand:
                        elf_health += heal_health
                        # If heal brings health above 10, reset to 10
                        if elf_health >= MAX_HEALTH:
                            elf_health = 10
                        print('Dodge + Heal successful.')
                    elif elf['speed'] < rand:
                        dealt = normal_offense * 3
                        elf_health -= dealt
                        print('Dodge + Heal failed. Your normal attack hit very hard.')
                print('Your health is now', format(hero_health, '.2f'))
                print('The elf\'s health is now', format(elf_health, '.2f'))
                input('Press enter to continue.')
                print()
                if elf_health <= 0:
                    return hero_health
                # If the hero dies, returns game_over to end game
                if hero_health <= 0:
                    hero_health = 'game_over'
                    print()
                    return hero_health
                # Accumulate turn counter
                turn += 1

    elif enemy == 'boss':
        battling = True
        # Dictionary of boss stats
        boss = dict()
        boss['attack'] = 5
        boss['defense'] = 6
        boss['speed'] = 5
        # Health for enemy
        boss_health = 10
        # Normal damage calculations
        normal_offense = hero['attack'] / boss['defense']
        normal_defense = boss['attack'] / hero['defense']
        # Initialize turn counter
        turn = 1
        print()
        print('Enemy: Boss Elf')
        print('Attack: Moderate')
        print('Defense: High')
        print('Speed: Moderate')
        while battling:
            try:
                move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
                # Checks whether it's the first turn or not, if so, asks player to move again
                if turn == 1 and move == 1:
                    print('Can\'t use Sword Swing on the first turn.')
                    move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal ')
            except ValueError:
                print('That is not a valid option. Please enter a number 1-5.')
            else:
                # Player moves
                if move == '1':
                    print('You used Sword Swing, and the boss used its normal attack on you.')
                    dealt = normal_offense
                    boss_health -= dealt
                    received = normal_defense
                    hero_health -= received
                elif move == '2':
                    print('You used Shield Bash, and did a little damage to the boss.')
                    received = normal_defense / 2
                    hero_health -= received
                    dealt = received / 2
                    boss_health -= dealt
                elif move == '3':
                    print('You used Heal, and recovered half your health. The boss used its normal attack on you.')
                    heal_health = 5
                    hero_health += heal_health
                    received = normal_defense
                    hero_health -= received
                elif move == '4':
                    rand = random.randint(1, 10)
                    print('You attempted to Dodge.')
                    if hero['speed'] >= rand:
                        print('Dodge successful.')
                    elif hero['speed'] < rand:
                        received = normal_defense * 2
                        hero_health -= received
                        print('Dodge failed. The boss\'s normal attack hit harder than usual.')
                elif move == '5':
                    print('You attempted to Dodge + Heal.')
                    rand = random.randint(1, 20)
                    heal_health = 5
                    if hero['speed'] >= rand:
                        hero_health += heal_health
                        # If heal brings health above 10, reset to 10
                        if hero_health >= MAX_HEALTH:
                            hero_health = 10
                        print('Dodge + Heal successful.')
                    elif hero['speed'] < rand:
                        received = normal_defense * 3
                        hero_health -= received
                        print('Dodge + Heal failed. The boss\'s normal attack hit very hard.')
                print('Your health is now', format(hero_health, '.2f'))
                print('The boss\'s health is now', format(boss_health, '.2f'))
                input('Press enter to continue.')
                print()
                # Check if the boss is dead, if so, returns hero's remaining health
                if boss_health <= 0:
                    return hero_health
                # If the hero dies, returns game_over to end game
                if hero_health <= 0:
                    hero_health = 'game_over'
                    print()
                    return hero_health
                # boss move random generator
                boss_random = random.randint(1, 100)
                # Checks number of turns, boss behaves differently based on this
                if turn == 0:
                    if boss_random < 21:
                        boss_move = '1'
                    elif boss_random < 41:
                        boss_move = '2'
                    elif boss_random < 61:
                        boss_move = '3'
                    elif boss_random < 81:
                        boss_move = '4'
                    else:
                        boss_move = '5'
                else:
                    if boss_random < 26:
                        boss_move = '2'
                    elif boss_random < 51:
                        boss_move = '3'
                    elif boss_random < 76:
                        boss_move = '4'
                    else:
                        boss_move = '5'
                # boss moves
                if boss_move == '1':
                    print('Boss used Bow and Arrow.')
                    received = normal_defense * 1.5
                    hero_health -= received
                    dealt = normal_offense
                    boss_health -= dealt
                elif boss_move == '2':
                    print('Boss used Sword Swing.')
                    received = normal_defense
                    hero_health -= received
                    dealt = normal_offense
                    boss_health -= dealt
                elif boss_move == '3':
                    print('Boss used Heal.')
                    heal_health = 5
                    boss_health += heal_health
                    if boss_health > 10:
                        boss_health = 10
                    dealt = normal_offense
                    boss_health -= dealt
                elif boss_move == '4':
                    print('Boss attempted to Parry.')
                    rand = random.randint(1, 10)
                    if boss['speed'] >= rand:
                        print('Dodge successful.')
                    elif boss['speed'] < rand:
                        dealt = normal_defense * 2
                        boss_health -= dealt
                        print('Dodge failed. Your normal attack hit harder than usual.')
                elif boss_move == '5':
                    print('boss attempted to Parry + Heal.')
                    rand = random.randint(1, 20)
                    heal_health = 5
                    if boss['speed'] >= rand:
                        boss_health += heal_health
                        # If heal brings health above 10, reset to 10
                        if boss_health >= MAX_HEALTH:
                            boss_health = 10
                        print('Dodge + Heal successful.')
                    elif boss['speed'] < rand:
                        dealt = normal_offense * 3
                        boss_health -= dealt
                        print('Dodge + Heal failed. Your normal attack hit very hard.')
                print('Your health is now', format(hero_health, '.2f'))
                print('The boss\'s health is now', format(boss_health, '.2f'))
                input('Press enter to continue.')
                print()
                if boss_health <= 0:
                    return hero_health
                # If the hero dies, returns game_over to end game
                if hero_health <= 0:
                    hero_health = 'game_over'
                    print()
                    return hero_health
                # Accumulate turn counter
                turn += 1
