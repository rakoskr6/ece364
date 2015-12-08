#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-08-31 21:09:14 -0400 (Mon, 31 Aug 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab01/exist.bash $  
#      $Revision: 80898 $   
#                 
#########################

for ((I = $#; I > 0; I--))
do
	if [[ -e $1 ]]
	then
		if [[ -r $1 ]] 
		then
			echo "File $1 is readable!"
		fi
	else
		touch $1
	fi

	shift
done


exit 0
