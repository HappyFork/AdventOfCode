# AOC22-D14P2.py
# Advent of code 2022, day 14 part 2

#FILENAME = "testd14"
FILENAME = "inputd14"


coordinates = {}
floor = 0             # Cave floor


# This is the ugliest file parsing I have ever done I'm so sorry
with open( FILENAME ) as f:
    lines = f.readlines()   # One line will be one line of rocks
    for lin in lines:
        input = []
        for l in lin.strip().split('->'):   # Split the coordinates up
            input.append( l.strip() )       # And put them in input
        for a in range(len(input)-1):       # For each set of two input coordinates,
            from_cords_str = input[a].split(',')    # Get each x and y
            to_cords_str = input[a+1].split(',')
            from_cords = []
            to_cords = []
            for f in from_cords_str:                # And turn them into ints
                from_cords.append( int(f) )
            for t in to_cords_str:
                to_cords.append( int(t) )
            
            # Find lowest y
            if from_cords[1] > floor:
                floor = from_cords[1]
            if to_cords[1] > floor:
                floor = to_cords[1]

            # Draw lines
            if from_cords[0] == to_cords[0]:        # If they have the same x axis,
                if from_cords[1] < to_cords[1]:     # draw a line along the y axis
                    for b in range( from_cords[1], to_cords[1] + 1 ):
                        cord_string = str(from_cords[0]) + "," + str(b)
                        coordinates[cord_string] = "Rock"
                else:                               # But I have to do this weird thing so the ranges work right if they're backwards
                    for b in range( to_cords[1], from_cords[1] + 1 ):
                        cord_string = str(from_cords[0]) + "," + str(b)
                        coordinates[cord_string] = "Rock"
            elif from_cords[1] == to_cords[1]:      # Then the same for the y axis.
                if from_cords[0] < to_cords[0]:
                    for b in range( from_cords[0], to_cords[0] + 1 ):
                        cord_string = str(b) + "," + str(from_cords[1])
                        coordinates[cord_string] = "Rock"
                else:
                    for b in range( to_cords[0], from_cords[0] + 1 ):
                        cord_string = str(b) + "," + str(from_cords[1])
                        coordinates[cord_string] = "Rock"


# Put in a floor
floor += 2
for c in range(200,800):
    cord_string = str(c) + "," + str(floor)
    coordinates[cord_string] = "Floor"


# Now, simulate the sand falling
sand_cord = [500,0]
pouring = True
while pouring:
    current_cord_string = str(sand_cord[0]) + "," + str(sand_cord[1])
    below_cord_string = str(sand_cord[0]) + "," + str(sand_cord[1] + 1)
    left_cord_string = str(sand_cord[0] - 1) + "," + str(sand_cord[1] + 1)
    right_cord_string = str(sand_cord[0] + 1) + "," + str(sand_cord[1] + 1)
    if below_cord_string not in coordinates.keys():
        sand_cord[1] += 1
    elif left_cord_string not in coordinates.keys():
        sand_cord[0] -= 1
        sand_cord[1] += 1
    elif right_cord_string not in coordinates.keys():
        sand_cord[0] += 1
        sand_cord[1] += 1
    else:
        coordinates[current_cord_string] = "Sand"
        sand_cord = [500,0]
    
    if "500,0" in coordinates.keys():
        pouring = False


sands = 0
for key in coordinates:
    if coordinates[key] == "Sand":
        sands += 1
print( sands )