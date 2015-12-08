#! /bin/bash

# get date in m/d/y 23:59 format
now=$(date "+%m/%d/%y %H:%M")
echo "Date: " $now

IFS='/: ' # split on separators
now_array=($now)

echo "Year = ${now_array[2]}"
echo "Month = ${now_array[0]}"
echo "Day = ${now_array[1]}"
echo "Hour = ${now_array[3]}"
echo "Minute = ${now_array[4]}"

# Can also use set command to overwrite command line arguments:
set $now
echo "Date parts = $@"
echo "Month = $1"
echo "Minute = $5"

exit 0