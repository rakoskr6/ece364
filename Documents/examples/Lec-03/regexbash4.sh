#! /bin/bash

line=0
re="^[-+]*[0-9]+$"
while read item
do
    ((line=$line+1))
    echo -n "Line ${line}: $item is"
    if [[ $item =~ $re ]]
    then
	echo " OK"
    else
	echo " BAD"
    fi
done

exit 0