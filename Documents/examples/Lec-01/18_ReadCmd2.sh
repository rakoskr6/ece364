#! /bin/bash

#
# $Id$
#

# Read will split on while space
while read col1 col2 therest
do
    echo "Col 2: $col2"    
    echo "The rest: $therest"
    echo

done < tabdata

exit 0
