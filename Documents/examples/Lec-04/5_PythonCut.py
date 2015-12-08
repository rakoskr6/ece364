#! /usr/bin/env python

# This example reads input from stdin, extracts a column and prints it to stdout
# Try redirecting the csv_data file into this script

import sys

if len(sys.argv) != 3:
    sys.stderr.write("usage: 5_PythonCut.py <delim> <field>\n")
    sys.stderr.write("\t<delim> - field delimiter string\n")
    sys.stderr.write("\t<field> - field number\n")
    sys.exit(1)

delim=sys.argv[1]

# Convert to integer
field=int(sys.argv[2])

if field <= 0:
    sys.stderr.write("error: invalid field\n")
    sys.exit(1)

n = 0
for line in sys.stdin:
    n += 0
    line = line.rstrip()
    
    cols = line.split(delim)
    
    if len(cols) >= field:
        sys.stdout.write(cols[field-1] + "\n")
    else:
        sys.stdout.write("")
    
    
sys.exit(0)
