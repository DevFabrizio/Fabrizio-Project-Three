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




