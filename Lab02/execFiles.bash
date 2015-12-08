#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-08 17:13:15 -0400 (Tue, 08 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab02/execFiles.bash $  
#      $Revision: 81690 $   
#                 
#########################

if (($# == 0))
then
    ls ./c-files/*.c >tempoutput
    exec 4<tempoutput
    exec 2>/dev/null
    while read -a line <&4
    do
	FileName=$(echo $line | cut -d'/' -f3)
	Name=$(echo $FileName | cut -d'.' -f1)
	gcc -Wall -Werror $line -o a.out

	if (( $? == 0 ))
	then
	    echo "Compiling file $FileName... Compilation succeeded."
	    a.out > $Name.out
	else
	    echo "Compiling file $FileName... Error: Compilation failed."
	fi
	
    done

else
    echo "Usage: ./execFiles.bash"
    exit 1
fi
echo
rm -f tempoutput
exit 0