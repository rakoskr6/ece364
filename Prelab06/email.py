#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-04 14:34:50 -0400 (Sun, 04 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab06/email.py $
#      $Revision: 82391 $
#
#########################

import glob
import string
import re
from pprint import pprint as pp

def email():
    file = "Part2.in"
    i = 0
    x = 0
    with open(file,'r') as myFile:
        lines = myFile.readlines()

        for line in lines:
            line = line.strip()
            line = re.sub("@purdue.edu","@ecn.purdue.edu",line)
            line = line + "/100"
            print(line)







if __name__ == '__main__':

    #test = openFile("bad1.sud")
    #print(test)

    test = email()
   #print(test)

    # print()
    # print('-----------------------------')
    # print()
