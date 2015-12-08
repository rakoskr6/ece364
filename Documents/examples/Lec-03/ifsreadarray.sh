#! /bin/bash

IFS=','
while read -a data
do
    echo ${data[2]}
done < tadata

exit 0