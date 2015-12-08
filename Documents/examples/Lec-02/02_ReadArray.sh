#! /bin/bash

#
# $Id$
#

line=0
while read -a data
do
    ((line++))
    echo Read ${#data[*]} items on line $line
    echo The 3rd item is ${data[2]}
done < Some_Data_File

exit 0