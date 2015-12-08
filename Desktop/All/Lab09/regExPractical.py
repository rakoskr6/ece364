#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-11-03 17:28:24 -0500 (Tue, 03 Nov 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab09/regExPractical.py $
#      $Revision: 83137 $
#
#########################

import glob
import string
import re
import copy
import math
from pprint import pprint as pp


def getNumber(stringInput):
    found =  re.search(r"[+|-]?\d\.\d+[e|E][+|-]?\d+",stringInput)
    if found:
        return found.group(0)
    else:
        return None

def getOptions(commandline):
    l = []
    f = re.findall(r"-[a-z]? +[a-zA-Z0-9/:.]+",commandline)
    for item in f:
        #print(item)
        #print('is')
        x1 = re.findall(r"[a-z]",item)
        x2 = re.findall(r"[a-zA-Z0-9/:.]+",item)
        #print(x2)

        t = (x1[0],x2[1])
        l.append(t)

    l.sort()

    return l

def getAddressParts(url):
    return None

def getAttributes(xmlSnippet):
    return None

if __name__ == '__main__':
    print(getOptions("script.bash -v -z 2 -p /local/bin"))
















































































































































