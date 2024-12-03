# AOC22-D10P1.py
# Advent of code 2022, day 10 part 1
# I'm adult enough to admit to myself when a naming convention isn't working

#FILENAME = "testd10"
FILENAME = "inputd10"

cycle_number = 1
register_value = 1
cycle_history = {}
signal_strength_sum = 0

with open( FILENAME ) as f:
    lines = f.readlines()
    for l in lines:
        instructs = l.strip().split()

        match instructs[0]:
            case "addx":
                cycle_history[cycle_number] = register_value
                cycle_number += 1
                cycle_history[cycle_number] = register_value
                register_value += int( instructs[1] )
                cycle_number += 1
            case "noop":
                cycle_history[cycle_number] = register_value
                cycle_number += 1


for x in range( 20, len(cycle_history), 40 ):
    signal_strength_sum += x * cycle_history[x]

print( signal_strength_sum )