# AOC22-D17P1.py
# Advent of code 2022, day 17 part 1

FILENAME = "testd17"
#FILENAME = "inputd17"


rocks = [
    [[1,1,1,1]],
    [[0,1,0],[1,1,1],[0,1,0]],
    [[1,1,1],[0,0,1],[0,0,1]],
    [[1],[1],[1],[1]],
    [[1,1],[1,1]]
]
rock_ind = 0
vent_ind = 0
tower = {0: [1,1,1,1,1,1,1]}
falling_rock_pos = [4,2]
rocks_fell = 0
top = 0


def get_row( r, rind, rpos ):
    global rocks

    row = []
    if r in tower.keys():
        row = tower[r]
    else:
        row = [0,0,0,0,0,0,0]
    
    for x in range( len(rocks[rind]) ):
        if r == rpos[0] + x:
            for y in range( len(rocks[rind][x]) ):
                if rocks[rind][x][y] == 1:
                    row[rpos[1]+y] = 1
    
    return row


with open( FILENAME ) as f:
    vent_pattern = f.read()


while rocks_fell < 2022:
    # Move the rock per the vent
    match vent_pattern[vent_ind]:
        case '>':
            # Check if the rock can move right
            move_right = True           # By default, yes
            if len( rocks[rock_ind][0] ) + falling_rock_pos[1] >= 7:
                move_right = False      # Not if it would go into the wall
            for x in range(len(rocks[rock_ind])):   # For each row in the rock
                # If the rock can still move right (no point checking otherwise), and the row in the tower contains other rocks,
                # and there is a rock to the right of the falling rock, and the falling rock doesn't have an empty space in that position
                if move_right and x+falling_rock_pos[0] in tower.keys() and tower[x+falling_rock_pos[0]][falling_rock_pos[1]+len(rocks[rock_ind][0])] == 1 and rocks[rock_ind][x][-1] == 1:
                    move_right = False  # Then the rock bumps into the other rock and can't move 
                # If the rock can still move right (no point checking otherwise), and the falling rock is the plus sign rock,
                # and the row in the tower contains other rocks, and there is a rock in the rightmost position in the row
                # (this only works because the plus sign rocks' partially empty rows have exactly 1 empty space on either side)
                if move_right and rock_ind == 1 and x+falling_rock_pos[0] in tower.keys() and tower[x+falling_rock_pos[0]][falling_rock_pos[1]+len(rocks[rock_ind][0])-1] == 1:
                    move_right = False  # Then the rock bumps into the other rock and can't move 
            if move_right:              # If it can move right,
                falling_rock_pos[1] +=1 # It does
                #print( "Rock was pushed right" )
            #else:
                #print( "Rock attempted to move right, but did not have space" )
        case '<':
            # Check if the rock can move left
            move_left = True            # By default, yes
            if falling_rock_pos[1] <= 0:
                move_left = False       # Not if it would go into the wall
            for x in range(len(rocks[rock_ind])):   # For each row in the rock
                # If the rock can still move left (no point checking otherwise), and the row in the tower contains other rocks,
                # and there is a rock to the left of the falling rock, and the falling rock doesn't have an empty space in that position
                if move_left and x+falling_rock_pos[0] in tower.keys() and tower[x+falling_rock_pos[0]][falling_rock_pos[1]-1] == 1 and rocks[rock_ind][x][0] == 1:
                    move_left = False   # Then the rock bumps into the other rock and can't move 
                # If the rock can still move left (no point checking otherwise), and the falling rock is the plus sign rock,
                # and the row in the tower contains other rocks, and there is a rock in the leftmost position in the row
                # (this only works because the plus sign rocks' partially empty rows have exactly 1 empty space on either side)
                if move_left and rock_ind == 1 and x+falling_rock_pos[0] in tower.keys() and tower[x+falling_rock_pos[0]][falling_rock_pos[1]] == 1:
                    move_left = False   # Then the rock bumps into the other rock and can't move 
            if move_left:               # If the rock can move left,
                falling_rock_pos[1] -=1 # It does
                #print( "Rock was pushed left" )
            #else:
                #print( "Rock attempted to move left, but did not have space" )

    # Move the rock down
    if falling_rock_pos[0] > top + 1:
        falling_rock_pos[0] -= 1
    else:
        stop = False
        belrow = tower[falling_rock_pos[0] - 1]
        for y in range( len(rocks[rock_ind][0]) ):
            if rocks[rock_ind][0][y] == 1 and belrow[y+falling_rock_pos[1]] == 1:
                stop = True
        if not stop and rock_ind == 1 and falling_rock_pos[0] in tower.keys():
            #print( "Ran" )
            botrow = tower[falling_rock_pos[0]]
            if rocks[rock_ind][1][y] == 1 and botrow[y+falling_rock_pos[1]] == 1:
                stop = True
        if stop:
            #print( falling_rock_pos )
            # The rock comes to a rest
            # Add the rows to tower
            for x in range( len(rocks[rock_ind]) ):
                tower[x+falling_rock_pos[0]] = get_row( x+falling_rock_pos[0], rock_ind, falling_rock_pos )
            # Find the new top of the tower
            top = max( tower.keys() )
            #print( top )
            # Get the next rock started
            if rock_ind + 1 >= len(rocks):
                rock_ind = 0
            else:
                rock_ind += 1
            falling_rock_pos = [top+4,2]
            # And increment the number of rocks that have fallen
            rocks_fell += 1
        else:
            falling_rock_pos[0] -= 1

    # Increment the vent pattern
    if vent_ind + 1 >= len(vent_pattern):
        vent_ind = 0
        #print( "Vent reset" )
    else:
        vent_ind += 1


for l in tower.__reversed__():
    print( f"Row {l}: {tower[l]}" )
print( max( tower.keys() ) )