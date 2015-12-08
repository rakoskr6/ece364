#! /bin/bash

#
# $Id$
#

((x=$RANDOM % 6))
echo $(whoami) "rolled a $x."

if (( $x != 4 ))
then
    exit 0
else
    exit 1
fi