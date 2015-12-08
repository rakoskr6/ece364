#! /bin/bash

for i in $*
do
    # What would happen if we did not 
    # include ^ and $ boundaries
    if [[ ! $i =~ ^[0-9]+$ ]]
    then
	echo "- $i is not a number!"
    else
	echo "+ $i is a valid number!"
    fi
done

exit 0