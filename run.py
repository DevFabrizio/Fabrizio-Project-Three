import time
import sys
import data
import os
import random


def typing_print(text, t):

    """
    Function to substitute the print function to create slow typing effect
    """

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(t)
    return ''


def clear_screen():
    """
    Function to clear the screen
    """
    os.system('clear')


typing_print(data.RULES, 0.02)

USER = ''

while True:
    USER = input(typing_print('Enter your battle name: ', 0.02))

    if USER.isalpha():
        typing_print(f"Welcome {USER}, get ready for battle!", 0.02)
        break
    else:
        typing_print('You must enter a valid name!\n', 0.02)

time.sleep(2)

clear_screen()


print()


print()

grid_size = 8
user_grid = []
computer_grid = []
user_ships = []
computer_ships = []
computer_shots = []

"""
Creates a grid to play the game
"""

for i in range(grid_size):
    user_row = []
    computer_row = []
    for j in range(grid_size):
        user_row.append('-')
        computer_row.append('-')
    user_grid.append(user_row)
    computer_grid.append(computer_row)

"""
Function to print the grid
"""

def print_grid():
    print(f"     {USER}'s Grid                                   Enemy's Grid")
    for i in range(grid_size):
        print(str(i + 1) + ' ' + ' / '.join(user_grid[i]) + '      ' + str(i + 1) + ' ' + ' / '.join(computer_grid[i]))

print_grid()

"""
Function to position the user ships on the grid
"""
def user_ships_position():
    for i in range(5):
        while True:
            row_position = random.randint(0, 5 -1)
            column_position = random.randint(0, 5 -1)
            if [row_position, column_position] not in user_ships:
                break
        user_ships.append([row_position, column_position])
        user_grid[row_position][column_position] = '#'


"""
Function to generate the computer ships using the same logic as the user ships
but without showing the ships on the grid
"""
def computer_ships_position():
    for i in range(5):
        while True:
            row_position = random.randint(0, 5 -1)
            column_position = random.randint(0, 5 -1)
            if [row_position, column_position] not in computer_ships:
                break
        computer_ships.append([row_position, column_position])


"""
Function to generate computer shots attempt with a random number for row 
and column
"""


def computer_shot():
    while True:
        row_guess = random.randint(0, grid_size - 1)
        column_guess = random.randint(0, grid_size - 1)
        if [row_guess, column_guess] not in computer_shots:
            break
        computer_shots.append([row_guess, column_guess])
        return [row_guess, column_guess]


"""
Function to check if the computer shot it or missed a user ship
"""


def check_computer_shot(guess):
    row_guess, column_guess = guess
    if [row_guess, column_guess] in user_ships:
        typing_print('The enemy just sunk one of your ships!!!', 0.02)
        user_ships.remove([row_guess, column_guess])
        user_grid[row_guess][column_guess] = 'X'
    else:
        typing_print('Ahahah the enemy ship missed its shot!', 0.02)
        user_grid[row_guess][column_guess] = 'M'

"""
Global variable to transform the column letter in integers
"""

column_nums = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

"""
Function to collect user input for row and column coordinates
"""

def user_shot():
    while True:
        try:
            row_guess = int(input('Insert your row coordinates (Number from 1 to 8): '))
            if row_guess < 1 or row_guess > 5:
                typing_print('Your input MUST be a number between 1 and 8!', 0.02)
            else:
                break
        except ValueError:
            typing_print('Enter a number between 1 and 8', 0.02)
        while True:
        try:
            column = input('Insert your column coordinates (Letter from A to H): ')
            if column not in 'ABCDEFGH':
                typing_print('Wrong coordinate. Enter a capital letter between A to H', 0.02)
            else:
                column_guess = column_nums[column]
                break
        except:
            typing_print('Your column coordinate must be a capital letter from A to H', 0.02)
    return [row_guess - 1, column_guess]





def run_game():



