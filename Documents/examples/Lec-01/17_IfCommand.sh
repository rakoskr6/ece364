#! /bin/bash

#
# $Id$
#

if gcc good.c
then
    echo "good.c compiles!"
    ./a.out
fi

if gcc bad.c
then
    echo "bad.c somehow compiles..."
else
    echo "bad.c contains a few bugs..."
fi

if (( 5 < 6 && 6 <= 6 ))
then
    echo "Looks like bash is working."
else
    echo "Better get a new bash installaton."
fi

if [[ -d $0 ]]
then
    echo "How is $0 a directory?"
elif [[ ! -x $0 ]]
then
    echo "This script is not marked with execute permissions."
else
    echo "$0 is running"
fi

if [[ -d $HOME && -w $HOME ]]
then
    echo "You can write to your home directory!"
fi

# single line if (saves some typing)
[[ $# == 0 ]] || echo "Error: Too many parameters..."
[[ $# == 0 ]] && echo "OK: You provided enough parameters..."


exit 0
