#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-27 16:59:38 -0400 (Tue, 27 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab08/vtools.py $
#      $Revision: 83031 $
#
#########################

import glob
import string
import re
import copy
import math
from pprint import pprint as pp


def isValidName(identifier):
    for char in identifier:
        if char not in (string.ascii_letters + string.digits + '_'):
            return False
    return True

def parsePinAssignment(assignment):
    both = assignment.split('(')
    if len(both) != 2:
        raise(ValueError(assignment))


    if both[0][0] != '.':
        raise(ValueError(assignment))
    port = both[0][1:]
    pin = both[1][0:-1]


    if isValidName(port) and isValidName(pin) and len(both) == 2 and both[1][-1] == ')':
        return (port,pin)
    raise(ValueError(assignment))


def parseNetLine(line):
    l = []
    items = line.split()
    if len(items) < 3:
        raise(ValueError(line))
    comp = items[0]
    instance = items[1]

    if isValidName(comp) == False or isValidName(instance) == False:
        raise(ValueError(line))

    assignments = items[2:]
    assignments[0] = assignments[0][1:]
    assignments[-1] = assignments[-1][0:-1]



    if len(assignments) < 2:
        for item in assignments:
            if type(item) == type('string'):
                assignments = item.split(',')







    for item in assignments:
        if item != '':
            if item[-1] == ',':
                l.append(parsePinAssignment(item[0:-1]))
            else:
                l.append(parsePinAssignment(item))

    x = tuple(l)

    return(comp,instance,x)







if __name__ == '__main__':
    #print(isValidName('hello_1'))
    #print(parsePinAssignment('.D(Q)'))
    #print(parsePinAssignment('D(Q)'))


    assignmentList = ("D", "serial_in"), ("CLK", "clk"), ("R", "1"), ("S", "n5"), ("Q", "Q_int1")
    expectedValue = "DFFSR", "Q_int1_reg", assignmentList
    actualValue = parseNetLine("DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )")


    print()
    print("Expected: ",end="")
    print(expectedValue)
    print("Actual: ",end="")
    print(actualValue)



















































































































































