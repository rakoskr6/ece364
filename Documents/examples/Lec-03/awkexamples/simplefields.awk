# Lines are separated into field variables
# $0 - the whole line
# $n - field N

# You can also create variables for use
BEGIN { 
    FS="," # FS is the field separator
    sum=0  # sum is a variable we have created
}

{ sum+=$3 }

END { print "Sum of 3rd field is " sum }

