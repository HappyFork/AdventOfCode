# AOC22-D15P1.py
# Advent of code 2022, day 15 part 1

FILENAME = "testd15"
#FILENAME = "inputd15"


with open( FILENAME ) as f:
    line = f.readline()
    sxi = line.find("=") + 1
    digits = 0
    for c in range( sxi, len(line) ):
        if line[c].isdecimal() or line[c] == '-':
            digits += 1
        else:
            break
    sx = line[sxi:sxi+digits]
    print( sx )
    print( line[sxi+digits:] )