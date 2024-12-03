# AOC22-C9.py
# Advent of code 2022, challenge 9

with open( "inputd5" ) as f:
    
    temp_array = []
    stack_array = []

    # Ugh, a lot of things are hard coded here. This is not very scalable.
    for x in range(8):          
        t = f.readline()
        temp_array.append( [ t[1], t[5], t[9], t[13], t[17], t[21], t[25], t[29], t[33] ] )

    for x in range(9):
        ts = []

        for a in reversed(temp_array):
            ts.append( a[x] )
        
        stack_array.append( ts )
    
    for x in range(len(stack_array)):
        while ' ' in stack_array[x]:
            stack_array[x].remove(' ')

    # Okay I have the stacks read in now.
    f.readline()
    f.readline()

    instructions = f.readlines()
    for i in instructions:
        t = i.split()
        mov = int( t[1] )
        frm = int( t[3] ) - 1
        to = int( t[5] ) - 1
        for x in range(mov):
            letr = stack_array[frm].pop(-1)
            stack_array[to].append( letr )

for s in stack_array:
    print( s[-1] )