#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-08-31 21:09:14 -0400 (Mon, 31 Aug 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab01/sum.bash $  
#      $Revision: 80898 $   
#                 
#########################

let Sum=0
for ((I = $#; I > 0; I--))
do
	((Sum=$1+Sum))
	shift
done

echo $Sum
exit 0
