"""Liam Meisinger's Morse code converter"""
"""The goal is to create a command line program that converts any text into morse code. 
For all the secret spy missions :)"""

"""Imports"""
from logo import logo
from data import decode, encode

# Logo for fun and a better UI experience
print(logo)


# define functions
def text_to_morse(text):
    morse_code = ""
    for char in text:
        if char in encode:
            morse_code += encode[char] + ' '
        else:
            morse_code += ' '  #incase there is a char not in my dictioanry
    return morse_code


def morse_to_text(morse_code):
    text_out = ''
    morse_code = morse_code.split(' ')
    for char in morse_code:
        if char in decode:
            text_out += decode[char]
        else:
            text_out += ' '
    return text_out


# Loop to ensure the program continues to run until stopped
should_continue = True
while should_continue:
    user_input = input("Would you like to encode, decode or terminate the session? 'E' for encode, "
                       "'D' for decode and 'T' to terminate.\n").upper()
    if user_input == 'T':
        should_continue = False
    elif user_input == 'E':
        text = input('Message to encode:\n').upper()
        print(text_to_morse(text))
    elif user_input == 'D':
        morse_code = input('Message to decode:\n')
        print(morse_to_text(morse_code))
    else:
        print("Invalid choice. Please enter 'E', 'D', or 'T'.")
