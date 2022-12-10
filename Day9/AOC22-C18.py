# AOC22-C18.py
# Advent of code 2022, challenge 18

import copy

tail_spots = set()
rope = [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]


def rope_step( dir, rp ):
    start_rope = copy.deepcopy(rp)

    # Move the head in the specified direction
    match dir:
        case 'U':
            rp[0][1] += 1
        case 'D':
            rp[0][1] -= 1
        case 'L':
            rp[0][0] -= 1
        case 'R':
            rp[0][0] += 1
    
    # Then move the rest of the rope to be adjacent to the previous section
    for x in range( 1, len(rp) ):
        if abs(rp[x][0]-rp[x-1][0]) > 1 and rp[x][1] == rp[x-1][1]:
            rp[x][0] = start_rope[x-1][0]
        elif abs(rp[x][1]-rp[x-1][1]) > 1 and rp[x][0] == rp[x-1][0]:
            rp[x][1] = start_rope[x-1][1]
        elif abs(rp[x][0]-rp[x-1][0]) > 1 or abs(rp[x][1]-rp[x-1][1]) > 1:
            if rp[x-1][0] > rp[x][0]:
                rp[x][0] += 1
            else:
                rp[x][0] -= 1
            if rp[x-1][1] > rp[x][1]:
                rp[x][1] += 1
            else:
                rp[x][1] -= 1
            #rp[x][0] = start_rope[x-1][0]
            #rp[x][1] = start_rope[x-1][0]

    #if abs(tp[0]-hp[0]) > 1 or abs(tp[1]-hp[1]) > 1:
    #    tp[0] = start_head_pos[0]
    #    tp[1] = start_head_pos[1]

    # Then add tail_pos to the tail_spots set
    #print( str(rp[8][0]) + str(rp[8][1]) )
    tail_spots.add( str(rp[8][0]) + str(rp[8][1]) )


with open( "inputd9" ) as f:
    lines = f.readlines()
    for l in lines:
        instruction = l.strip().split()
        instruction[1] = int( instruction[1] )
        for x in range( instruction[1] ):
            rope_step( instruction[0], rope )

#print( tail_spots )
print( len(tail_spots) )