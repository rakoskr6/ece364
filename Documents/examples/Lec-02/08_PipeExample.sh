#! /bin/bash

#
# $Id$
#


# We can use a combination of date and cut to extract various strings


# date prints a date string to stdout
date

# If we were interested in getting the current hour
# we need to isolate the time string

# Knowing that cut can extract columns of delimited data
# we can pass the output of date to cut
date | cut -d' '  -f5

# The result of this short pipe sequence is the time string
# Again the time string is delimited so we can extract with cut
for i in 1 2 3
do
    date | cut -d' ' -f5 | cut -d':' -f$i
done

# If we needed to save the current hour into a variable we can wrap
# the pipe sequence in $(...)
hour=$(date | cut -d' ' -f5 | cut -d':' -f1)
printf "The current hour is %d\n" $hour

exit 0
