import time
import sys
import data


def typing_print(text, t):

    """
    Function to substitute the print function to create slow typing effect
    """

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(t)
    return ''


# def typing_input(text, t):

#     """
#     Function to substitute the normal imput function with a slow 
#     typing effect
#     """

#     for character in text:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(t)
#     value = input()
#     return value


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