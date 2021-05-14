#!/usr/bin/python3

# Made by Jordan Leich & Mordy Waldner on 5/11/2021, Last updated on 5/14/2021, Version 1.5

# TODO List complete the storyline, add more checkpoints as story progresses, finish merchant function

# Imports
import colors
import json
import time
import random

try:
    with open('data.json', 'r') as data:
        data = json.load(data)
        user_balance = data['Balance']
        user_health = data['Health']
        merchant_luck = data['Merchant Luck']
        starting_knife = data['Starting Knife']
        baseball_bat = data['Baseball Bat']
        beretta_pistol = data['Beretta Pistol']
        ak_47_rifle = data['AK_47 Rifle']
except FileNotFoundError:
    print(colors.green + 'No saved data found...\nStarting a fresh game...\n' + colors.reset)
    user_balance = 0
    user_health = 0
    merchant_luck = 0
    time.sleep(1)


def game_intro_description():
    print('This is a zombie survival game where you must make the best choices and decisions possible in order to live.'
          ' As a survivor, you will encounter zombies, weapons, people, and a merchant to buy from with an '
          'in-game currency. Every decision you make has a cause and effect while some lead you to fortune and others '
          'lead you to death.\n')
    time.sleep(2)
    game()


def game():
    global user_health, user_balance, merchant_luck, starting_knife, ak_47_rifle, beretta_pistol, baseball_bat
    difficulty()

    print('You have ended up in a small local town called Hinesville. This old town contains a population of about '
          'only 6000 people and holds only a gas station, local diner, and a park. The current year is 1999 and you '
          'cannot wait to finally get on with your life and move somewhere more alive\n')
    time.sleep(2)
    user_choice1 = int(input('While sitting down in your living room apartment, you can either (1) look around or '
                             '(2) walk outside: '))
    print()
    time.sleep(1)

    if user_choice1 == 1:
        print('You have decided to look around your apartment and decide to grab a concealed knife that you legally '
              'are allowed to carry in public areas just in case anything happens...\n')
        time.sleep(1)
        starting_knife = True
        outside_area()
    elif user_choice1 == 2:
        time.sleep(1)
        starting_knife = False
        outside_area()
    else:
        error_message()


def merchant():
    global merchant_luck, user_balance
    merchant_luck = random.randint(1, 7)

    if merchant_luck == 4:
        print(colors.green + 'Whoosh! The lucky merchant has appeared in-front of you...\n' + colors.reset)
        time.sleep(1)

        if user_balance <= 0:
            print(colors.yellow + 'Uh-Oh! You do not have enough money to buy anything... keep playing to acquire more '
                                  'money!\n', colors.reset)
            time.sleep(1)

        user_choice = str(input('Would you like to buy from the merchant or skip past him (buy / skip): '))
        print()
        time.sleep(1)

        if user_choice.lower() == 'b' or user_choice.lower() == 'buy' or user_choice.lower() == 'y' or user_choice. \
                lower() == 'yes':
            user_item_buy = int(input('''--- Merchants inventory ---
(1) Spiked Baseball Bat (5 Dollars)
(2) 1997 Beretta Pistol (20 Dollars)
(3) 1999 AK-47 Assault Rifle (5 Dollars)
What would you like to buy or skip the merchant: '''))
            print()
            time.sleep(1)

            if user_item_buy == 1:
                print(colors.green + 'Spiked Baseball Bat has been purchased!\n', colors.reset)
                time.sleep(1)

        elif user_choice.lower() == 's' or user_choice.lower() == 'sell' or user_choice.lower() == 'n' or user_choice. \
                lower() == 'no':
            print()


def gas_station():
    global user_health, user_balance, merchant_luck
    print('You have entered the local gas station...\n', colors.green + 'A checkpoint has been reached...\n',
          colors.reset)
    time.sleep(1)

    merchant()

    with open('data.json', 'w') as user_data_file:
        user_data_file.write(json.dumps({'Balance': user_balance, 'Health': user_health,
                                         'Merchant Luck': merchant_luck, 'Starting Knife': starting_knife,
                                         'Baseball Bat': baseball_bat, 'Beretta Pistol': beretta_pistol,
                                         'AK 47 Rifle': ak_47_rifle}))


def outside_area():
    global user_health, user_balance, merchant_luck, starting_knife
    print('You make your way to the outside area...\n')
    time.sleep(1)
    print('You instantly notice something is not right... a dark gloomy fog covers all of the town and you do not see '
          'a single friendly soul insight... You start to come to a conclusion about where everybody in the small '
          'town of Hinesville has went but nothing is making sense...\n')
    time.sleep(2)
    user_choice = int(input('You have the choice to either explore (1) outside area or (2) visit the local gas '
                            'station: '))
    print()
    time.sleep(1)

    if user_choice == 1:
        print('You decide to explore the outside area and along the way, you see a woman bleeding out on the ground '
              'with the shape of a man figure hovering over her...\n')
        time.sleep(2)
        print('Lone behold... the figure is eating the woman alive but you are too late to rescue her!\n')
        time.sleep(1.5)
        user_choice = int(input('Since you have the knife on you already, (1) do you attack the zombie or (2) '
                                'avoid the zombie and run to the local gas station: '))
        print()
        time.sleep(1)

        if user_choice == 1:
            print('You attacked the zombie with the knife you found earlier and killed the zombie... '
                  'You search the body of the zombie and woman and find a total of 11 Dollars...')

        elif user_choice == 2:
            gas_station()
        else:
            error_message()

    elif user_choice == 2:
        gas_station()
    else:
        error_message()


def difficulty():
    global user_health
    print(colors.green + 'Easy\n' + colors.reset + colors.yellow + 'Medium\n' + colors.reset + colors.red + 'Hardcore\n'
          + colors.reset)

    user_difficulty = str(input('Select a difficulty: '))
    print()
    time.sleep(1)

    if user_difficulty.lower() == 'e' or user_difficulty.lower() == 'easy':
        print(colors.green + 'Easy mode has been selected, you will begin with 200 health.\n' + colors.reset)
        user_health = 200
        time.sleep(1)
    elif user_difficulty.lower() == 'm' or user_difficulty.lower() == 'medium':
        print(colors.yellow + 'Medium mode has been selected, you will begin with 100 health.\n' + colors.reset)
        user_health = 100
        time.sleep(1)
    elif user_difficulty.lower() == 'h' or user_difficulty.lower() == 'hard':
        print(colors.red + 'Hardcore mode has been selected, you will begin with only 50 health.\n' + colors.reset)
        user_health = 50
        time.sleep(1)
    else:
        error_message()


def error_message():
    time.sleep(1)
    print(colors.red + 'An error has been found... restarting game...\n' + colors.reset)
    time.sleep(2)
    game()


game_intro_description()