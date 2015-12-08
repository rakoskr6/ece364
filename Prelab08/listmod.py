#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-26 14:06:37 -0400 (Mon, 26 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab08/listmod.py $
#      $Revision: 82932 $
#
#########################

import glob
import string
import re
import copy
import math
from pprint import pprint as pp
def find_median(List_1, List_2):
    median = 0

    l3 = List_1 + List_2
    l3.sort()
    middle = math.floor((len(l3) - 1) / 2)

    return (l3[middle],l3)



#if __name__ == '__main__':





















































































































































