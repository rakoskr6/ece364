#! /bin/bash

# Try the num1, nums2, and nums3 input

if (( $# != 3 ))
then
    echo "usage: $0 <file1> <file2> <file3>"
    exit 1
fi

# Make sure each file is readable
for file in $*
do
    if [[ ! -f $file || ! -r $file ]]
    then
	echo "error: $file is not readable"
	exit 2
    fi
done

# Open all three files for reading
exec 3<$1
exec 4<$2
exec 5<$3

while (( 1 == 1 ))
do

    # Read a line from the other files
    read D1 <&3
    read D2 <&4
    read D3 <&5
    
    # If we get to the end of a file Dn will be an empty string
    # just break out of the loop
    if [[ -z $D1 || -z $D2 || -z $D3 ]]
    then
	break
    fi

    if (( $D1 > $D2 && $D1 > $D3 ))
    then
	largest=$D1
    elif (( $D2 > $D1 && $D2 > $D3 ))
    then
	largest=$D2
    else
	largest=$D3
    fi

    echo "Largest of $D1 $D2 $D3 is: $largest"

done

exit 0