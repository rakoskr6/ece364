#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-04 14:44:11 -0400 (Sun, 04 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab06/ip_detect.py $
#      $Revision: 82392 $
#
#########################

import glob
import string
import sys
from pprint import pprint as pp
import re

#def ip_detect(file):
file = sys.argv[1]
#file = "addys.in"
i = 0
x = 0
with open(file,'r') as myFile:
    lines = myFile.readlines()
    for line in lines:
        Match = re.match(r"(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2}):(\w*)", line)

        if Match:
            print(Match.group(0),end=" - ")

            if re.match("[0-9]*$",Match.group(5)):
                if int(Match.group(5)) < 1024:
                    print("Valid (root privileges required)")
                elif int(Match.group(5)) < 32767:
                    print("Valid")
                else:
                    print("Invalid Port Number")
            else:
                print("Invalid Port Number")
        else:
            line = re.sub("\n", "", line)
            print(line,end="")
            print(" - Invalid IP Address")





#if __name__ == '__main__':

    #test = openFile("bad1.sud")
    #print(test)

    #test = ip_detect()
    #print(test)

    # print()
    # print('-----------------------------')
    # print()
