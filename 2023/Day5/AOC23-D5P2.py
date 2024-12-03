# AOC23-D5P2.py
# Advent of code 2023, day 5 part 2

#FILENAME = "testd5.txt"
FILENAME = "inputd5"


seeds = []
soil_map = []
soils = []
fert_map = []
ferts = []
water_map = []
waters = []
light_map = []
ligts = []
temp_map = []
temps = []
humid_map = []
humids = []
locat_map = []
locats = []


# Parse the maps to the above lists
def get_map( line ):
    found = False
    while not found:
        l = f.readline()
        if l == "\n" or l == "":
            found = True
        else:
            t1 = l.strip().split(" ")
            t2 = []
            for x in t1:
                t2.append( int(x) )
            match line:
                case "seed-to-soil map:\n":
                    soil_map.append( tuple(t2) )
                case "soil-to-fertilizer map:\n":
                    fert_map.append( tuple(t2) )
                case "fertilizer-to-water map:\n":
                    water_map.append( tuple(t2) )
                case "water-to-light map:\n":
                    light_map.append( tuple(t2) )
                case "light-to-temperature map:\n":
                    temp_map.append( tuple(t2) )
                case "temperature-to-humidity map:\n":
                    humid_map.append( tuple(t2) )
                case "humidity-to-location map:\n":
                    locat_map.append( tuple(t2) )


# Convert the origin array to the next array
def match_maps( origin, map, output ):
    for y in map:
        diff = y[1]-y[0]
        high_map_range = y[1]+y[2]-1
        orig_copy = origin.copy()
        for r in orig_copy:
            if r[0] in range( y[1], high_map_range+1 ) and r[1] in range( y[1], high_map_range+1 ):
                # If both values in the origin range are in the map range, the whole thing is there
                output.append( [r[0]-diff, r[1]-diff] )
                origin.remove( r )
            elif r[1]<y[1] or r[0]>high_map_range:
                # If the high end of the range is less than the low end of the map range, or
                # vice versa, the whole thing is not in the range
                pass    # Nothin' to do
            else:
                # This is the complicated one. Part of the range overlaps
                if r[0]<y[1] and r[1]>y[1] and r[1]<high_map_range:
                    # The end of the origin range is in the map range
                    output.append( [y[0], r[1]-diff] )
                    origin.append( [r[0], y[1]-1] )
                    origin.remove( r )
                elif r[1]>high_map_range and r[0]<high_map_range and r[0]>y[1]:
                    # The beginning of the origin range is in the map range
                    output.append( [r[0]-diff, high_map_range-diff] )
                    origin.append( [ high_map_range+1, r[1] ] )
                    origin.remove( r )
                elif r[0]<y[1] and r[1]>high_map_range:
                    # The middle of the origin range is in the map range
                    output.append( [y[0], high_map_range-diff] )
                    origin.append( [ r[0], y[1]-1 ] )
                    origin.append( [ high_map_range+1, r[1] ] )
    for x in origin:
        # If there's anything left over in origin, just move it to output
        output.append( x )


# Open the file
with open( FILENAME ) as f:
    # Get the starting seeds
    line = f.readline().split(":")
    st = line[1].strip().split(" ")
    for x in range( 0, len(st), 2 ):
        seeds.append( [int(st[x]), int(st[x])+int(st[x+1])-1] )
    
    # Skip a line
    f.readline()

    get_map( f.readline() ) # Seed-to-soil
    get_map( f.readline() ) # Soil-to-fertilizer
    get_map( f.readline() ) # Fertilizer-to-water
    get_map( f.readline() ) # Water-to-light
    get_map( f.readline() ) # Light-to-temperature
    get_map( f.readline() ) # Temperature-to-humidity
    get_map( f.readline() ) # Humidity-to-location


match_maps( seeds, soil_map, soils )    # Seed-to-soil
match_maps( soils, fert_map, ferts )    # Soil-to-fertilizer
match_maps( ferts, water_map, waters )  # Fertilizer-to-water
match_maps( waters, light_map, ligts )  # Water-to-light
match_maps( ligts, temp_map, temps )    # Light-to-temperature
match_maps( temps, humid_map, humids )  # Temperature-to-humidity
match_maps( humids, locat_map, locats ) # Humidity-to-location

smallest = 9999999999
for i in locats:
    if i[0] < smallest:
        smallest = i[0]
print( smallest )