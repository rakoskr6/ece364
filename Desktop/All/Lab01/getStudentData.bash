
#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-01 16:22:42 -0400 (Tue, 01 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab01/getStudentData.bash $  
#      $Revision: 81236 $   
#                 
#########################

if (($# == 1))
then
	if [[ $1 == "ece364" || $1 == "ece337" ]]
	then
	    
	    ((Students=0))
	    ((TotalScore=0))
	    ((HighScore=0))
	    
	    for ((i = 0; i<= 9; i++))
	    do
		filename="./gradebooks/$1_$i.txt"
		
		if [[ -e $filename ]]
		then
		    exec 4< $filename
		    read line <&4
		    while [[ -n $line ]]
		    do
			((Students=$Students + 1))
			((Score=$(echo $line | cut -d',' -f2)))
			((TotalScore=TotalScore+Score))

			if (( $Score >= $HighScore ))
			then
			   HighStudent=$(echo $line | cut -d',' -f1)
			   ((HighScore=$Score))
			fi
			#echo "$line: $Score  ($TotalScore)    ($HighStudent - $HighScore)"
			read line <&4
		    done

		fi
	    
	      
	    done
	    ((AverageScore=$TotalScore/$Students))
	    echo "Total students: $Students"
	    echo "Average score: $AverageScore"
	    echo "$HighStudent had the highest score of $HighScore"
	else
		echo "Error: course $1 is not a valid option"
		exit 2
	fi
else
	echo "Usage: ./getStudentData.bash <course name>"
	exit 1
fi


exit 0
