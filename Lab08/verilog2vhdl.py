#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-27 17:22:10 -0400 (Tue, 27 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab08/verilog2vhdl.py $
#      $Revision: 83040 $
#
#########################

import glob
import string
import re
import copy
import math
import vtools
from pprint import pprint as pp


def convertLine(verilogLine):
    try:
        verilog = vtools.parseNetLine(verilogLine)
    except:
        return "Error: Bad Line."

    s = verilog[1] + ': ' + verilog[0] + ' PORT MAP('

    i = len(verilog[2])
    for item in verilog[2]:
        q = item[0] + '=>' + item[1]
        if i > 1:
            q += ', '
        else:
            q += ');'
        s += q
        i -= 1


    return s

def convertFile(sourceFile, targetFile):
    s = ''
    with open(sourceFile, 'r') as myFile:
        lines = myFile.readlines()


    with open(targetFile,'w') as myFile2:
        i = len(lines)
        for item in lines:
            vhdl = convertLine(item)
            if i > 1:
                s = vhdl + '\n'
            else:
                s = vhdl
            myFile2.writelines(s)
            i -= 1








if __name__ == '__main__':
    #print(isValidName('hello_1'))
    #print(parsePinAssignment('.D(Q)'))
    #print(parsePinAssignment('D(Q)'))


    test = convertLine("COMP_NAME INSTANCE_NAME (.PORT_NAME(PIN_NAME),.PORT2_NAME(PIN2_NAME))")
    test = convertFile('verilog_test.v','output_test.txt')
    print()
    print(test)



















































































































































