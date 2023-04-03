import time,sys

"""
Function to substitute the normal print function in order to create a slow typing effect
"""

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
  
