#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-05 23:15:17 -0400 (Mon, 05 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab06/prelab06_ee364f03.py $
#      $Revision: 82496 $
#
#########################

import glob
import string
import re
from pprint import pprint as pp

def part1(input):
    return re.search(' A{2,5} ',input)


def part2(input):
    return re.sub(r"-?[0-9]+\.*[0-9]*", "float", input)

def part3(input):
    return re.subn(r"-?[0-9]+\.*[0-9]*", "float", input)[1]


def part4(input):
    Sum = 0
    Match = re.findall(r"-?[0-9]+\.*[0-9]*", input)
    for item in Match:
        Sum += float(item)

    return Sum / len(Match)

def part5(input):
    return re.sub("EE364", "EE461", input, 1 )


def part6(input):
    Match = re.match(r"(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})$", input)

    if Match:
        return True
    return False



    if Match:
        for item in Match.group(1,2,3,4):
            if int(item) > 255:
                sum = 0
        return True
    return False


def part7(input):
    pass
    #re.search("e", input, re.I)
    #returns the location of e or E in a string

    #re.match("(.*)(is a)(.*)", input)
    #returns the location of "is a" inside s string

    #re.match("(?P<First>.*)(?P<Second>is a)(?P<Third>.*)", input)
    #returns the string seperated into three groups with "is a" the second group

    #re.search("(I){1}(like){10,}(you){1,2}", input)
    #finds one occurrences of I followed by at least 10 repetitions of "like" followed by 1 to 2 repetitions of you







if __name__ == '__main__':

    test = part7('akjkdis alaasd')
    print(test)

