# AOC23-D3P1.py
# Advent of code 2023, day 3 part 2

#FILENAME = "testd3.txt"
FILENAME = "inputd3"

total = 0           # Puzzle solution
lines = []          # Store file lines here
gear_coords = []    # Keep track of where the symbols are
found_numbers = []  # Keep track of numbers already found


# Function for looking for numbers at a specific coordinates
def find_number( x, y ):
    starty = 0
    endy = len(lines[x])
    temp_num_str = ""

    # Find the start of the number
    for i in range( y, -1, -1 ):
        if not lines[x][i].isdigit():
            starty = i+1
            break
    
    # Find the end of the number
    for i in range( y, len(lines[x]) ):
        if not lines[x][i].isdigit():
            endy = i-1
            break
    
    # Get the number and save the coords
    for i in range( starty, endy+1 ):
        found_numbers.append( (x,i) )
        temp_num_str += lines[x][i]
    
    return int( temp_num_str )


# Open the file
with open( FILENAME ) as f:
    lines = f.readlines()       # Get the lines

    for i in range( 0, len(lines) ):                # Find the coordinates
        for j in range( 0, len(lines[i]) ):         # of each asterisk
            if lines[i][j] == '*':
                gear_coords.append( (i,j) )
    
    for sc in gear_coords:
        nums = 0
        ratio = 1

        # x-1, y-1
        if lines[sc[0]-1][sc[1]-1].isdigit() and (sc[0]-1,sc[1]-1) not in found_numbers:
            ratio *= find_number( sc[0]-1,sc[1]-1 )
            nums += 1
        
        # x-1, y
        if lines[sc[0]-1][sc[1]].isdigit() and (sc[0]-1,sc[1]) not in found_numbers:
            ratio *= find_number( sc[0]-1,sc[1] )
            nums += 1
        
        # x-1, y+1
        if lines[sc[0]-1][sc[1]+1].isdigit() and (sc[0]-1,sc[1]+1) not in found_numbers:
            ratio *= find_number( sc[0]-1,sc[1]+1 )
            nums += 1
        
        # x, y-1
        if lines[sc[0]][sc[1]-1].isdigit() and (sc[0],sc[1]-1) not in found_numbers:
            ratio *= find_number( sc[0],sc[1]-1 )
            nums +=1
        
        # x, y+1
        if lines[sc[0]][sc[1]+1].isdigit() and (sc[0],sc[1]+1) not in found_numbers:
            ratio *= find_number( sc[0],sc[1]+1 )
            nums += 1
        
        # x+1, y-1
        if lines[sc[0]+1][sc[1]-1].isdigit() and (sc[0]+1,sc[1]-1) not in found_numbers:
            ratio *= find_number( sc[0]+1,sc[1]-1 )
            nums += 1
        
        # x+1, y
        if lines[sc[0]+1][sc[1]].isdigit() and (sc[0]+1,sc[1]) not in found_numbers:
            ratio *= find_number( sc[0]+1,sc[1] )
            nums += 1
        
        # x+1, y+1
        if lines[sc[0]+1][sc[1]+1].isdigit() and (sc[0]+1,sc[1]+1) not in found_numbers:
            ratio *= find_number( sc[0]+1,sc[1]+1 )
            nums += 1
        
        if nums == 2:
            total += ratio
            

        

print( total )