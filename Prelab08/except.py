#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-26 14:34:39 -0400 (Mon, 26 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab08/except.py $
#      $Revision: 82936 $
#
#########################

import glob
import string
import re
import copy
import math
from pprint import pprint as pp

l1 = input('Please enter some values: ')

l1 = l1.split()

sum = 0.0
for item in l1:
    try:
        sum += float(item)
    except:
        sum = sum

print("The sum is: ",end="")
print(sum)



#if __name__ == '__main__':





















































































































































