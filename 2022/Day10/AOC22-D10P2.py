# AOC22-D10P2.py
# Advent of code 2022, day 10 part 2
# I'm adult enough to admit to myself when a naming convention isn't working

#FILENAME = "testd10"
FILENAME = "inputd10"

cycle_number = 1
register_value = 1
cycle_history = {}
#signal_strength_sum = 0

def cycle( cy, reg, add=0 ):
    global cycle_history
    cycle_history[cy] = reg

    mod = cy % 40

    if mod == reg or mod == reg + 1 or mod == reg + 2:
        print( "#", end="" )
    else:
        print( ".", end="" )

    if mod == 0:
        print( "" )
    
    return cy + 1

with open( FILENAME ) as f:
    lines = f.readlines()
    for l in lines:
        instructs = l.strip().split()

        match instructs[0]:
            case "addx":
                cycle_number = cycle(cycle_number, register_value)
                cycle_number = cycle(cycle_number, register_value)
                register_value += int( instructs[1] )
            case "noop":
                cycle_number = cycle(cycle_number, register_value)


for x in range( 1, len(cycle_history) ):
    pass
    #print( x, ": ", cycle_history[x] )
    #signal_strength_sum += x * cycle_history[x]

#print( signal_strength_sum )