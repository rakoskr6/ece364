
#! /bin/bash
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-29 16:35:58 -0400 (Tue, 29 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab05/benchmarks.bash $  
#      $Revision: 82273 $   
#                 
#########################

if (($# == 1))
then

    read -p "Enter the array size(s): " ArraySize
    read -p "Enter the algorithm(s): " Algs
    ArraySize=($ArraySize)
    Algs=($Algs)
    deletethis="deletethis.txt"
    
    read -p "Enter column # to sort benchmarks " Colmn
    if ((Colmn < 2 || Colmn > ${#ArraySize[*]}+1))
    then
	echo "Error: invalid column number"
	exit 4
    fi


    touch $1
    rm  $1
    echo -n "size" >>$1
    for ((x = 0; x < ${#ArraySize[*]}; x++))
    do
	echo -n ",${ArraySize[x]}">>$1
    done
    echo>>$1

   for ((i = 0; i < ${#Algs[*]}; i++))
   do
       echo -n "${Algs[i]}" >>$1
       for ((x = 0; x < ${#ArraySize[*]}; x++))
       do
	   orig=$(sorting ${ArraySize[x]}  ${Algs[i]} | cut -d' ' -f3)
	  
	   sorting ${ArraySize[x]}  ${Algs[i]}>>$deletethis
	   rvalue=$?
	   rm $deletethis
	   if (($rvalue == 2))
	   then
	       echo  "Error: invalid size of array"
	       rm $1
	       exit 2
	   elif (($rvalue == 5))
	   then
	       echo "Error: invalid algorithm name."
	       rm $1
	       exit 5
	   fi
	   echo -n ",$orig" >> $1

       done
       echo>>$1
   done

   cp $1 $1.sorted

else
	echo "Usage: ./benchmarks.bash <outputFile>"
	exit 1
fi


exit 0
