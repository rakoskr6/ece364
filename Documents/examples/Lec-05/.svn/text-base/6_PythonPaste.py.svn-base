#! /usr/bin/env python

import os, sys

if len(sys.argv) < 4:
    sys.stderr.write("usage: 6_PythonPaste.py <delim> <outfile> <infile1> [infile2, infile3 ...]")
    sys.stderr.write("\t<delim> - String delimiter to join to the values in each input file\n")
    sys.stderr.write("\t<outfile> - Output file to write to\n")
    sys.stderr.write("\t<infile1> - First input file\n")
    sys.stderr.write("\t[infile2, ...] - Additional input files (optional)\n")
    sys.exit(1)

if os.path.exists(sys.argv[2]) and not os.access(sys.argv[2], os.W_OK):
    sys.stderr.write("error: can not write to output file %s\n" % (sys.argv[2]))
    sys.exit(1)

for filename in sys.argv[3:]:
    if not os.access(filename, os.R_OK) or not os.path.isfile(filename):
        sys.stderr.write("error: can not read from input file %s\n" % (filename,))
        sys.exit(1)


# Open the output file for writing
outfile = open(sys.argv[2], "w")

# See lecture 4 examples for list comprehension
# This statement creates a list where each element is the result of calling open() on each input file ma,e
infiles = [ open(filename, "r") for filename in sys.argv[3:] ] 

# The list column_lines will contain len(infiles) lists.
# column_lines[1] would be the list of lines from the second input file
column_lines = []
for f in infiles:
    # Read all lines. 
    # This statement calls strip() on each line x produced by readlines()
    lines = [ x.strip() for x in f.readlines() ]    
    column_lines.append(lines)

# For each line:
for i in range(len(column_lines[0])):
    # This line produces a list by getting each row from column i
    # Note that list comprehension does not reqire the expression to the left of for to be a function call
    line_items = [ column_lines[j][i] for j in range(len(column_lines)) ]
    
    # Join the line using the delimiter and write it
    outfile.write(sys.argv[1].join(line_items) + "\n")
    
# Close the output and input files
outfile.close()
for fp in infiles:
    fp.close()

sys.exit(0)
