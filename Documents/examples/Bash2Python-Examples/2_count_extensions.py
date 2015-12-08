#! /usr/bin/env python

import sys, os, glob

files={}

if len(sys.argv) != 1:
    sys.stderr.write("usage: 2_count_extensions.py\n")
    sys.exit(1)

for f in glob.glob("*"):
    # Only consider actual files
    if os.path.isfile(f):

        # Split the file name into a name and extension
        name, ext = os.path.splitext(f)
    
        # Init an empty list for a particular extension
        if ext not in files:
            files[ext] = []
    
        # Append the original file name to the list
        files[ext].append(f)

# Loop over each extension
for ext in files:
    print "There were %d files with a \"%s\" extension" % (len(files[ext]), ext)

    # Print out the files
    for f in files[ext]:
        print f

    print 

sys.exit(0)

