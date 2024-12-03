# AOC23-D8P1.py
# Advent of code 2023, day 8 part 1


#FILENAME = "testd82.txt"
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


looking = True
index = 0
curr_loc = "AAA"
while( looking ):
    if curr_loc == "ZZZ":
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

print( step )