#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-08-31 21:09:14 -0400 (Mon, 31 Aug 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab01/check_file.bash $  
#      $Revision: 80898 $   
#                 
#########################

if (($# == 1))
then
	
	if [[ -e $1 ]]
	then
		echo "$1 exists"
	else
		echo "$1 does not exist"
	fi

	if [[ -d $1 ]]
	then
		echo "$1 is a directory"
	else
		echo "$1 is not a directory"
	fi

        if [[ -f $1 ]]
        then
               	echo "$1 is an ordinary file"
        else
               	echo "$1 is not an ordinary file"
        fi



        if [[ -r $1 ]]
        then
               	echo "$1 is readable"
        else
               	echo "$1 is not readable"
        fi


        if [[ -w $1 ]]
        then
               	echo "$1 is writable"
        else
               	echo "$1 is not writable"
        fi



        if [[ -x $1 ]]
        then
               	echo "$1 is executable"
        else
               	echo "$1 is not executable"
        fi

else
	echo "Usage: ./check_file.bash <filename>"
fi
exit 0
