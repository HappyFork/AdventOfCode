# AOC22-D13P1.py
# Advent of code 2022, day 13 part 1

#FILENAME = "testd13"
FILENAME = "inputd13"


index = 1
solution = 0


def check_list( l, r ):
    # First, we'll see if one list is longer than the other. Save a return value but don't return yet
    # because the contents of the list might mean we need to return differently.
    if len(l) < len(r):
        ret_val = 1
    elif len(l) > len(r):
        ret_val = -1
    else:
        ret_val = 0

    # Next, check the list according to the rules.
    for j, k in zip( l, r ):
        if isinstance( j, list ) and isinstance( k, list ):
            # If they're both lists, recurse this function with those lists
            res = check_list( j, k )
            # But if they're the same, don't return just yet.
            if res != 0:
                return res
        elif isinstance( j, list ):
            # If only one of them is a list, recurse this function with the list
            # and the number value as a list with a single element.
            k_list = [k]
            res = check_list( j, k_list )
            # Again, don't return if 0
            if res != 0:
                return res
        elif isinstance( k, list ):
            # Same as above
            j_list = [j]
            res = check_list( j_list, k )
            if res != 0:
                return res
        else:
            # Else, this means they're both numbers. See which one's bigger and
            # Return accordingly.
            if j < k:
                return 1
            elif j > k:
                return -1
    
    # If there's no answer after all of that, return the value we saved at the beginning.
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
            solution += index
        else:
            print( "Incorrect" )

        # If the next line is a new line, keep going
        index += 1
        n = f.readline()
        if n != "\n":
            reading = False


print( solution )