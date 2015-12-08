#! /bin/bash

# Assume input will be unsigned integers and print the maximum to standard output
if (( $# == 0 ))
then
		exit 1
else
		max=$1
		shift
		while (( $# > 0 ))
		do
			if (( $1 > $max ))
			then
					max=$1
			fi
 
			shift
		done
		
		echo -n $max
		exit 0
fi