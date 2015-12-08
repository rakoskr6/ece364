#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-08-31 21:04:25 -0400 (Mon, 31 Aug 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab01/svncheck.bash $  
#      $Revision: 80892 $   
#                 
#########################
	
if [[ -e file_list ]]
then
	exec 4< file_list
	read line <&4
	while [[ -n $line ]]
	do
		if [[ -e $line ]]
		then	
			StatusCheck=$(svn status $line)
			if [[ $StatusCheck == "" ]] #then in svn
			then
				echo -n "$line in SVN "
				PermissionCheck=$(ls -l $line)
				PermissionCheck=${PermissionCheck:3:1}
				if [[ $PermissionCheck == "x" ]] #executable
				then
					echo "and is executable"
				else
					echo "and not executable"
					echo "Would you like to make it executable? [y]"
					read  MakeExec
					if [[ $MakeExec == "y" ]]
					then
						svn propset svn:executable ON $line
					fi
				fi

			else
				echo -n "$line not in SVN "
				PermissionCheck=$(ls -l $line)
				PermissionCheck=${PermissionCheck:3:1}
				if [[ $PermissionCheck == "x" ]] #executable
				then
					echo "and is executable"
				else
					echo "and not executable"
					echo "Would you like to make it executable? [y]"
					read MakeExec
					if [[ $MakeExec == "y" ]]
					then	
						chmod +x $line
					fi
				fi
			fi
						
		else
			echo "Error: File $line appears to not exist here or in svn"
		fi
		read line <&4
	done 
	
		
else
	echo "Cannot read file_list"
fi #< file_list

echo "Auto-committing code"
svn commit

exit 0
