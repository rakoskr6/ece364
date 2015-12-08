#! /bin/bash

#
# $Id$
#

if (( $# != 2 ))
then
    echo "usage: $0 <infile> <outfile>"
    exit 1
fi

# You can use the file one.txt as an input file
# You can use the file name one.out as an output file

exec 3< $1 # Open new file descriptor 3 for reading
exec 4> $2 # Open new file descriptor 4 for writing
I=0
while read Line  # read from file descriptor #3 
do
    echo "Processing line: $Line" # will not be printed to output
    echo Line ${I}: ${Line} >&4 # print to FD #4
    ((I=I+1))
done <&3