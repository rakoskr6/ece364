#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/09/10 19:59:43 $
# $Revision: 1.3 $

import sys

# Counts the number of bytes (characters), words and lines read from stdin.

Byte_Count = 0
Word_Count = 0
Line_Count = 0
Words = []

# This is another way to read lines 
while (1):

    Line_Of_Text = sys.stdin.readline()

    if len(Line_Of_Text) > 0:
      
        # Comma at end of line is needed to
        # suppress the extra new line character

        sys.stdout.write(Line_Of_Text)

        # Get the list of whitespace separated words
        Words = Line_Of_Text.split()

        Line_Count = Line_Count + 1
        Word_Count = Word_Count + len(Words)
        Byte_Count = Byte_Count + len(Line_Of_Text)
    else:
        # End of file found
        break

print
print "Total lines: %d" % (Line_Count)
print "Total words: %d" % (Word_Count)
print "Total bytes: %d" % (Byte_Count)

sys.exit(0)
