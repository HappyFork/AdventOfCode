# AOC22-C11.py
# Advent of code 2022, challenge 11

chars_read = 0      # Will keep track of how many characters are read


def check_repeats( str ):
# Function to check if the passed-in string has any repeat characters
# will return true if so, and false if not
    for c in str:                   # For each character in the string
        if str.count(c) > 1:        # If the string has more than 1
            return True             # Return true
    return False                    # If no repeats found, return false


with open( "inputd6" ) as f:        # Open the input file as f
    buffer = f.read( 4 )            # Get the first 4 characters
    chars_read += 4                 # Count those characters
    sopm_not_found = check_repeats( buffer )    # Check if there are any repeats

    while( sopm_not_found ):        # As long as the start of packet isn't found,
        buffer = buffer[1:] + f.read(1)     # Read one character at a time
        # The buffer will only hold the last 4 characters read
        chars_read += 1                     # Count that character
        sopm_not_found = check_repeats( buffer )    # And check for start of packet again


print( chars_read )                 # Print characters read