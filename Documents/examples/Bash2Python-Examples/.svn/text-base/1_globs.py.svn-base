#! /usr/bin/env python

import sys, os, glob

if len(sys.argv) == 1:
    globstr = "*"
elif len(sys.argv) == 2:
    # Note: You will need to quote the glob because bash will expand them in the argument list!
    # Example: ./1_globs.py "*.cpp"
    globstr = sys.argv[1]
else:
    sys.stderr.write("usage: 1_globs.py [glob string]\n")
    sys.exit(1)

sys.stdout.write("Items matching the glob \"%s\":\n" % (globstr,))

for f in glob.glob(globstr):
    # What is the file?
    if os.path.isfile(f):
        sys.stdout.write("File: ")
    elif os.path.isdir(f):
        sys.stdout.write("Dir: ")
    else:
        sys.stdout.write("Other: ")

    sys.stdout.write("%s\n" % (f,))

sys.exit(0)
    
