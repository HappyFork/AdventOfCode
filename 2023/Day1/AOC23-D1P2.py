# AOC23-D1P2.py
# Advent of code 2023, day 1 part 2

#FILENAME = "testd2"
FILENAME = "inputd1"


total = 0

# Open the file
with open( FILENAME ) as f:
    # Get each line
    lines = f.readlines()
    for l in lines:
        nchars = ""     # Characters making up the target number
        

        # Find the first digit
        incr = 0
        first_found = False
        while not first_found:
            # If it's a digit
            if l[incr] in "123456789":
                nchars = nchars + l[incr]
                first_found = True
            # If it's spelled out
            else:
                match l[incr]:
                    case "o":
                        # One
                        if l[incr+1] == "n" and l[incr+2] == "e":
                            nchars = nchars + "1"
                            first_found = True
                    case "t":
                        # Two
                        if l[incr+1] == "w" and l[incr+2] == "o":
                            nchars = nchars + "2"
                            first_found = True
                        # Three
                        elif l[incr+1] == "h" and l[incr+2] == "r" and l[incr+3] == "e" and l[incr+4] == "e":
                            nchars = nchars + "3"
                            first_found = True
                    case "f":
                        # Four
                        if l[incr+1] == "o" and l[incr+2] == "u" and l[incr+3] == "r":
                            nchars = nchars + "4"
                            first_found = True
                        # Five
                        elif l[incr+1] == "i" and l[incr+2] == "v" and l[incr+3] == "e":
                            nchars = nchars + "5"
                            first_found = True
                    case "s":
                        # Six
                        if l[incr+1] == "i" and l[incr+2] == "x":
                            nchars = nchars + "6"
                            first_found = True
                        # Seven
                        elif l[incr+1] == "e" and l[incr+2] == "v" and l[incr+3] == "e" and l[incr+4] == "n":
                            nchars = nchars + "7"
                            first_found = True
                    case "e":
                        # Eight
                        if l[incr+1] == "i" and l[incr+2] == "g" and l[incr+3] == "h" and l[incr+4] == "t":
                            nchars = nchars + "8"
                            first_found = True
                    case "n":
                        # Nine
                        if l[incr+1] == "i" and l[incr+2] == "n" and l[incr+3] == "e":
                            nchars = nchars + "9"
                            first_found = True
                
                # If no number found
                incr += 1


        # Find the last digit
        incr = -1
        last_found = False
        while not last_found:
            # If it's a digit
            if l[incr] in "123456789":
                nchars = nchars + l[incr]
                last_found = True
            # If it's spelled out
            else:
                match l[incr]:
                    case "e":
                        # One
                        if l[incr-1] == "n" and l[incr-2] == "o":
                            nchars = nchars + "1"
                            last_found = True
                        # Three
                        elif l[incr-1] == "e" and l[incr-2] == "r" and l[incr-3] == "h" and l[incr-4] == "t":
                            nchars = nchars + "3"
                            last_found = True
                        # Five
                        elif l[incr-1] == "v" and l[incr-2] == "i" and l[incr-3] == "f":
                            nchars = nchars + "5"
                            last_found = True
                        # Nine
                        elif l[incr-1] == "n" and l[incr-2] == "i" and l[incr-3] == "n":
                            nchars = nchars + "9"
                            last_found = True
                    case "o":
                        # Two
                        if l[incr-1] == "w" and l[incr-2] == "t":
                            nchars = nchars + "2"
                            last_found = True
                    case "r":
                        # Four
                        if l[incr-1] == "u" and l[incr-2] == "o" and l[incr-3] == "f":
                            nchars = nchars + "4"
                            last_found = True
                    case "x":
                        # Six
                        if l[incr-1] == "i" and l[incr-2] == "s":
                            nchars = nchars + "6"
                            last_found = True
                    case "n":
                        # Seven
                        if l[incr-1] == "e" and l[incr-2] == "v" and l[incr-3] == "e" and l[incr-4] == "s":
                            nchars = nchars + "7"
                            last_found = True
                    case "t":
                        # Eight
                        if l[incr-1] == "h" and l[incr-2] == "g" and l[incr-3] == "i" and l[incr-4] == "e":
                            nchars = nchars + "8"
                            last_found = True
                
                # If no number found
                incr -= 1
        
        # Add target to total
        total += int(nchars)

print( total )