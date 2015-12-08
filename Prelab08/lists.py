#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-26 14:06:37 -0400 (Mon, 26 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab08/lists.py $
#      $Revision: 82932 $
#
#########################

import glob
import string
import re
import copy
import math
import listmod
from pprint import pprint as pp


l1 = input('Enter the first list of numbers: ')
l2 = input('Enter the second list of numbers: ')

l1 = l1.split()
l2 = l2.split()
l1 = list(map(int,l1))
l2 = list(map(int,l2))

print("First list: ",end="")
print(l1)
print("Second list: ",end="")
print(l2)
x = listmod.find_median(l1,l2)
print("Merged list: ",end="")
print(x[1])
print("Median: ",end="")
print(x[0])




#if __name__ == '__main__':





















































































































































