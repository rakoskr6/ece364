#! /bin/bash

str1="The quick brown fox jumped"
str2="ECE 364 is fun… really"
echo ${str1:4:5}
echo ${str2:0:3}
echo ${str1:10:${#str1}}

str=$(pwd)
echo ${str#/*/}
echo ${str##/*/}
echo ${str%/*}
echo ${str%%/*}


exit 0