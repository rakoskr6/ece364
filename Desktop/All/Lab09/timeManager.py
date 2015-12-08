#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-11-03 16:59:31 -0500 (Tue, 03 Nov 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab09/timeManager.py $
#      $Revision: 83108 $
#
#########################

import glob
import string
import re
import copy
import math
import timeDuration as du
from pprint import pprint as pp

def getTotalDuration(experimentName):
    filename = "Experiments.txt"
    with open(filename,'r') as myFile:
        lines = myFile.readlines()
    i = 3
    total = du.Duration()
    for line in lines:
        if i <= 0:
            lines2 = line.split()
            #lines3 = lines2[1]
            #print(lines2)

            minutes2 = lines2[1].split(':')[0]
            seconds2 = lines2[1].split(':')[1]
            itter = lines2[2]

            if lines2[0] == experimentName:
                temp = du.Duration(minutes=int(minutes2), seconds=int(seconds2))
                if int(itter) > 0:
                    temp = temp * int(itter)
                elif int(itter) == 0:
                  temp = du.Duration()

                total = total + temp

        i -= 1
    return total

def rankExperiments(*args):
    l = []
    l2 = []
    d = {}
    for item in args:
        tot = getTotalDuration(item)
        d[tot.getTotalSeconds()] = item
        l.append((getTotalDuration(item).getTotalSeconds()))
    l.sort()

    i = 0
    for item in l:
        l[i] = d[item]
        i += 1

    x = len(l) - 1
    i = 0
    for item in l:
        l2.append(l[x])
        i += 1
        x -= 1
    return l2


if __name__ == '__main__':
    test = rankExperiments('Experiment13','Experiment07')
    print(getTotalDuration('Experiment13'))
    print(getTotalDuration('Experiment07'))
    print(test)














































































































































