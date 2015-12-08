
#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-01 16:59:58 -0400 (Tue, 01 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab01/advCalc.bash $  
#      $Revision: 81269 $   
#                 
#########################

if (($# == 1))
then
	if [[ -e $1 ]]
	then
	    
	    exec 4< $1
		read line <&4
		
		while [[ -n $line ]]
		do
		    #echo $line
			#Result=$(echo $line | simpleCalc.bash)
		    Result=$(simpleCalc.bash $line)
		    
		    if (( $? == 0 ))
		    then
			echo "$line: $Result"
		    else
			echo "$line: Error."
		    fi

		read line <&4
			
		done
	
	else
		echo "Error: input file does not exist"
		exit 2
	fi
else
	echo "Usage: ./advCalc.bash <filename>"
	exit 1
fi


exit 0
