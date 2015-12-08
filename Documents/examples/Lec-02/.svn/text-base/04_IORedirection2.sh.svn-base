#! /bin/bash

#
# $Id$
#

# Note: The scores file is provided as input

# Standard checks to make sure correct argument is passed
if [[ $# != 1 ]]
then
		echo "usage: $0 <file_name>"
		exit 1
fi

if [[ ! -f $1 || ! -r $1 ]]
then
		echo "error: $1 is not readable"
		exit 2
fi

# The read command always reads from standard input unless you explicitly
# redirect a stream into it. (See lecture 2 Advanced I/O Redirection)
# 
# When read is used in conjunction with a while loop you can perform redirection
# at the end of the loop rather than at each read command. This loop redirects the
# file passed in the 1st command line argument to standard input of the while loop.
# When the while loop executes a read command it will read from standard input but 
# because of the redirection this will be the contents of the input file and not the
# keyboard
while read course_id
do
		# Sometimes you need to read more than one line per loop iteration.
		# Things can get messy if you start using counters to keep track of
		# the line number so most of the time just putting additional read
		# commands is sufficient.
		read -a prelab_scores
		read -a lab_scores

		# Notice that these read commands to not include explicit redirection.
		# Standard input is still redirected within the loop body so the other
		# read commands will also read from the input file.

		# Find the maximum prelab score from the list of prelab scores
		max_prelab=${prelab_scores[0]}	 
		for (( i = 1; i < ${#prelab_scores[*]}; i++ ))
		do
				if (( ${prelab_scores[$i]} > $max_prelab ))
			  then
						max_prelab=${prelab_scores[$i]}
				fi
		done

		# This is an example of calling another script and capturing its output
		# Take a look at maximum.sh to see what it does. Notice that we pass the
		# entire list of lab scores to the script simply by putting the variable
		# inside of the $(...). Before maximum.sh is run the list of lab scores
		# will be expanded into a whitespace separated list and passed as command
		# line arguments to maximum.sh
		max_lab=$(./maximum.sh ${lab_scores[*]})
	  echo "${course_id}: max prelab: $max_prelab, max lab: $max_lab"
done < $1


exit 0