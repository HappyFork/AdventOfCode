# AOC23-D6P1.py
# Advent of code 2023, day 6 part 1


#FILENAME = "testd6.txt"
FILENAME = "inputd6"


total = 1   # Puzzle solution


# Open the file
with open( FILENAME ) as f:
    t = f.readline()
    d = f.readline()

times = t.split(":")[1].strip().split(" ")
distances = d.split(":")[1].strip().split(" ")

for t in range(0,len(times)):
    if "" in times:
        times.remove( "" )

for d in range(0,len(distances)):
    if "" in distances:
        distances.remove( "" )

for i in range( 0, len(times) ):
    win_strats = 0
    for x in range( 0, int(times[i]) ):
        if (x*(int(times[i])-x)) > int(distances[i]):
            win_strats += 1
    total *= win_strats

print( total )