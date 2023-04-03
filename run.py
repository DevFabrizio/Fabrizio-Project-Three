import time, sys


def typing_print(text):

    """
    Function to substitute the normal print function to create a slow typing effect
    """

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
  
  
def typing_input(text):
   
    """
    Function to substitute the normal imput function with a slow typing effect 
    """
  
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

typing_print("Welcome to this round of BattleShip!\n In case you have never played this game I will now explain the rules.\n The game will generate a grid and both you and the computer\n will be assigned some ships on this grid.\n You will only be able to see your ships' positions and when prompted you'll have to decide where to fire on the enemy's grid.\n Once you have sunk all the computer's ships you will have won\n but if the enemy sinks all of your ships you will have lost.\n Now get ready and have fun!\n")
print()



