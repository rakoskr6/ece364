#! /bin/bash

for i in $*
do
    # Will not work for cases... e.g. ab123cd would match the regex
    if [[ ! $i =~ [0-9]+ ]]
    then
	echo "- $i is not a number!"
    else
	echo "+ $i is a valid number!"
    fi
done

exit 0