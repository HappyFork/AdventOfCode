# AOC22-C15.py
# Advent of code 2022, challenge 15

rows = 0            # How many rows of trees
columns = 0         # How many columns of trees
tree_array = []     # The 2d array of trees
visible_trees = 0   # Number of visible trees (puzzle solution)

def is_tree_vis( xcor, ycor ):
    """Checks if the tree at the passed-in coordinate is visible"""
    top_vis = True                              # If the tree is visible from any direction,
    bottom_vis = True                           # It's visible, so this function will only
    left_vis = True                             # return false if all of these are false
    right_vis = True

    this_tree = tree_array[xcor][ycor]          # First, grab the value of the tree at the passed-in coordinate

    for xl in range( xcor ):                    # If any trees above that tree are the same height or taller,
        if tree_array[xl][ycor] >= this_tree:    # the tree isn't visible.
            top_vis = False                     # Set top_vis to false
    for xh in range( xcor+1, rows ):            # Again for the trees below
        if tree_array[xh][ycor] >= this_tree:
            bottom_vis = False
    for yl in range( ycor ):                    # Again for the trees to the left
        if tree_array[xcor][yl] >= this_tree:
            left_vis = False
    for yh in range( ycor+1, columns ):         # Again for the trees to the right
        if tree_array[xcor][yh] >= this_tree:
            right_vis = False
    return top_vis or bottom_vis or left_vis or right_vis


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

visible_trees += rows * 2
visible_trees += (columns-2) * 2
for x in range( 1, rows-1 ):
    for y in range( 1, columns - 1 ):
        if is_tree_vis( x, y ):
            visible_trees += 1
print( visible_trees )