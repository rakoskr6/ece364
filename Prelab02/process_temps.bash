#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-07 13:58:59 -0400 (Mon, 07 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab02/process_temps.bash $  
#      $Revision: 81492 $   
#                 
#########################

if (($# == 1))
then
 
    if [[ -e $1 ]]
    then
	exec 4< $1
	read -a line <&4
	while read -a line <&4
	do

	  ((Total=0))
	  for ((i=1; i<${#line[*]};i++))
	  do
	      ((Total=$Total+${line[i]}))
	  done
	  ((Average=$Total/(${#line[*]}-1)))
	  echo "Average temperature for time ${line[0]} was $Average C."
	done
    else
	echo "Error: $1 is not a readable file"
	exit 2
    fi
    

else
    echo "Usage: process_temps.bash <input file>"
    exit 1
fi
exit 0