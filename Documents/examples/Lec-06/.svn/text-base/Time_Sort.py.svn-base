#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/02/26 21:16:42 $
# $Revision: 1.2 $

import time
#import whrandom
import random
import os
import sys
import Sort
 
def Main ():

    ERROR = 1
    NO_ERRORS_DETECTED = 0

    MAX_N = 10000
    MAX_SEED = 255

    RAW_FILE_NAME = "Raw"
    SORTED_FILE_NAME = "Sorted"
    
    Prompt = "Select a sorting Algorithm: "
    Reply = None
    while Reply == None:
        print
        print "Enter the number of the sorting"
        print "algorithm followed by return/enter"
        print "   0: Exit"
        print "   1: Quick Sort"
        print "   2: Quick_MI Sort"
        print "   3: Radix Sort"
        print "   4: Insertion Sort"
        print "   5: Tree Sort"
        print "   6: Cook_Kim Sort"
        print "Your Selection: ",

        Reply = sys.stdin.readline()
        Reply = Reply.strip()
        try:
            Reply = int(Reply)
        except ValueError, Message:
            print
            print "ERROR: Invalid data entered"
            print "   %s" % (Message)
            Reply = None
        else:
            print
            if (    (Reply < 0) \
                 or (Reply > 6)):
                print "ERROR: Invalid Selection %d" % (Reply)
                Reply = None
            elif Reply == 0:
                sys.exit(NO_ERRORS_DETECTED)
            elif Reply == 1:
                Algorithm = "Quick"
            elif Reply == 2:
                Algorithm = "Quick_MI"
            elif Reply == 3:
                Algorithm = "Radix"
            elif Reply == 4:
                Algorithm = "Insertion"
            elif Reply == 5:
                Algorithm = "Tree"
            elif Reply == 6:
                Algorithm = "Cook_Kim"
            else:
                Reply = None

    N = None
    while N == None:
        print
        print "Please enter the number of items to"
        print "be sorted followed by a return/enter"
        print "    0 <= N <= %d" % (MAX_N)
        print "N: ",
    
        N = sys.stdin.readline()
        N = N.strip()
    
        try:
            N = int(N)
        except ValueError, Message:
            print "ERROR: Invalid data entered"
            print "   %s" % (Message)
            N = None
        else:
            print
            if (    (N < 0)
                 or (N > MAX_N)):
                print "ERROR: N = %d is out of range" % (N)
                print "    0 <= N <= %d" % (MAX_N)
                N = None

    Seed = None
    while Seed == None:
        print
        print "Please enter a seed for the random"
        print "number generator followed by a return/enter"
        print "A seed of 0 uses the current clock time as seed"
        print "    0 <= Seed <= %d" % (MAX_SEED)
        print "Seed: ",
    
        Seed = sys.stdin.readline()
        Seed = Seed.strip()
    
        try:
            Seed = int(Seed)
        except ValueError, Message:
            print "ERROR: Invalid data entered"
            print "   %s" % (Message)
            Seed = None
        else:
            print
            if (    (Seed < 0)
                 or (Seed > MAX_SEED)):
                print "ERROR: Seed = %d is out of range" % (Seed)
                print "    0 <= Seed <= %d" % (MAX_SEED)
                Seed = None

    #Random = whrandom.whrandom()
    #Random.seed (0, 0, Seed)
    Random = random.Random(Seed)
    
    Start = time.time()

    Unsorted = []
    for I in range(0, N):
        Value = Random.randint(0, 0x7FFFFFE)
        if Random.random() < 0.5:
            Unsorted.append(-Value)
        else:
            Unsorted.append(Value)
    
    Stop = time.time()

    print "  Build list time for %6d Items: %8.3f in seconds"  \
        % (len(Unsorted), (Stop - Start))

    Start = time.time ()

    try:
        Raw_File = open (RAW_FILE_NAME, "w")
    except IOError, Message:
        print "ERROR Unable to open file %s for writing" \
           % (RAW_FILE_NAME)
        print "   %s" % (Message)
        sys.exit(ERROR)

    for I in range (0, len(Unsorted)):
        Raw_File.write("%10d\n" % (Unsorted[I]))
    Raw_File.close()

    if len(Unsorted) <= 10:
        print "Unsorted list"
        print Unsorted

    Stop = time.time()

    print "   Write raw time for %6d Items: %8.3f in seconds"  \
        % (len(Unsorted), (Stop - Start))

    Sorted = []

    Start = time.time()

    if Algorithm == "Quick":
        Sorted = Sort.Quick (Unsorted, 0, len(Unsorted)-1)
    elif Algorithm == "Quick_MI":
        Sorted = Sort.Quick_MI (Unsorted, 0, len(Unsorted)-1)
    elif Algorithm == "Radix":
        Sorted = Sort.Radix (Unsorted)
    elif Algorithm == "Insertion":
        Sorted = Sort.Insertion (Unsorted)
    elif Algorithm == "Tree":
        Sorted = Sort.Tree (Unsorted)
    elif Algorithm == "Cook_Kim":
        Sorted = Sort.Cook_Kim (Unsorted)

    Stop = time.time()

    print "        Sort time for %6d Items: %8.3f in seconds"  \
        % (len(Sorted), (Stop - Start)),
    print "for %s" % (Algorithm)

    Start = time.time ()

    Sorted_File = open (SORTED_FILE_NAME, "w")
    try:
        Sorted_File = open (SORTED_FILE_NAME, "w")
    except IOError, Message:
        print "ERROR Unable to open file %s for writing" \
           % (SORTED_FILE_NAME)
        print "    %s" % (Message)
        sys.exit(ERROR)

    for I in range (0, len(Sorted)):
        Sorted_File.write("%10d\n" % (Sorted[I]))
    Sorted_File.close()

    if len(Sorted) <= 10:
        print "Sorted list"
        print Sorted

    Stop = time.time()

    print "Write sorted time for %6d Items: %8.3f in second"  \
        % (len(Sorted), (Stop - Start))

    print
    sys.exit(NO_ERRORS_DETECTED)
Main()
