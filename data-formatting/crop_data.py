## how to run: chimera --nogui crop.py
import os
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages

# gather the names of .pdb files in the folder
file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]

# loop through the files, opening, processing, and closing each in turn
for fn in file_names:
	replyobj.status("Processing " + fn) # show what file we're working on
	rc("open " + fn)
        rc("select :106 z<35")
        rc("select invert")
        rc("delete sel")
        rc("write format pdb 0 35_" + fn)
        rc("close all")

	rc("open " + fn)
        rc("select :106 z<30")
        rc("select invert")
        rc("delete sel")
        rc("write format pdb 0 30_" + fn)
        rc("close all")

	rc("open " + fn)
        rc("select :106 z<25")
        rc("select invert")
        rc("delete sel")
        rc("write format pdb 0 25_" + fn)
        rc("close all")

	rc("open " + fn)
        rc("select :106 z<20")
        rc("select invert")
        rc("delete sel")
        rc("write format pdb 0 20_" + fn)
        rc("close all")

	rc("open " + fn)
        rc("select :106 z<15")
        rc("select invert")
        rc("delete sel")
        rc("write format pdb 0 15_" + fn)
        rc("close all")

	rc("open " + fn)
        rc("select :106 z<10")
        rc("select invert")
        rc("delete sel")
        rc("write format pdb 0 10_" + fn)
        rc("close all")

	rc("open " + fn)
        rc("select :106 z<5")
        rc("select invert")
        rc("delete sel")
        rc("write format pdb 0 5_" + fn)
        rc("close all")

