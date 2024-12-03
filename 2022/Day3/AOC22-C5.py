# AOC22-C5.py
# Advent of code 2022, challenge 5

import string                           # Used in assign_priority to see if character is uppercase or lowercase

priority_sum = 0                        # Holds sum of all priorities

def assign_priority( c ):               # Function to assign a priority to each character
    v = ord(c)                          # Ascii value of passed in character
    # Python has this neato built in function to get the ascii value of a character.

    if c in string.ascii_uppercase:     # Letters A-Z should return 27-52 in order
        temp = ord("A") - 1
        return v - temp + 26
    elif c in string.ascii_lowercase:   # Letters a-z should return 1-26 in order
        temp = ord("a") - 1
        return v - temp
    else:
        # This shouldn't happen. Error
        print( "You fucked up somehow" )
        return 0

with open( "inputd3" ) as f:            # Open input file

    lines = f.readlines()               # Get lines

    for l in lines:                     # For each line

        common_char = ""
        csiz = int(len(l.strip()) / 2)  # Get half of the length.
        # I'm heavily relying on built in python functions here. .strip() removes
        # the newline '\n' at the end of each line, len() returns the length as an
        # int, and then int() transforms the whole thing back into an int. I guess
        # by dividing by 2 (not even 2.0?) the number is converted to a float.

        c1 = l.strip()[:csiz]           # The first half of the string in compartment 1
        c2 = l.strip()[csiz:]           # The second half in compartment 2

        for char in c1:                 # For each character in compartment 1
            if char in c2:              # If it's also in compartment 2,
                common_char = char      # We found the common character
                break
        
        priority_sum += assign_priority( common_char )

print( priority_sum )