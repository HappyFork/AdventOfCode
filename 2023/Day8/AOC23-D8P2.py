# AOC23-D8P1.py
# Advent of code 2023, day 8 part 2


#FILENAME = "testd83.txt"
FILENAME = "inputd8"


nodes = {}
directions = ""
step = 0


# Open the file
with open( FILENAME ) as f:
    directions = f.readline().strip()
    f.readline()
    for l in f.readlines():
        curr_line = l.split()
        nodes[curr_line[0]] = ( curr_line[2][1:4], curr_line[3][:3] )

starts = []
steps = []

for k in nodes.keys():
    if k[-1] == "A":
        starts.append( k )

for l in starts:
    curr_loc = l
    looking = True
    index = 0
    step = 0
    while( looking ):
        if curr_loc[-1] == "Z":
            looking = False
        else:
            if directions[index] == "L":
                curr_loc = nodes[curr_loc][0]
            elif directions[index] == "R":
                curr_loc = nodes[curr_loc][1]
            step += 1
            if index >= len( directions )-1:
                index = 0
            else:
                index += 1
    steps.append( step )


print( steps )