import time
import sys
import data
import os


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

rows = int(input(typing_print('How many rows would you like on the grid? ', 0.02)))

columns = int(input(typing_print('How many columns would you like on the grid? ', 0.02)))
print()


"""
Creates a grid to play the game
"""
user_grid = []
computer_grid = []

for i in range(rows):
    user_row = []
    computer_row = []
    for j in range(columns):
        user_row.append('-')
        computer_row.append('-')
    user_grid.append(user_row)
    computer_grid.append(computer_row)

def print_grid():
    for i in range(rows):
        print(' | '.join(user_grid[i]) + '      ' + ' | '.join(computer_grid[i]))

print_grid()

























