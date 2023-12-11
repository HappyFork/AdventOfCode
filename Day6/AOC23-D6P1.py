# AOC23-D6P1.py
# Advent of code 2023, day 6 part 1


FILENAME = "testd6.txt"
#FILENAME = "inputd6"


total = 0   # Puzzle solution


# Open the file
with open( FILENAME ) as f:
    t = f.readline()
    d = f.readline()

times = t.split(":")[1].strip().split(" ")
distances = d.split(":")[1].strip().split(" ")

for t in times:
    if "" in times:
        times.remove( "" )

for d in distances:
    if "" in distances:
        distances.remove( "" )

print( times )
print( distances )