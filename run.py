import time
import sys
import data
import os
import random


# list of global variables used

grid_size = 8
user_grid = []
computer_grid = []
user_ships = []
computer_ships = []
computer_shots = []
column_nums = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
USER = ''


def slow_print_effect(text, t):

    """
    Function to substitute the print function to create slow typing effect
    Args: text is for the string that the function prints and "t" is for the
    amount of time we want to delay the printing of the next character
    on the terminal
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


slow_print_effect(data.RULES, 0.02)


while True:
    USER = input(slow_print_effect('Enter your battle name: ', 0.02))

    if USER.isalpha():
        slow_print_effect(f"Welcome {USER}, get ready for battle!", 0.02)
        break
    else:
        slow_print_effect('You must enter a valid name!\n', 0.02)

time.sleep(2)

clear_screen()


print()



def create_grid():
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

def print_grid():

    """
    Function to print the grid
    """
    print(f"     {USER}'s Grid                                  Enemy's Grid")
    for i in range(grid_size):
        print(str(i + 1) + ' ' + ' / '.join(user_grid[i]) + '      ' 
        + str(i + 1) + ' ' + ' / '.join(computer_grid[i]))

def user_ships_position():

    """
    Function to position the user ships on the grid
    """
    for i in range(8):
        while True:
            row_position = random.randint(0, 8 -1)
            column_position = random.randint(0, 8 -1)
            if [row_position, column_position] not in user_ships:
                break
        user_ships.append([row_position, column_position])
        user_grid[row_position][column_position] = '#'


def computer_ships_position():
    """
    Function to generate the computer ships using the same logic as the user ships
    but without showing the ships on the grid
    """
    for i in range(8):
        while True:
            row_position = random.randint(0, 8 -1)
            column_position = random.randint(0, 8 -1)
            if [row_position, column_position] not in computer_ships:
                break
        computer_ships.append([row_position, column_position])




def generate_computer_shot():
    """
    Function to generate computer shots attempt with a random number for row 
    and column
    return: a list of random integers from 0 to 7
    """
    while True:
        row_guess = random.randint(0, grid_size - 1)
        column_guess = random.randint(0, grid_size - 1)
        if [row_guess, column_guess] not in computer_shots:
            break
        computer_shots.append([row_guess, column_guess])
        return [row_guess, column_guess]




def check_computer_shot(guess):
    """
    Function to check if the computer shot it or missed a user ship
    Args: guess is set to define the row and column guess
    """
    row_guess, column_guess = guess
    if [row_guess, column_guess] in user_ships:
        slow_print_effect('The enemy just sunk one of your ships!!!', 0.02)
        user_ships.remove([row_guess, column_guess])
        user_grid[row_guess][column_guess] = 'X'
    else:
        slow_print_effect('Ahahah the enemy ship missed its shot!', 0.02)
        user_grid[row_guess][column_guess] = 'M'



def get_user_shot():

    """
    Function to collect user input for row and column coordinates
    """
    while True:
        try:
            row_guess = int(input('Insert your row coordinates (From 1 to 8): '))
            if row_guess < 1 or row_guess > 5:
                slow_print_effect('Your input MUST be a number between 1 and 8!', 0.02)
            else:
                break
        except ValueError:
            slow_print_effect('Enter a number between 1 and 8', 0.02)
        while True:
            try:
                column = input('Insert your column coordinates (From A to H): ')
                if column not in 'ABCDEFGH':
                    slow_print_effect('Wrong coordinate', 0.02) 
                    slow_print_effect('Enter a capital letter between A to H', 0.02)
                else:
                    column_guess = column_nums[column]
                    break
            except:
                ('Your column coordinate must be a capital letter from A to H', 0.02)
    return [row_guess - 1, column_guess]





def run_game():
    create_grid()
    user_ships_position()
    computer_ships_position()
    print_grid()

run_game()



