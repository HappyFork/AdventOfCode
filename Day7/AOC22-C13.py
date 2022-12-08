# AOC22-C13.py
# Advent of code 2022, challenge 13

# Class definitions
class Directory:
    """A directory that holds files and other directories"""
    def __init__( self, nm, cd = None ):    # On create,
        self.name = nm                      # Set instance name
        self.containing_dir = cd            # Set containing dir
        self.dirs = []                      # Create a blank list of directories
        self.files = []                     # Create a blank list of files

    def size( self ):
        pass    # Add up all the filesizes of all contained files and all contained files of contained directories.

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

    curr_dir = Directory( "/" )
    solution_size = 0
    
    lines = f.readlines()

    for l in lines:
        spl = l.split()

        if spl[0] == "$":
            pass # It's a command
        else:
            pass # It's output