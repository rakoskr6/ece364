#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-08 16:41:28 -0400 (Tue, 08 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab02/printUsageStats.bash $  
#      $Revision: 81674 $   
#                 
#########################

if (($# == 1))
then
    
    if [[ -e $1 ]]
    then
	exec 4< $1
	read -a line <&4
	echo "Parsing file \"$1\". Timestamp: ${line[2]}"

	echo "Your choices are:"
	echo "1) Active user IDs"
	echo "2) Highest CPU usage"
	echo "3) Top 3 longest running processes"
	echo "4) All processes by a specific user"
	echo "5) Exit"

	((Input=0))
	while (( $Input != 5 ))
	do
	    read -p "Please enter your choice: " Input
	    
	    if (( $Input == 1 ))
	    then
		exec 4< $1
		read -a line <&4
		echo "Total number of active user IDs: ${line[7]}"
		echo

	    elif (( $Input == 2 ))
	    then
		exec 4< $1
		for ((i=0; i<8;i++))
		do
		    read -a line <&4
		done
		echo "User ${line[1]} is utilizing the highest CPU resources at ${line[8]}%"
		echo

	    elif (( $Input == 3 ))
	    then
		tail -n +8 $1 | sort -k11 -n -r | head -n 3
		echo
	

	    elif (( $Input == 4 ))
	    then
		read -p "Please enter a valid username: " UserSearch
		read -p "Please enter a filename to save user's process: " SaveFile

		((Found=0))
		exec 4< $1
		while read -a line <&4
		do
		    if [[ $UserSearch = ${line[1]} ]]
		    then
			if (( $Found == 0 ))
			then
			    rm -f $SaveFile
			    touch $SaveFile
			fi
			
			echo ${line[*]} >> $SaveFile
			((Found=$Found+1))
		    fi
		    
		done
		if (( $Found == 0 ))
		then
		    echo "No match found"
		else
		    echo "Input written to file $SaveFile"
		    echo
		fi
	    fi
	done
	exit 0



    else
	echo "Error: $1 does not exist"
	exit 2
    fi
    

else
    echo "Usage: ./printUsageStats.bash <filename>"
    exit 1
fi
exit 0