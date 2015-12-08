
#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-01 16:35:34 -0400 (Tue, 01 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab01/simpleCalc.bash $  
#      $Revision: 81244 $   
#                 
#########################

if (($# == 3))
then
	if [[ $1 = "add" || $1 == "sub"|| $1 == "mul"|| $1 == "div"|| $1 == "exp"|| $1 == "mod" ]]
	then
	    if [[ $1 = "add" ]]
	    then
		((Result=$2+$3))
		echo "$2 + $3 = $Result"
	    fi
	    if [[ $1 = "sub" ]]
	    then
		((Result=$2-$3))
		echo "$2 - $3 = $Result"
	    fi

	    if [[ $1 = "mul" ]]
	    then
		((Result=$2*$3))
		echo "$2 * $3 = $Result"
	    fi

	    if [[ $1 = "div" ]]
	    then
		((Result=$2/$3))
		echo "$2 / $3 = $Result"
	    fi

	    if [[ $1 = "exp" ]]
	    then
		((Result=$2**$3))
		echo "$2 ^ $3 = $Result"
	    fi

	    if [[ $1 = "mod" ]]
	    then
		((Result=$2%$3))
		echo "$2 % $3 = $Result"
	    fi

	else
		echo "Error: invalid operator"
		exit 2
	fi
else
	echo "Usage: ./simpleCalc.bash <operator> <operand1> <operand2>"
	exit 1
fi


exit 0
