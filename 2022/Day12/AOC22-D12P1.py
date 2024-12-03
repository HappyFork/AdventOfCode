# AOC22-D12P1.py
# Advent of code 2022, day 12 part 1


import sys
sys.setrecursionlimit( 2000 )   # This feels wrong. I feel dirty

#FILENAME = "testd12"
FILENAME = "inputd12"


grid = []           # Will hold the grid of characters
path_cache = {}     # Will hold a dictionary of coordinates and their # of steps to E
startx = 0          # Will be X and Y coordinates of 'S'
starty = 0
endx = 0            # X and Y coordinates of 'E'
endy = 0
endord = ord( 'z' ) # ASCII byte value of z (for comparisons later)


def check_path(xcord, ycord, currval, asc = 0):
    # Will check each tile in turn for distance from the end
    cord_string = str(xcord) + "," + str(ycord)
    if asc == 0:
        this_ord_adj = ord( grid[xcord][ycord] ) - 1
    else:
        this_ord_adj = asc - 1
    if cord_string in path_cache and path_cache[cord_string] <= currval:
            return # Don't do extra work
    else:
        print( cord_string )
        path_cache[cord_string] = currval
        if xcord != 0 and ord( grid[xcord-1][ycord] ) >= this_ord_adj:
            check_path( xcord-1, ycord, currval + 1)
        if ycord != 0 and ord( grid[xcord][ycord-1] ) >= this_ord_adj:
            check_path( xcord, ycord-1, currval + 1)
        if xcord < len(grid) - 1 and ord( grid[xcord+1][ycord] ) >= this_ord_adj:
            check_path( xcord+1, ycord, currval + 1)
        if ycord < len(grid[0]) - 1 and ord( grid[xcord][ycord+1] ) >= this_ord_adj:
            check_path( xcord, ycord+1, currval + 1)


# Read the file, create a 2-axis array
with open( FILENAME ) as f:
    for line in f:
        row = []
        for c in line:
            if c != '\n':
                row.append(c)
        grid.append(row)


# Find the starting coordinates
for x in range(len(grid)):
    if 'S' in grid[x]:
        startx = x
        starty = grid[x].index('S')

grid[startx][starty] = 'a'  # Replace S with a, but the coords are saved
startcord_string = str(startx) + "," + str(starty)  # As a string!


# Find the ending coordinates
for x in range(len(grid)):
    if 'E' in grid[x]:
        endx = x
        endy = grid[x].index('E')
# Start the recursive function with the endpoint as 'z'
check_path( endx, endy, 0, ord('z') )


print( path_cache[startcord_string] )
#print( path_cache )