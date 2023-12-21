# AOC23-D7P2.py
# Advent of code 2023, day 7 part 2


#FILENAME = "testd7.txt"
FILENAME = "inputd7"


hands = {}
priority = "AKQT98765432J"


# Function to bubble sort a given array according to the priority
def bsort( arr ):
    for i in range( 0, len(arr)-1 ):
        for j in range( 0, len(arr)-i-1 ):
            for c in range( 0, len(arr[j]) ):
                if priority.find( arr[j][c] ) > priority.find( arr[j+1][c] ):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    break
                elif priority.find( arr[j][c] ) < priority.find( arr[j+1][c] ):
                    break


# Open the file
with open( FILENAME ) as f:
    lines = f.readlines()
    for l in lines:
        hands[ l[:5] ] = [ int(l[6:]), 0 ]


cur_rank = len( hands )     # Current rank number being assigned

# Find all the five-of-a-kinds
s5oak = []
for h in hands.keys():
    counts = ""
    for c in h:
        counts += str( h.count(c) )
    if h.count( h[0] ) == 5:
        s5oak.append( h )
    elif str( 5-h.count("J") ) in counts:
        s5oak.append( h )
# Sort the five-of-a-kinds
if len(s5oak) > 1:
    bsort(s5oak)
# Assign ranks
for h in s5oak:
    hands[h][1] = cur_rank
    cur_rank -= 1

# Find all the four-of-a-kinds
s4oak = []
for h in hands.keys():
    if h not in s5oak:
        counts = ""
        for c in h:
            counts += str( h.count(c) )
        if "4" in counts:
            s4oak.append( h )
        elif str( 4-h.count("J") ) in counts and counts.count("1") == 1:
            s4oak.append( h )
# Sort the four-of-a-kinds
if len(s4oak) > 1:
    bsort(s4oak)
# Assign ranks
for h in s4oak:
    hands[h][1] = cur_rank
    cur_rank -= 1

# Find the full houses and the three-of-a-kinds
sfullh = []
s3oak = []
for h in hands.keys():
    if h not in s5oak and h not in s4oak:
        counts = ""
        for c in h:
            counts += str( h.count(c) )
        if "3" in counts:
            if "2" in counts:
                sfullh.append( h )
            else:
                s3oak.append( h )
        elif str( 3-h.count("J") ) in counts:
            if counts.count("1") == 1:
                sfullh.append( h )
            else:
                s3oak.append( h )
# Sort the arrays
if len(sfullh) > 1:
    bsort(sfullh)
if len(s3oak) > 1:
    bsort(s3oak)
# Assign ranks
for h in sfullh:
    hands[h][1] = cur_rank
    cur_rank -= 1
for h in s3oak:
    hands[h][1] = cur_rank
    cur_rank -= 1

# Find the two pairs and one pairs
s2pair = []
s1pair = []
for h in hands.keys():
    if h not in s5oak and h not in s4oak and h not in sfullh and h not in s3oak:    # A faster way to check this would be to check if hands[h][1] == 0
        counts = ""
        for c in h:
            counts += str( h.count(c) )
        if counts.count( "2" ) == 4:
            s2pair.append( h )
        elif counts.count( "2" ) == 2 or "J" in h:
            s1pair.append( h )
# Sort the arrays
if len(s2pair) > 1:
    bsort(s2pair)
if len(s1pair) > 1:
    bsort(s1pair)
# Assign ranks
for h in s2pair:
    hands[h][1] = cur_rank
    cur_rank -= 1
for h in s1pair:
    hands[h][1] = cur_rank
    cur_rank -= 1

# Now, the last set
left = []
for h in hands.keys():
    if h not in s5oak and h not in s4oak and h not in sfullh and h not in s3oak and h not in s2pair and h not in s1pair:
        left.append( h )
if len(left) > 1:
        bsort(left)
for h in left:
    hands[h][1] = cur_rank
    cur_rank -= 1

total = 0
for h in hands.values():
    total += h[0] * h[1]

print( total )