#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-26 14:34:39 -0400 (Mon, 26 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab08/parse.py $
#      $Revision: 82936 $
#
#########################

import glob
import string
import re
import copy
import math
import sys
from pprint import pprint as pp

if len(sys.argv) != 2:
    print("Usage: parse.py [filename]")
    exit()
try:
    with open(sys.argv[1],'r') as myFile:
        lines = myFile.readlines()
except:
    print(sys.argv[1],end=" ")
    print("is not a readable file.")
    exit()
sum = 0
s = ""
num = 0
for line in lines:
    line = line.split()
    for word in line:
        #print(word)
        try:
            sum += int(word)
            num += 1
        except:
            s += word
            s += ' '

    if num > 0:
        avg = sum / num
        print("{0:.3f}".format(avg),end=" ")
    print(s)
    s = ""
    num = 0
    sum = 0


#if __name__ == '__main__':