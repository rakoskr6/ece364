#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-08-31 21:09:14 -0400 (Mon, 31 Aug 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab01/sensor_sum.sh $  
#      $Revision: 80898 $   
#                 
#########################

if (($# == 1))
then
	
	if [[ -r $1 ]]
	then
		
		exec 4< $1
		read line <&4
		
		while [[ -n $line ]]
		do
			Val0=$(echo $line | cut -d'-' -f1)
			Val1=$(echo $line | cut -d' ' -f2)
			Val2=$(echo $line | cut -d' ' -f3)
			Val3=$(echo $line | cut -d' ' -f4)
			let Total=Val1+Val2+Val3
			echo "$Val0 $Total"
		read line <&4
		done
	else
		echo "$1 is not a readable file"
	fi

      

else
	echo "usage: ./sensor_sum.sh <filename>"
fi
exit 0
