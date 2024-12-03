# AOC22-D13P2.py
# Advent of code 2022, day 13 part 2

#FILENAME = "testd13"
FILENAME = "inputd13"


parsed_lines = []


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
    lines = f.readlines()
    for l in lines:
        temp = l.strip()
        if temp != "":
            parsed_lines.append(eval(temp))

parsed_lines.append([[2]])
parsed_lines.append([[6]])


# Let's do a bubble sort! I'm a fraud and had to look up how to do this lol
for i in range(len(parsed_lines)):
    for j in range( 0, len(parsed_lines)-i-1 ):
        if check_list( parsed_lines[j], parsed_lines[j+1] ) == -1:
            parsed_lines[j], parsed_lines[j+1] = parsed_lines[j+1], parsed_lines[j]
            # Looking up the bubble sort also taught me this cool way to swap values in python!


# This next line would look so much better if the signal was 0 indexed but whatever!
print( (parsed_lines.index([[2]]) + 1) * (parsed_lines.index([[6]]) + 1) )