# AOC23-D2P1.py
# Advent of code 2023, day 2 part 1

#FILENAME = "testd2.txt"
FILENAME = "inputd2"


total = 0       # Puzzle solution. Sum of possible line IDs

# Open the file
with open( FILENAME ) as f:
    # Get each line
    lines = f.readlines()
    for l in lines:
        spl = l.split(":",1)                # First split, 0 is game #, 1 is the rest of the line
        number = spl.pop(0).split(" ")[1]   # Get the game number of this line
        possible = True                     # Flag for if the line is possible (default = it is)
        rounds = spl[0].split(";")          # Get the rounds from the rest of the line
        for r in rounds:                    # For each line,
            cubes = r.split(",")            # Get the cubes of different colors pulled
            for c in cubes:                 # Cube lists have 2 parts: the color and the number
                cs = c.strip()              # First, strip whitespace
                t = cs.split(" ")           # Then split into color (1) and number (0)
                if t[1] == "blue" and int(t[0]) > 14:
                    possible = False        # If more than 14 blues, not possible
                elif t[1] == "red" and int(t[0]) > 12:
                    possible = False        # If more than 12 reds, not possible
                elif t[1] == "green" and int(t[0]) > 13:
                    possible = False        # If more than 13 greens, not possible
        if possible:                        # If the line is possible,
            total += int(number)            # Ad the ID to the total
        

print( total )