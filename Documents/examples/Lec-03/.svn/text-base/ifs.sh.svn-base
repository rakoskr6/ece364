#! /bin/bash

data1="1 2 3 4"
data2="1:2:3:4"
echo "data1 = $data1"
echo "data2 = $data2"
echo

echo "data1: IFS = \"$IFS\""
for i in $data1
do
    echo "$i"
done
echo 

echo "data2: IFS = \"$IFS\""
for i in $data2
do
    echo "$i"
done
echo 

#change the ifs to :
IFS=':'

echo "data1: IFS = \"$IFS\""
for i in $data1
do
    echo "$i"
done
echo 

echo "data2: IFS = \"$IFS\""
for i in $data2
do
    echo "$i"
done
echo 

exit 0
