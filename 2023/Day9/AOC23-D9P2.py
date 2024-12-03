# AOC23-D9P2.py
# Advent of code 2023, day 9 part 2


#FILENAME = "testd9.txt"
FILENAME = "inputd9"


total = 0


def prev_value( list ):
    new_list = [ list[x]-list[x-1] for x in range( 1, len(list)) ]
    if new_list.count( 0 ) != len(new_list):
        return new_list[0] - prev_value( new_list )
    else:
        return 0


# Open the file
with open( FILENAME ) as f:
    for l in f.readlines():
        numbers = [ int(x) for x in l.split() ]
        total += numbers[0] - prev_value( numbers )


print( total )