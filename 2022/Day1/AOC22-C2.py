# AOC22-C2.py
# Advent of code 2022, challenge 2

max1 = 0 # Will hold the largest sum in the set
max2 = 0 # 2nd largest
max3 = 0 # 3rd largest

def checkmaxs( currsum ):
    # This function will check if the passed-in value is greater than
    # any of the highest 3 values. If it is, it will replace that
    # value and move the lower values down to the appropriate var
    global max1
    global max2
    global max3

    if currsum > max1:
        max3 = max2
        max2 = max1
        max1 = currsum
    elif currsum > max2:
        max3 = max2
        max2 = currsum
    elif currsum > max3:
        max3 = currsum


with open( "inputd1" ) as f:        # Open the file as f

    lines = f.readlines()           # Read the lines into lines
    csum = 0                        # This will be the sum of the current block of lines

    for l in lines:                 # For each line in lines
        if l.strip() == "":         # If it's a new line, that's the end of the block
            checkmaxs( csum )
            csum = 0                # Then, reset csum
        else:                       # If it's a number,
            csum += int( l.strip() )# Add it to current sum

# I believe when the file ends it won't do a last max check so
checkmaxs( csum )

print( max1 + max2 + max3 )