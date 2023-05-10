"""
List of module imports
"""

import time
import sys
import os
import random
import data
import colorama

colorama.init()

# list of global variables used

GRID_SIZE = 8
user_grid = []
computer_grid = []
user_ships = []
computer_ships = []
computer_shots = []
column_nums = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def slow_print_effect(text, timing):

    """
    Function to substitute the print function to create slow typing effect
​
    Args:
        text: the text to print
        timing: the print interval
    """

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(timing)
    return ''


def clear_screen():

    """
    Function to clear the screen
    """
    os.system('clear')


def get_user_battlename():

    """
    Function to get and validate user battle name
    """

    global USER
    while True:
        try:
            USER = input(slow_print_effect('Enter your battle name: \n', 0.02))

            if USER.isalpha():
                slow_print_effect(
                    f"Welcome {USER}, get ready for battle!", 0.02
                )
                print('\n\n\n')
                break
            else:
                slow_print_effect('You must enter a valid name!\n', 0.02)
        except ValueError:
            print(colorama.Fore.RED + 'Error getting user input')


def create_grid():

    """
    Creates a grid to play the game
    """
    global COMPUTER_ROW

    for i in range(GRID_SIZE):
        user_row = []
        COMPUTER_ROW = []
        for j in range(GRID_SIZE):
            user_row.append('-')
            COMPUTER_ROW.append('-')
        user_grid.append(user_row)
        computer_grid.append(COMPUTER_ROW)


def print_grid():

    """
    Function to print the grid
    """

    print(f"     {USER}'s Grid                                  Enemy's Grid")
    print('\n')
    slow_print_effect('  A   B   C   D   E   F   G   H       '
                      ' A   B   C   D   E   F   G   H\n', 0.01)
    for i in range(GRID_SIZE):
        print(str(i + 1) + ' ' + ' / '.join(user_grid[i]) + '      '
              + str(i + 1) + ' ' + ' / '.join(computer_grid[i]))


def user_ships_position():

    """
    Function to position the user ships on the grid
    """

    for i in range(8):
        while True:
            row_position = random.randint(0, 8 - 1)
            column_position = random.randint(0, 8 - 1)
            if [row_position, column_position] not in user_ships:
                break
        user_ships.append([row_position, column_position])
        user_grid[row_position][column_position] = '#'


def computer_ships_position():

    """
    Function to generate the computer ships using the same logic
    as the user ships
    but without showing the ships on the grid
    """

    for i in range(8):
        while True:
            row_position = random.randint(0, 8 - 1)
            column_position = random.randint(0, 8 - 1)
            if [row_position, column_position] not in computer_ships:
                break
        computer_ships.append([row_position, column_position])


def generate_computer_shot():

    """
    Function to generate computer shots attempt with a random number for row
    and column
    Return:
        a list of random integers from 0 to 7
    """

    while True:
        row_guess = random.randint(0, GRID_SIZE - 1)
        column_guess = random.randint(0, GRID_SIZE - 1)
        if [row_guess, column_guess] not in computer_shots:
            break
    computer_shots.append([row_guess, column_guess])
    return [row_guess, column_guess]


def check_computer_shot(guess):

    """
    Function to check if the computer shot it or missed a user ship
    Args:
        guess is set to define the row and column guess
    """

    row_guess, column_guess = guess
    if [row_guess, column_guess] in user_ships:
        slow_print_effect('The enemy just sunk one of your ships!!!\n', 0.02)
        user_ships.remove([row_guess, column_guess])
        user_grid[row_guess][column_guess] = 'X'
    else:
        slow_print_effect('Ahahah the enemy ship missed its shot!\n', 0.02)
        user_grid[row_guess][column_guess] = 'M'


def get_user_shot():

    """
    Function to collect user input for row and column coordinates
    Returns:
        list of row and column guess
    """

    while True:
        try:
            row_guess = int(input('Insert your row coordinates'
                                  '(From 1 to 8): \n'))
            if row_guess < 1 or row_guess > 8:
                slow_print_effect('Your input MUST be a number'
                                  'between 1 and 8!\n', 0.02)
            else:
                break
        except ValueError:
            slow_print_effect('Enter a number between 1 and 8\n', 0.02)

    while True:
        try:
            column = input('Insert your column coordinates (From A to H): \n')
            if column not in 'ABCDEFGH':
                slow_print_effect('Wrong coordinate\n', 0.02)
                slow_print_effect('Enter a capital letter'
                                  'between A to H\n', 0.02)
            else:
                column_guess = column_nums[column]
                break
        except KeyError:
            ('Your column coordinate must be a'
             'capital letter from A to H\n', 0.02)
    return [row_guess - 1, column_guess]


def check_user_shot(guess):

    """
    Function to check the user guess
    Args:
        guess is set to define row and column guess
    """

    row_guess, column_guess = guess
    if [row_guess, column_guess] in computer_ships:
        print(colorama.Fore.GREEN + "That's a hit! Well done!\n")
        print(colorama.Fore.RESET)
        computer_ships.remove([row_guess, column_guess])
        computer_grid[row_guess][column_guess] = 'H'
        return True
    else:
        print(colorama.Fore.RED + 'You missed!\n')
        print(colorama.Fore.RESET)
        computer_grid[row_guess][column_guess] = 'M'


def play_another_round():

    """
    Function to play another round
    through user input request
    """

    next_round = input(slow_print_effect('Do you want to play another round?'
                                         '("yes" or "no") \n', 0.02)).lower()
    if next_round == 'yes':
        run_game()
    elif next_round == 'no':
        slow_print_effect('Exiting the game...', 0.04)
        time.sleep(2)
        clear_screen()
    else:
        slow_print_effect('Please input "yes" or "no"\n', 0.02)
        play_another_round()


def run_game():

    """
    Function to run the game.
    Within are called the functions to print the rules
    get the user input for the name
    create the grid and print the grid to the terminal.
    """

    slow_print_effect(data.RULES, 0.02)
    get_user_battlename()
    time.sleep(1)
    clear_screen()
    create_grid()
    user_ships_position()
    computer_ships_position()
    print_grid()
    guess_attempt = 0

    while True:
        guess = get_user_shot()
        guess_attempt += 1
        if check_user_shot(guess):
            if not computer_ships:
                slow_print_effect(f"It took you {guess_attempt}"
                                  f"shots to sink all the enemy's ships!\n"
                                  f"You've won the battle", 0.02)
                break
        cpu_guess_position = generate_computer_shot()
        check_computer_shot(cpu_guess_position)

        if not user_ships:
            slow_print_effect(f"The enemy sunk your ships in"
                              f"{guess_attempt} turns"
                              f" You have lost this battle!", 0.02)
            break
        time.sleep(2)
        clear_screen()
        print_grid()


run_game()
play_another_round()
