# AOC22-C17.py
# Advent of code 2022, challenge 17

tail_spots = set()
head_pos = [0, 0]
tail_pos = [0, 0]


def rope_step( dir, hp, tp ):
    start_head_pos = hp.copy()

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
    if abs(tp[0]-hp[0]) > 1 or abs(tp[1]-hp[1]) > 1:
        tp[0] = start_head_pos[0]
        tp[1] = start_head_pos[1]

    # Then add tail_pos to the tail_spots set
    tail_spots.add( str(tp[0]) + str(tp[1]) )


with open( "inputd9" ) as f:
    lines = f.readlines()
    for l in lines:
        instruction = l.strip().split()
        instruction[1] = int( instruction[1] )
        for x in range( instruction[1] ):
            rope_step( instruction[0], head_pos, tail_pos )

print( len(tail_spots) )