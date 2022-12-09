# AOC22-C16.py
# Advent of code 2022, challenge 16

rows = 0                    # How many rows of trees
columns = 0                 # How many columns of trees
tree_array = []             # The 2d array of trees
highest_scenic_score = 0    # Number of visible trees (puzzle solution)


def get_scenic_score( xcor, ycor ):
    """Checks if the tree at the passed-in coordinate is visible"""
    top_vis = 0
    bottom_vis = 0
    left_vis = 0
    right_vis = 0

    this_tree = tree_array[xcor][ycor]          # First, grab the value of the tree at the passed-in coordinate

    for xl in range( xcor-1, -1, -1 ):          # If any trees above that tree are the same height or taller,
        top_vis += 1                            # Add 1 to the top visibility
        if tree_array[xl][ycor] >= this_tree:   # If that tree is caller than this_tree, 
            break                               # don't count any more
    for xh in range( xcor+1, rows ):            # Again for the trees below
        bottom_vis += 1
        if tree_array[xh][ycor] >= this_tree:
            break
    for yl in range( ycor-1, -1, -1 ):          # Again for the trees to the left
        left_vis += 1
        if tree_array[xcor][yl] >= this_tree:
            break
    for yh in range( ycor+1, columns ):         # Again for the trees to the right
        right_vis += 1
        if tree_array[xcor][yh] >= this_tree:
            break

    return top_vis * bottom_vis * left_vis * right_vis


with open( "inputd8" ) as f:
    lines = f.readlines()
    columns = len( lines[0] ) - 1

    for l in lines:
        new_row = []
        for num in l:
            if num != '\n':
                new_row.append( int(num) )
        #print( new_row )
        tree_array.append( new_row )
        rows += 1

for x in range( 1, rows-1 ):
    for y in range( 1, columns - 1 ):
        this_ss = get_scenic_score( x, y )
        if this_ss > highest_scenic_score:
            highest_scenic_score = this_ss

print( highest_scenic_score )