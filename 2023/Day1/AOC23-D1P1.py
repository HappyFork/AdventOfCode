# AOC23-D1P1.py
# Advent of code 2023, day 1 part 1

#FILENAME = "testd1"
FILENAME = "inputd1"


total = 0

# Open the file
with open( FILENAME ) as f:
    # Get each line
    lines = f.readlines()
    for l in lines:
        nchars = ""     # Characters making up the target number

        # Find the first digit
        for c in l:
            if c in "0123456789":
                print( c, end='' )
                nchars = nchars + c
                break

        # Find the second digit
        for c in range( -2,-len(l)-1, -1):
            if l[c] in "0123456789":
                print( l[c] )
                nchars += l[c]
                break
        
        # Add target to total
        total += int(nchars)

print( total )