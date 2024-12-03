# AOC22-D15P2.py
# Advent of code 2022, day 15 part 2

#FILENAME = "testd15"
FILENAME = "inputd15"


#sensor_range_cords = set()  # Outer bounds of where beacons cannot be
#beacons = set()             # Locations of beacons
sensor_sets = {}            # Sensors and their closest beacons


def check_closest( x, y ):
    for k in sensor_sets.keys():
        if abs( x - k[0] ) + abs( y - k[1] ) <= sensor_sets[k]:
            return False
    return True


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

        # Save the beacon coordinates in the beacon set
        #beacons.add( (bx,by) )

        # Find the manhattan distance of each sensor to it's corresponding
        # beacon and save the distance as a value with the sensor tuple
        # as the key.
        mdist = abs( sx - bx ) + abs( sy - by )
        sensor_sets[(sx,sy)] = mdist


# For each sensor
for sensor in sensor_sets:
    extradist = sensor_sets[sensor] + 1
    for x in range( sensor[0] - extradist, sensor[0] + extradist + 1 ):
        if x >= 0 and x <= 4000000:
            mdiff = extradist - abs( x-sensor[0] )
            if sensor[1] - mdiff >= 0 and check_closest( x, sensor[1] - mdiff ):
                print( x, sensor[1] - mdiff )
            if sensor[1] + mdiff <= 4000000 and check_closest( x, sensor[1] + mdiff ):
                print( x, sensor[1] + mdiff )