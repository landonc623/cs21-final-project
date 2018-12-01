# Landon Cayia and Taylor French
# CS 21 Final Project
# combat.py contains all the files and functions required for combat in "text-adventure.py". Must be imported.


# battle function handles battles with various enemies, accepting the type of enemy and the player's stat dictionary as parameters.
def battle(enemy, hero):
    # This is a tutorial.
    if enemy == 'human':
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
            normal_offense = hero['attack'] / human['defense']
            normal_defense = human['attack'] / hero['defense']
            move = input('1: Sword Swing, 2: Shield Bash, 3: Heal, 4: Dodge, 5: Dodge + Heal')
            if move == '1':
                human_health -= normal_offense
                hero_health -= normal_defense
            elif move == '2':
                human_health -= normal_defense / 2
                human_health -= normal_offense / 4
    elif enemy == 'elf':
        # Elf battle here
    elif enemy == 'dwarf':
        # Dwarf battle here
    elif enemy == 'boss':
        # Boss battle here