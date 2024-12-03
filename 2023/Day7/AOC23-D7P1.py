# AOC23-D7P1.py
# Advent of code 2023, day 7 part 1


#FILENAME = "testd7.txt"
FILENAME = "inputd7"


hands = {}
priority = "AKQJT98765432"


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
    if h.count( h[0] ) == 5:
        s5oak.append( h )
        break
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
    for c in h:
        if h not in s5oak and h.count(c) == 4:
            s4oak.append( h )
            break
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

# I think the above method is the best, and I could
# optimize this whole thing using that method, but I'm
# lazy and really just focused on completing the puzzles

# Find the two pairs and one pairs
s2pair = []
s1pair = []
for h in hands.keys():
    if h not in s5oak and h not in s4oak and h not in sfullh and h not in s3oak:
        counts = ""
        for c in h:
            counts += str( h.count(c) )
        if counts.count( "2" ) == 4:
            s2pair.append( h )
        elif counts.count( "2" ) == 2:
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