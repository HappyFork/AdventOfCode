# AOC23-D6P2.py
# Advent of code 2023, day 6 part 2


FILENAME = "testd6.txt"
#FILENAME = "inputd6"


# Open the file
with open( FILENAME ) as f:
    t = f.readline()
    d = f.readline()

times = t.split(":")[1].strip()
distances = d.split(":")[1].strip()

tim = ""
dist = ""

for t in times:
    if t.isdigit():
        tim += t

for d in distances:
    if d.isdigit():
        dist += d

print( tim )
print( dist )

win_strats = 0
for x in range( 0, int(tim) ):
    if (x*(int(tim)-x)) > int(dist):
        win_strats += 1

print( win_strats )