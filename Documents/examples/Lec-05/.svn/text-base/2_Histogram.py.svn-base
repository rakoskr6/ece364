#! /usr/bin/env python

import sys, os

# Reads in an input file and countes the number of times each word appears
# Then prompts the user to enter a word and displays the count

if len(sys.argv) != 2:
    sys.stderr.write("usage: 2_Histogram.py <file>\n")
    sys.exit(1)

if not os.access(sys.argv[1], os.R_OK) or not os.path.isfile(sys.argv[1]):
    sys.stderr.write("error: can not read %s\n" % (sys.argv[1],))
    sys.exit(1)

fp = open(sys.argv[1], "r")

# Use a dictionary to store the word:count key:value pairs
words = {}

for line in fp:
    # convert each word to lowercase and put into a list
    line = line.strip().lower().split()

    for word in line:
        if not word in words:
            words[word] = 1
        else:
            words[word] += 1

fp.close()

# Prompt the user for a word to lookup:
while(1):
    word = raw_input("Enter a word to query: ").strip().lower()
    
    # Exit on empty words
    if len(word) == 0:
        break

    if word in words:
        print "%s occurred %d times." % (word, words[word])
    else:
        print "%s never occurred." % (word,)


sys.exit(0)
