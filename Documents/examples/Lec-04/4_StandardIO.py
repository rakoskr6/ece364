#! /usr/bin/env python

import sys

# Read all lines from stdin and echo them back with a line number

n=0
for line in sys.stdin:
    n += 1
    sys.stdout.write("%d: %s" % (n, line))


sys.exit(0)
