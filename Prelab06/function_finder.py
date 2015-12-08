#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-04 15:18:11 -0400 (Sun, 04 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab06/function_finder.py $
#      $Revision: 82395 $
#
#########################

import glob
import string
import sys
import re

import os
from pprint import pprint as pp

if len(sys.argv[:]) != 2:
    print("Usage: function_finder.py [python_file_name]")
    exit()

file = sys.argv[1]
if not os.access((file),os.R_OK):
    print("Error: Could not read ",end="")
    print(file)
    exit()

with open(file,'r') as myFile:
    lines = myFile.readlines()
    for line in lines:
        i = 1
        test = re.match(r"def *(?P<funcname>[a-zA-Z]?[a-zA-Z0-9_-]*) *\((?P<arguments>[a-zA-Z0-9_,= -]*)\):", line)


        if test:
            print(test.group("funcname"))

            arg = test.group("arguments").split(',')

            for item in arg:
                print("Arg",end='')
                print(i,end=': ')
                print(item.strip())
                i += 1


            #print(test.group("arguments"))
            #print(arg)


