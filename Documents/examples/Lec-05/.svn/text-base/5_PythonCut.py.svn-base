#! /usr/bin/env python

# This example reads input from stdin, extracts a column and prints it to stdout
# Try redirecting the csv_data file into this script

# Same as the lecture 4 example except it will read from a file is one is passed in

import sys, os

if len(sys.argv) < 3 or len(sys.argv) > 4:
    sys.stderr.write("usage: 5_PythonCut.py <delim> <field> [file]\n")
    sys.stderr.write("\t<delim> - field delimiter string\n")
    sys.stderr.write("\t<field> - field number\n")
    sys.stderr.write("\t[file] - optional input file to read from instead of stdin\n")
    sys.exit(1)

delim=sys.argv[1]

# Convert to integer
field=int(sys.argv[2])

if field <= 0:
    sys.stderr.write("error: invalid field\n")
    sys.exit(1)

# Get the input file is one is passes
if len(sys.argv) == 4:

    # Make sure we can read
    if not os.access(sys.argv[3], os.R_OK) or not os.path.isfile(sys.argv[3]):
        sys.stderr.write("error: can not read %s\n" % (sys.argv[3],))
        sys.exit(1)

    fp = open(sys.argv[3], "r")
else:
    # Otherwise point fp to stdin
    fp = sys.stdin

n = 0
for line in fp:
    n += 0
    line = line.rstrip()
    
    cols = line.split(delim)
    
    if len(cols) >= field:
        sys.stdout.write(cols[field-1] + "\n")
    else:
        sys.stdout.write("")
    

fp.close()

sys.exit(0)
