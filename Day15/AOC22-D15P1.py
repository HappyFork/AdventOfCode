# AOC22-D15P1.py
# Advent of code 2022, day 15 part 1

#FILENAME = "testd15"
FILENAME = "inputd15"


no_beacons = set()      # Locations where beacons cannot be
sensor_sets = {}        # Sensors and their closest beacons
solution = 0


# Open and read file
with open( FILENAME ) as f:
    for line in f:
        digits = 0

        # Find sensor's x coordinate
        sxi = line.find("=") + 1    
        for c in range( sxi, len(line) ):
            if line[c].isdecimal() or line[c] == '-':
                digits += 1
            else:
                break
        # Save it as sx
        sx = int(line[sxi:sxi+digits])
        
        # Find sensor's y coordinate
        lin = line[sxi+digits:]
        digits = 0
        syi = lin.find("=") + 1
        for c in range( syi, len(lin) ):
            if lin[c].isdecimal() or lin[c] == '-':
                digits += 1
            else:
                break
        # Save it as sy
        sy = int(lin[syi:syi+digits])

        # Find sensor's closest beacon's x coordinate
        lin = lin[syi+digits:]
        digits = 0
        bxi = lin.find("=") + 1
        for c in range( bxi, len(lin) ):
            if lin[c].isdecimal() or lin[c] == '-':
                digits += 1
            else:
                break
        # Save it as bx
        bx = int(lin[bxi:bxi+digits])

        # Find sensor's closest beacon's y coordinate
        lin = lin[bxi+digits:]
        digits = 0
        byi = lin.find("=") + 1
        for c in range( byi, len(lin) ):
            if lin[c].isdecimal() or lin[c] =='-':
                digits += 1
            else:
                break
        # Save it as by
        by = int(lin[byi:byi+digits])

        # Save the line's sensor's coordinates in a tuple as a key
        # in the sensor_sets dictionary. The corresponding value is
        # its closest beacon's coordinates, also as a tuple.
        # Can you tell I just learned about tuples?
        print( f"Sensor: ({sx},{sy}), Beacon: ({bx},{by})" )
        sensor_sets[(sx,sy)] = (bx,by)


#print( len(sensor_sets) )


# For each sensor
for sensor in sensor_sets:
    # Find the manhattan distance to its beacon
    beacon = sensor_sets[sensor]
    mdist = abs( sensor[0] - beacon[0] ) + abs( sensor[1] - beacon[1] )
    print( f"{sensor}, Beacon distance: {mdist}" )

    
    #xleast = sensor[0] - mdist
    #xmost = sensor[0] + mdist
    #yleast = sensor[1] - mdist
    #ymost = sensor[1] + mdist

    # Then add each space within that distance to no_beacons
    for x in range( sensor[0] - mdist, sensor[0] + mdist + 1 ):
        mdiff = abs( x - sensor[0] )
        if 2000000 > sensor[1] - mdiff and 2000000 < sensor[1] + mdiff + 1:
            no_beacons.add( (x,2000000) )
        #for y in range( sensor[1] - mdiff, sensor[1] + mdiff + 1 ):
        #    print( (x,y) )
        #    no_beacons.add( (x,y) )     # As a tuple... naturally.

    #for x in range( xleast, xmost + 1 ):
    #    for y in range( yleast-x, ymost + 1 ):
    #        #print( f"({x},{y})" )
    #        if abs( sensor[0] - x ) + abs( sensor[1] - y ) <= mdist:
    #            if (x,y) not in sensor_sets.values():
    #                print( (x,y) )
    #                no_beacons.add( (x,y) )     # As a tuple... naturally.


#for cp in no_beacons:
#    if cp[1] == 2000000:
#        #print(cp)
#        solution += 1

print( len(no_beacons) )