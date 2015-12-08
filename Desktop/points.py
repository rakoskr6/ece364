#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-18 16:41:51 -0400 (Sun, 18 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab07/points.py $
#      $Revision: 82709 $
#
#########################

import glob
import string
import re
import copy
from pprint import pprint as pp

class PointND:
    def __init__(self, *args):

        for item in args:
            if type(item) != type(1.0):
                raise ValueError("Cannot instantiate an object with non-float values.")
        self.t = args
        self.n = len(args)


    def __str__(self):
        output = '('
        i = 1
        for item in self.t:
            output += "{0:.2f}".format(item)
            if i < self.n:
                output += ', '
            i += 1

        output += ')'
        return output

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        sum = 0
        i = 0

        if other.n != self.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")

        for item in other.t:
            sum += (self.t[i] - item)**2
            i += 1
        return sum**.5

    def distanceFromOrigin(self):
        sum = 0
        i = 0

        for item in self.t:
            sum += (item)**2
            i += 1
        return sum**.5


    def nearestPoint(self,points):
        min = 9999999999999
        if points == '' or len(points) == 0:
            raise ValueError("Input cannot be empty.")

        for item in points:
            dist = self.distanceFrom(item)
            if dist < min:
                min = dist
                point = item
        return point

    def clone(self):
        return copy.copy(self)

    def __add__(self,other):
        temp = []
        i = 0

        if isinstance(other,self.__class__):
            for item in other.t:
                temp.append(item + self.t[i])
                i += 1

            result = PointND(*temp)
        else:
            for item in self.t:
                temp.append(other + item)

            result = PointND(*temp)

        return result

    def __radd__(self,other):
        temp = []
        i = 0

        if isinstance(other,self.__class__):
            for item in other.t:
                temp.append(item + self.t[i])
                i += 1

            result = PointND(*temp)
        else:
            for item in self.t:
                temp.append(other + item)

            result = PointND(*temp)

        return result


    def __sub__(self,other):
        temp = []

        i = 0

        if type(other) == type(self):

            for item in other.t:
                temp.append(self.t[i] - item)
                i += 1

            result = PointND(*temp)
        else:
            for item in self.t:
                temp.append(item - other)

            result = PointND(*temp)

        return result


    def __mul__(self,other):
        temp = []

        i = 0

        if type(other) == type(self):

            for item in other.t:
                temp.append(self.t[i] * item)
                i += 1

            result = PointND(*temp)
        else:
            for item in self.t:
                temp.append(item * other)

            result = PointND(*temp)

        return result

    def __rmul__(self,other):
        temp = []

        i = 0

        if type(other) == type(self):

            for item in other.t:
                temp.append(self.t[i] * item)
                i += 1

            result = PointND(*temp)
        else:
            for item in self.t:
                temp.append(item * other)

            result = PointND(*temp)

        return result


    def __truediv__(self,other):
        temp = []

        i = 0

        if type(other) == type(self):

            for item in other.t:
                temp.append(self.t[i] / item)
                i += 1

            result = PointND(*temp)
        else:
            for item in self.t:
                temp.append(item / other)

            result = PointND(*temp)

        return result

    def __neg__(self):
        temp = []
        for item in self.t:
            temp.append(-item)
        result = PointND(*temp)
        return result

    def __getitem__(self,k):
        return self.t[k]


    def __lt__(self,other):
        lvalue = self.distanceFromOrigin()
        rvalue = other.distanceFromOrigin()
        return lvalue < rvalue

    def __gt__(self,other):
        lvalue = self.distanceFromOrigin()
        rvalue = other.distanceFromOrigin()
        return lvalue > rvalue

    def __ge__(self,other):
        lvalue = self.distanceFromOrigin()
        rvalue = other.distanceFromOrigin()
        return lvalue >= rvalue

    def __le__(self,other):
        lvalue = self.distanceFromOrigin()
        rvalue = other.distanceFromOrigin()
        return lvalue <= rvalue

    def __eq__(self,other):
        i = 0

        for item in self.t:
            if item != other.t[i]:
                return False
            i += 1
        return True

    def __ne__(self,other):
        return not self == other



if __name__ == '__main__':

    test = PointND(1.000,2.0,3.0)
    test2 = PointND(2.0,3.0,4.0)


    print(test>test2)
    print(test2>test)




















































































































































