# AOC22-C7.py
# Advent of code 2022, challenge 7

overlaps = 0

with open( "inputd4" ) as f:            # Open input file
    
    lines = f.readlines()               # Read in lines

    for l in lines:                     # For each line

        areas = l.split(",")            # First split it by the comma
        a1 = areas[0]                   # a1 and a2 represent the assigned
        a2 = areas[1]                   # areas for each pair

        a1range = a1.split("-")         # Then split each area by the hyphen
        a2range = a2.split("-")         # These will hold an array with the first and last area

        for i in range( len(a1range) ):
            a1range[i] = int( a1range[i] )
        for i in range( len(a2range) ):
            a2range[i] = int( a2range[i] )

        # This solution only works because all the ranges have the smaller value first. If this was
        # like 10% more complex it would take me way longer.

        if a1range[0] > a2range[0]:     # If the first number in elf 1's range is greater,
            if a1range[1] <= a2range[1]:
                overlaps += 1
        elif a1range[0] < a2range[0]:   # If the first number in elf 2's range is greater,
            if a1range[1] >= a2range[1]:
                overlaps += 1
        else:                           # If the first numbers are equal
            overlaps += 1

print( overlaps )