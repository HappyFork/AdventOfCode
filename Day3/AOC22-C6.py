# AOC22-C6.py
# Advent of code 2022, challenge 6

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
        # This shouldn't happen. Error.
        print( "You fucked up somehow" )
        return 0

with open( "inputd3" ) as f:            # Open input file

    line1 = f.readline()                # Get 3 lines
    line2 = f.readline()
    line3 = f.readline()

    while line1 != "" and line2 != "" and line3 != "":
        common_char = ""

        for char in line1:
            if (char in line2) and (char in line3):
                common_char = char
                break
        
        priority_sum += assign_priority( common_char )

        line1 = f.readline()            # Get the next 3 lines
        line2 = f.readline()
        line3 = f.readline()

print( priority_sum )