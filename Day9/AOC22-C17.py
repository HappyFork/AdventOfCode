# AOC22-C17.py
# Advent of code 2022, challenge 17

tail_spots = set()
head_pos = [0, 0]
tail_pos = [0, 0]


def rope_step( dir, hp, tp ):
    #print( "head is at: ", hp )
    #print( "tail is at: ", tp )
    start_head_pos = hp.copy()
    #print( "start head is at: ", start_head_pos )

    # Move the head in the specified direction
    match dir:
        case 'U':
            hp[1] += 1
        case 'D':
            hp[1] -= 1
        case 'L':
            hp[0] -= 1
        case 'R':
            hp[0] += 1
    
    # Then move the tail if it's no longer adjacent to head
    #print( "head is at: ", hp )
    #print( "tail is at: ", tp )
    #print( tp[0], " minus ", hp[0], " is ", abs(tp[0] - hp[0]) )
    #print( tp[1], " minus ", hp[1], " is ", abs(tp[1] - hp[1]) )
    if abs(tp[0]-hp[0]) > 1 or abs(tp[1]-hp[1]) > 1:
        #print( "tp will become ", start_head_pos )
        #tp = start_head_pos.copy()
        tp[0] = start_head_pos[0]
        tp[1] = start_head_pos[1]
        #print( "tail is now at: ", tp )

    # Then add tail_pos to the tail_spots set
    tail_spots.add( str(tp[0]) + str(tp[1]) )


with open( "inputd9" ) as f:
#with open( "testd9.txt" ) as f:
    lines = f.readlines()
    for l in lines:
        instruction = l.strip().split()
        instruction[1] = int( instruction[1] )
        for x in range( instruction[1] ):
            rope_step( instruction[0], head_pos, tail_pos )

#print( tail_spots )
print( len(tail_spots) )