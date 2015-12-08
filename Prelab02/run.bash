#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-07 13:41:18 -0400 (Mon, 07 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab02/run.bash $  
#      $Revision: 81488 $   
#                 
#########################
IFS=' :'
if (($# == 2))
then
    rm quick_sim -f
    gcc $1 -o quick_sim

    if (( $? != 0 ))
    then
	echo "error: quick_sim could not be compiled"
	exit 2
    fi

    Output=$2

    if [[ -e $Output ]]
    then
	echo -n "$2 exists. Would you like to delete it? "
	read Replace
	if [[ $Replace == 'y' ]]
	then
	    rm $Output -f
	else
	    read -p "Enter a new filename: " Output
	    rm -f $Output

	fi
	touch $Output
    fi
    ((Fastest=999999))

    for ((c=1; c<=32; c=c*2))
    do
    for ((i=1; i<=16; i=i*2))
    do
	quick_sim $c $i a >OrigResults
	read -a line <OrigResults
	CPI=${line[14]}
	((Exec=${line[19]}))
	echo "AMD Opteron:$c:$i:$CPI:$Exec">>$Output
	if (( Exec <= $Fastest ))
	then
	    ((Fastest=$Exec))
	    Cach=$c
	    Width=$i
	    Processor="AMD Opteron"
	fi


	quick_sim $c $i i >OrigResults
	read -a line <OrigResults
	CPI=${line[15]}
	((Exec=${line[20]}))
	echo "Intel Core i7:$c:$i:$CPI:$Exec">>$Output
	if (( Exec <= $Fastest ))
	then
	    ((Fastest=$Exec))
	    Cach=$c
	    Width=$i
	    Processor="Intel Core i7"
	fi

    done
    done
echo "Fastest run time achieved by $Processor with cach size $Cach and issue width $Width was $Exec"


else
    echo "Usage: run.bash <sourcefilename> <outputfilename>"
exit 1
fi
exit 0