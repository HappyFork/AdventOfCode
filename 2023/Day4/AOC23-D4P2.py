# AOC23-D4P2.py
# Advent of code 2023, day 4 part 2

#FILENAME = "testd4.txt"
FILENAME = "inputd4"

total = 0           # Puzzle solution
cards = {}


def increment_cards( index, amount ):
    if index not in cards.keys():
        cards[index] = amount
    else:
        cards[index] += amount


# Open the file
with open( FILENAME ) as f:
    lines = f.readlines()

    for x in range( 0, len(lines) ):
        cards[x+1] = 1

    for l in lines:
        win = []
        have = []
        cgame = 0

        spl = l.split(":")
        cgame = int( spl[0].split(" ")[-1] )
        nums = spl[1].split("|")
        w_raw = nums[0].strip().split(" ")
        h_raw = nums[1].strip().split(" ")
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
            for i in range( 1, matches + 1 ):
                increment_cards( cgame + i, cards[cgame] )


for x in cards.values():
    total += x
print( total )