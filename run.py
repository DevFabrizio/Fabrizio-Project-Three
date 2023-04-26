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

grid_size = 8
user_grid = []
computer_grid = []
user_ships = []
computer_ships = []

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
def user_ship_position():
    for i in range(5):
        while True:
            row_position = random.randint(0, 5 -1)
            column_position = random.randint(0, 5 -1)
            if [row_position, column_position] not in user_ships:
                break
        user_ships.append([row_position, column_position])
        user_grid[row_position][column_position] = '#'











