# AOC22-D16P1.py
# Advent of code 2022, day 16 part 1

FILENAME = "testd16"
#FILENAME = "inputd16"


open_valves = []    # The valves that have been opened
minutes = 30        # Minutes remaining
released = 0        # Amount of pressure released


class Valve:
    valves = []     # List of all created valves

    def __init__(self, name, flow, conn) -> None:
        self.name = name                    # Valve name
        self.flow_rate = flow               # Valve flow rate
        self.connected_valves_str = conn    # Connected valves as strings
        self.connected_valves = []          # Connected valves as valve objects
        self.cached_path_to = {}            # Cache of distance to other valves
        Valve.valves.append( self )         # Append self to list of valves
    
    # Some dunders I need for debugging purposes
    def __str__(self) -> str:
        ret_str = f"Valve {self.name}, flow rate {self.flow_rate}, connected valves:"
        for v in self.connected_valves:
            ret_str += f"\n{v.name}"
        return ret_str
    def __repr__(self) -> str:
        return self.name
    
    # Convert the valves named in connected_valves_str to valve objects in connected_valves
    def convert_connected(self):
        for sv in self.connected_valves_str:
            for tv in Valve.valves:
                if tv.name == sv:
                    self.connected_valves.append( tv )
    
    def path_to(self, val):
        # First, check if it's in the cache. If so, return that.
        # (The cache prevents infinite recursion that would occur in situations where
        # a valve in the calling valve's connected_valves list is not connected to the
        # passed-in valve except through the calling valve.)
        if val in self.cached_path_to:
            return self.cached_path_to[val]
        #elif self in val.cached_path_to:
        #    return val.cached_path_to[self]
        # Next, if the passed-in valve is the calling valve, save to the cache and
        # return 0
        elif val is self:
            self.cached_path_to[ val ] = 0
            return 0
        # Next, if the passed-in valve is in the calling valve's list of connected
        # valves, save to the cache and return 1
        elif val in self.connected_valves:
            self.cached_path_to[val] = 1
            val.cached_path_to[self] = 1
            return 1
        # Finally, do some convoluted thing.
        else:
            path = len(Valve.valves)            # Set path to len(list of valves)
            for v in self.connected_valves:     # If one of the valves in the calling valve's
                if val in v.cached_path_to:     # connected list has a cached path,
                    path = v.cached_path_to[val]# return that
                #elif v in val.cached_path_to:
                #    path = val.cached_path_to[v]
            if path == len(Valve.valves):       # If not, call this function recursively
                for v in self.connected_valves: # on the calling valve's list of connected
                    if v.path_to( val ) < path: # valves and return the shortest path + 1
                        path = v.path_to( val )
            self.cached_path_to[val] = path + 1
            val.cached_path_to[self] = path + 1
            return path + 1


# Function for passing a minute
def time_passes( min = 1 ):
    global minutes
    global open_valves
    global released

    minutes -= min
    for _ in range( min ):
        r_am = 0
        for v in open_valves:
            r_am += v.flow_rate
    
    released += r_am
    print( f"{minutes} minutes remaining, {released} pressure has been released.")


# Read the valves from the file
with open( FILENAME ) as f:
    for line in f:
        l = line.split()
        vname = l[1]            # Valve name

        vflow = ''              # Valve flow rate
        for c in l[4]:
            if c.isdecimal():
                vflow += c
        vflow = int(vflow)

        vconn = []
        for x in range( 9, len(l) ):
            vconn.append( l[x].strip(',') )

        Valve( vname, vflow, vconn )
# Then convert the connected valves from strings to objects
for v in Valve.valves:
    v.convert_connected()


current_valve = Valve.valves[0]
while current_valve != None and minutes >= 0:
    # A dictionary to hold the priority of each valve
    temp_path_dict = {}

    # Find the priority for each valve
    for v in Valve.valves:
        if v not in open_valves:
            temp_path_dict[v] = ( len(Valve.valves) - v.path_to( current_valve )) * v.flow_rate
    
    # Pass the appropriate amount of time and move to the next valve
    next_valve = max(temp_path_dict, key=temp_path_dict.get)
    print( temp_path_dict )
    if next_valve.flow_rate == 0:
        current_valve = None
    else:
        print( f"Moving {next_valve.path_to( current_valve )} spaces to {next_valve.name}." )
        for _ in range( next_valve.path_to( current_valve ) ):
            time_passes(  )
        current_valve = next_valve
        
        # Pass a minute and then open the valve
        time_passes()
        open_valves.append( current_valve )

if minutes > 0:
    time_passes(minutes)

print( released )