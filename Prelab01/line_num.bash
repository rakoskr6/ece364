
#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-08-31 21:09:14 -0400 (Mon, 31 Aug 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab01/line_num.bash $  
#      $Revision: 80898 $   
#                 
#########################

if (($# == 1))
then
	
	if [[ -e $1 ]]
	then
		if [[ -r $1 ]] 
		then
			exec 4< $1
			read line <&4
			((i = 1))
			while [[ -n $line ]]
			do
				echo "$i:$line"
				read line <&4
				((i++))
			done
		fi
	else
		echo "Cannot read $1"
	fi
else
	echo "Usage: line_num.bash <filename>"
fi


exit 0
