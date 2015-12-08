#! /usr/bin/env python

import sys

# Reverse each line from stdin and send it to stdout

for line in sys.stdin:
    items = line.split()

    # Watch out! reverse does not return anything! so don't assign its result
    items.reverse()

    # Assume all of the whitespace was a single space...    
    sys.stdout.write(" ".join(items) + "\n")

sys.exit(0)

