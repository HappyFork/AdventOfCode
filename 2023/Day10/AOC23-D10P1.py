# AOC23-D10P1.py
# Advent of code 2023, day 10 part 1


#FILENAME = "testd10.txt"
FILENAME = "inputd10"


total = 0
loop = {}


# Open the file
with open( FILENAME ) as f:
    # The whole file is the map
    map = [l.strip() for l in f.readlines()]

    # Find the starting position
    start = []
    queue = []      # I need this below
    for x in range(0,len(map)):
        for y in range(0,len(map[x])):
            if map[x][y] == "S":
                start = [x,y]
                loop[(x,y)] = 0    

    # Find the pipes connected to the starting position outside of the loop
    if start[0] > 0: # North of S
        c = map[start[0]-1][start[1]]
        if c == "|" or c == "7" or c == "F":
            queue.append((start[0]-1, start[1]))
    if start[0] < len(map)-1: # South of S
        c = map[start[0]+1][start[1]]
        if c == "|" or c == "L" or c == "J":
            queue.append((start[0]+1, start[1]))
    if start[1] > 0: # West of S
        c = map[start[0]][start[1]-1]
        if c == "-" or c == "L" or c == "F":
            queue.append((start[0], start[1]-1))
    if start[1] < len(map[0])-1: # East of S
        c = map[start[0]][start[1]+1]
        if c == "-" or c == "J" or c == "7":
            queue.append((start[0], start[1]+1))
    
    # Fill out the rest of the loop
    loop_broken = True
    step = 1
    while loop_broken:
        nq = []     # Next queue
        
        # Add the queue tuples to the loop dictionary
        for c in queue:
            loop[c] = step
        
        # Find the next pipe part based on the direction
        for c in queue:
            n = (c[0]-1,c[1])
            s = (c[0]+1,c[1])
            e = (c[0],c[1]+1)
            w = (c[0],c[1]-1)
            match map[c[0]][c[1]]:
                case "|":   # Check north and south
                    if n not in loop.keys():
                        nq.append(n)
                    elif s not in loop.keys():
                        nq.append(s)
                case "-":   # Check east and west
                    if e not in loop.keys():
                        nq.append(e)
                    elif w not in loop.keys():
                        nq.append(w)
                case "L":   # Check north and east
                    if n not in loop.keys():
                        nq.append(n)
                    elif e not in loop.keys():
                        nq.append(e)
                case "J":   # Check north and west
                    if n not in loop.keys():
                        nq.append(n)
                    elif w not in loop.keys():
                        nq.append(w)
                case "7":   # Check south and west
                    if s not in loop.keys():
                        nq.append(s)
                    elif w not in loop.keys():
                        nq.append(w)
                case "F":   # Check south and east
                    if s not in loop.keys():
                        nq.append(s)
                    elif e not in loop.keys():
                        nq.append(e)
        
        # End of loop stuff
        step += 1
        queue = nq.copy()

        # Check to see if the loop has connected
        if len(nq) == 2 and nq[0] == nq[1]:
            loop[nq[0]] = step
            loop_broken = False
        


print( step )