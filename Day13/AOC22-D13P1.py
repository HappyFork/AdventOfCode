# AOC22-D13P1.py
# Advent of code 2022, day 13 part 1

FILENAME = "testd13"
#FILENAME = "inputd13"


correct_order = 0


def check_list( l, r ):
    if len(l) < len(r):
        ret_val = 1
    elif len(l) > len(r):
        ret_val = -1
    else:
        ret_val = 0

    for j, k in zip( l, r ):
        if isinstance( j, list ) and isinstance( k, list ):
            check_list( j, k )
        elif isinstance( j, list ):
            k_list = [k]
            check_list( j, k_list )
        elif isinstance( k, list ):
            j_list = [j]
            check_list( j_list, k )
        else:
            if j < k:
                return 1
            elif j > k:
                return -1
    return ret_val


with open( FILENAME ) as f:
    reading = True
    while reading:
        # Read the next two lines
        left = eval(f.readline().strip())
        right = eval(f.readline().strip())

        # Compare the lists
        print( "Comparing ", left, "and", right )
        if check_list( left, right ) == 1:
            print( "Correct" )
            correct_order += 1
        else:
            print( "Incorrect" )

        # If the next line is a new line, keep going
        n = f.readline()
        if n != "\n":
            reading = False


print( correct_order )