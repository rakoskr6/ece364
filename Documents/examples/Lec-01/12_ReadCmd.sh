#! /bin/bash

#
# $Id$
#

echo -n "Enter a line of text: "
read aLineOfText
echo "You entered: " $aLineOfText
echo

read -p "How old are you? " age
echo "You are $age years old."
echo

echo "Press [ENTER] to continue..."
read

read -p "Enter your first and last name: " first last rest

echo "First Name: $first"
echo "Last Name: $last"
echo "The rest of the text you entered: $rest"

exit 0