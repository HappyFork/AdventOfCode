# AOC23-D4P2.py
# Advent of code 2023, day 4 part 2

#FILENAME = "testd4.txt"
FILENAME = "inputd4"

total = 0           # Puzzle solution
cards = {}


# Open the file
with open( FILENAME ) as f:
    lines = f.readlines()

    for x in range( 0, len(lines) ):
        cards[x+1] = 1

    for l in lines:
        win = []
        have = []

        spl = l.split(":")[1]
        spl = spl.split("|")
        w_raw = spl[0].strip().split(" ")
        h_raw = spl[1].strip().split(" ")
        for x in w_raw:
            if x != '':
                win.append( int(x) )
        for x in h_raw:
            if x != '':
                have.append( int(x) )
        
        matches = 0
        for n in have:
            if n in win:
                matches += 1
        
        if matches != 0:
            total += 2**(matches - 1)


print( total )