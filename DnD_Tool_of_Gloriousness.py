#!/usr/bin/python3
import os
import DnD
import json
import random


print('\nPress \'q\' to quit or go back.')
while True:
    print('What would you like to do? \n')
    print('1) Add a new character')
    print('2) Get a character\'s specific stat')
    print('3) Update a character\'s stats')
    print('4) Add a new monster')
    print('5) Get a monster\'s specific stat')
    print('6) Update a monster\'s stats')
    print('7) Roll a single dX')
    print('8) Roll XdX')
    print('9) Battle simulator')
    print('q) Quit \n')

    menu_entry = input()
    if menu_entry == 'q':
        exit(print('Bye bye!'))
    else:
        menu_entry = int(menu_entry)

        if menu_entry <= 3:
            character_name = input('Enter character name: \n').lower()
        # add character
        if menu_entry == 1:
            characters = DnD.Characters()
            characters.create_character(character_name)
            

        # get a stat or update one
        elif menu_entry == 2 or menu_entry == 3:
            character_stat = input('Enter character stat: \n')

            if menu_entry == 2:
                print(get_character_stat(character_name, character_stat))

            elif menu_entry == 3:
                try:
                    new_stat = int(input('Enter new stat value: \n'))
                except ValueError:
                    print('Enter a number, not a string.')
                    main()
                # attempt to add the stat
                change_character_stat(character_name, character_stat, new_stat)
                print('Done')

        # add monster
        if menu_entry == 4:
            add_monster()

        # get a stat or update one
        elif menu_entry == 5 or menu_entry == 6:
            monster_name = input('Enter monster name: \n').lower()
            monster_stat = input('Enter monster stat: \n')

            if menu_entry == 5:
                print(get_monster_stat(monster_name, monster_stat))

            elif menu_entry == 6:
                try:
                    new_stat = int(input('Enter new stat value: \n'))
                except ValueError:
                    print('Enter a number, not a string.')
                    main()
                # attempt to add the stat
                change_monster_stat(monster_name, monster_stat, new_stat)
                print('Done')

        # single die roll
        if menu_entry == 7:
            sides = int(input('Enter amount of sides: \n'))
            print(roll_die(sides))

        # multi-die roll
        if menu_entry == 8:
            total_dice = int(input('Number of dice to throw? \n'))
            sides = int(input('Enter amount of sides: \n'))
            while total_dice > 0:
                print(roll_die(sides))
                total_dice -= 1

        # simulate a battle (still half broken HP updates?)
        if menu_entry == 9:
            character_name = input('Enter character name: \n')
            monster_name = input('Enter monster name: \n')
            battle_simulator(character_name, monster_name)
