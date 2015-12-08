#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-29 17:32:50 -0400 (Tue, 29 Sep 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab05/practical1.py $
#      $Revision: 82312 $
#
#########################

import glob
import string
from pprint import pprint as pp

def verifySolution(file):
    rowsum = 0
    i = 0
    x = 0
    colsum = [0,0,0,0,0,0,0,0,0]
    with open(file,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            line = line.strip()
            rowsum = 0
            i = 0
            for number in line[:]:
                if int(number) > 0 and int(number) < 10:
                    rowsum += int(number)
                    colsum[i] += int(number)
                else:
                    return False
                i += 1


            if rowsum != 45:
                return False
    for item in colsum:
        if item != 45:
            return False


    return True

def missing(sourceFileName):
    i = 0
    x = 0
    colsum = [0,0,0,0,0,0,0,0,0]
    rowsum = [0,0,0,0,0,0,0,0,0]
    with open(sourceFileName,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            line = line.strip()
            row = 0
            i = 0
            for number in line[:]:
                if number != '.':
                    row += int(number)
                    colsum[i] += int(number)
                i += 1
            rowsum[x] = row
            x += 1


    for item in colsum:
        if item == 0:
            return "Column"


    return "Row"

def solvePuzzle(sourceFileName, targetFileName):
    miss = missing(sourceFileName)


    i = 0
    x = 0
    colsum = [0,0,0,0,0,0,0,0,0]
    rowsum = [0,0,0,0,0,0,0,0,0]
    sol = [0,0,0,0,0,0,0,0,0]
    with open(sourceFileName,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            line = line.strip()
            row = 0
            i = 0
            for number in line[:]:
                if number != '.':
                    row += int(number)
                    colsum[i] += int(number)
                i += 1
            rowsum[x] = row
            x += 1

    i = 0
    if (miss == "Row"):
        for item in colsum:
            sol[i] = 45 - item
            i += 1
    else:
        for item in rowsum:
            sol[i] = 45 - item
            i += 1


    Out = open(targetFileName,"w")

    with open(sourceFileName,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            line = line.strip()
            row = 0
            i = 0
            for number in line[:]:
                if number != '.':
                    Out.write(str(number))

            else:
                    Out.write(str(sol[i]))
            i += 1
            Out.write("\n")





    Out.close()




    return sol

def getCallersOf(phonenumber):
    file = 'Users.txt'
    i = 0
    names = {}

    with open(file,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            words = line.split()
            if i > 1:
                names[words[3]] = (words[0] + ' ' + words[1])
            i += 1
    return "Kyle"



def getCallActivity():
    return 0







if __name__ == '__main__':

    #test = openFile("bad1.sud")
    #print(test)

    test = solvePuzzle("sudoku_open1.sud",'out.sud')
    print(test)

    # print()
    # print('-----------------------------')
    # print()
