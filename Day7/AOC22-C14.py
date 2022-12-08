# AOC22-C14.py
# Advent of code 2022, challenge 14

# Class definitions
class Directory:
    """A directory that holds files and other directories"""
    def __init__( self, nm, cd = None ):    # On create,
        self.name = nm                      # Set instance name
        self.containing_dir = cd            # Set containing dir
        self.dirs = []                      # Create a blank list of directories
        self.files = []                     # Create a blank list of files

    def size( self ):                       # Return size of all contained files
        siz_sum = 0                         # plus size of all contained directories

        for d in self.dirs:                 # Directories
            siz_sum += d.size()
        
        for f in self.files:                # Files
            siz_sum += f.size
        
        return siz_sum

    def add_dir( self, dir ):
        self.dirs.append( dir )             # Add passed-in directory to list

    def add_file( self, fil ):
        self.files.append( fil )            # Add passed-in file to list

class File:
    """A file with a name and size"""
    def __init__( self, nm, sz ):           # On create,
        self.name = nm                      # Set instance name
        self.size = sz                      # Set instance size


# Read file
with open( "inputd7" ) as f:

    root_dir = Directory( "/" )
    curr_dir = root_dir
    created_dirs = [root_dir]
    
    lines = f.readlines()

    for l in lines:
        spl = l.split()

        if spl[0] == "$":
            if spl[1] == "cd":
                if spl[2] == "..":
                    curr_dir = curr_dir.containing_dir
                elif spl[2] == "/":
                    curr_dir = root_dir
                else:
                    for d in curr_dir.dirs:
                        if d.name == spl[2]:
                            curr_dir = d
                            break
            # Here is where I would parse the ls command,
            # but I was given a hint that it's worthless
        elif spl[0] == "dir":
            new_dir = Directory( spl[1], curr_dir )
            created_dirs.append( new_dir )
            curr_dir.add_dir( new_dir )
        else:
            new_file = File( spl[1], int(spl[0]) )
            curr_dir.add_file( new_file )

unused = 70000000 - root_dir.size()
need_to_free = 30000000 - unused
solution_size = 70000000    # I need this to be some arbitrarily big number to start

for d in created_dirs:
    s = d.size()
    if s >= need_to_free and s < solution_size:
        solution_size = s
    
print( solution_size )