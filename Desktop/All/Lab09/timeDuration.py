#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-11-03 16:59:31 -0500 (Tue, 03 Nov 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab09/timeDuration.py $
#      $Revision: 83108 $
#
#########################

import glob
import string
import re
import copy
import math
from pprint import pprint as pp

class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if type(hours) != type(1) or type(minutes) != type(1) or type(seconds) != type(1):
            raise TypeError
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError

        if seconds >= 60:
            minutes += seconds // 60
            seconds = seconds % 60
        if minutes >= 60:
            hours += minutes //60
            minutes = minutes % 60


        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        s = str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds)
        if self.seconds < 9 and self.minutes < 9 and self.hours < 9:
            s = '0' + str(self.hours) + ':0' + str(self.minutes) + ':0' + str(self.seconds)
        if self.seconds < 9 and self.minutes < 9 and self.hours > 9:
            s = str(self.hours) + ':0' + str(self.minutes) + ':0' + str(self.seconds)

        if self.seconds < 9 and self.minutes > 9 and self.hours < 9:
            s = '0' + str(self.hours) + ':' + str(self.minutes) + ':0' + str(self.seconds)
        if self.seconds < 9 and self.minutes > 9 and self.hours > 9:
            s = str(self.hours) + ':' + str(self.minutes) + ':0' + str(self.seconds)

        if self.seconds > 9 and self.minutes < 9 and self.hours < 9:
            s = '0' + str(self.hours) + ':0' + str(self.minutes) + ':' + str(self.seconds)
        if self.seconds > 9 and self.minutes < 9 and self.hours > 9:
            s = str(self.hours) + ':0' + str(self.minutes) + ':' + str(self.seconds)

        if self.seconds > 9 and self.minutes > 9 and self.hours < 9:
            s = '0' + str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds)
        if self.seconds > 9 and self.minutes > 9 and self.hours > 9:
            s = str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds)

        return s

    def getTotalSeconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError("Duration instance expected")
        totals = self.getTotalSeconds() + other.getTotalSeconds()
        return Duration(seconds = totals)

    def __mul__(self, other):
        if type(other) != type(1):
            raise TypeError("Integer expected")
        if other <= 0:
            raise ValueError("Value must be larger than 0")
        total = self.getTotalSeconds() * other
        return Duration(seconds=total)

    def __rmul__(self, other):
        if type(other) != type(1):
            raise TypeError("Integer expected")
        if other <= 0:
            raise ValueError("Value must be larger than 0")
        total = self.getTotalSeconds() * other
        return Duration(seconds=total)


if __name__ == '__main__':
    test = Duration(hours=2, minutes=125,seconds=75)
    print(test)
    test2 = test + test
    print(test2)
    test3 = 2 * test
    print(test3)















































































































































