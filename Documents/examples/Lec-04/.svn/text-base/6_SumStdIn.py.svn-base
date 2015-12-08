#! /usr/bin/env python

# Program reads from standard input and
# prints the sum of the data read

import sys

Sum = 0
while (1):

    Line_Of_Text = sys.stdin.readline()

    if len(Line_Of_Text) > 0:
      
        print "%s" % (Line_Of_Text),

        Line_Of_Text = Line_Of_Text.strip()

        Data = Line_Of_Text.split()
 
        print Data

        for I in range(len(Data)):
            Sum = Sum + float(Data[I])

    else:

        # End of file found

        break

print "Sum of data: %f" % (Sum)

sys.exit (0)
