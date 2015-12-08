#! /bin/bash

#
# $Id$
#

A=(1 foo 2)
echo "Element 2 =" ${A[1]}
echo "A =" ${A[*]}

A[1]=bar
echo "Element 2=" ${A[1]}

echo "Size of A is:" ${#A[*]}

echo "Indicies of A:" ${!A[*]}

# Looping: 
for item in ${A[*]}
do
    echo $item
done
echo 

for index in ${!A[*]}
do
    echo ${A[$item]}
done
echo

exit 0
