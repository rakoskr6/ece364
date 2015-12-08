#! /usr/bin/env python

# Try the nums1, nums2, nums3 input

import sys, os

if len(sys.argv) != 4:
    sys.stderr.write("usgae: %s <file1> <file2> <file3>\n" % (sys.argv[0],))
    sys.exit(1)

for f in sys.argv[1:]:
    if not os.path.isfile(f) or not os.access(f, os.R_OK):
        sys.stderr.write("error: %s is not a readable file.\n" % (f,))
        sys.exit(2)

fp1=open(sys.argv[1], "r")
fp2=open(sys.argv[2], "r")
fp3=open(sys.argv[3], "r")

while True:
    
    # Read from each file
    D1=fp1.readline().strip()
    D2=fp2.readline().strip()
    D3=fp3.readline().strip()

    if not (D1 and D2 and D3):
        break


    # Assume the input will be well formated
    D1=int(D1)
    D2=int(D2)
    D3=int(D3)
    
    # Find the largest (create a temporary tuple)
    largest=max((D1, D2, D3))

    sys.stdout.write("Largest of %d %d %d is: %d\n" % (D1, D2, D3, largest))

sys.exit(0)
