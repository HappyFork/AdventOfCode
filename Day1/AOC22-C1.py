# AOC22-C1.py
# Advent of code 2022, challenge 1

max = 0 # Will hold the largest sum in the set

with open( "inputd1" ) as f:        # Open the file as f

    lines = f.readlines()           # Read the lines into lines
    csum = 0                        # This will be the sum of the current block of lines

    for l in lines:                 # For each line in lines
        if l.strip() == "":         # If it's a new line, that's the end of the block
            if csum > max:          # If this sum is the biggest yet,
                max = csum          # Replace max
            csum = 0                # Then, reset csum
        else:                       # If it's a number,
            csum += int( l.strip() )# Add it to current sum

# I believe when the file ends it won't do a last max check so
if csum > max:
    max = csum
# Probably not the most efficient way to do this but whatever.

print( max )