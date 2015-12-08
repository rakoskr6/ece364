#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-09-15 17:07:17 -0400 (Tue, 15 Sep 2015) $     
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab03/myOperations.py $  
#      $Revision: 81904 $   
#                 
#########################

def checkTypes(l):
    all_types = [0,0,0]
    if type(l) != type([]):
        return None
    elif len(l) == 0:
        return None
    else:
        for item in l:
            if type(item) == type(1):
                all_types[0] += 1
            elif type(item) == type(1.1):
                all_types[1] += 1
            elif type(item) == type('string'):
                all_types[2] += 1
            else:
                return None
        return all_types

def normalizeVector(vector):
    if type(vector) != type([]):
        return None
    elif len(vector) == 0:
        return None
    else:
        total = 0
        i = 0
        for item in vector:
            total += item
        for item in vector:
            vector[i] = item / total
            i += 1
        return vector

def findMedian(vList):
    if type(vList) != type([]):
        return None
    elif len(vList) == 0:
        return None
    else:
        for item in vList:
            if type(item) != type(1) and type(item) != type(1.0):
                print(item)
                return None
        vList.sort()
        length = len(vList)
        if length %2 == 0:
            return (vList[int(length/2)] + vList[int(length/2 - 1)]) / 2
        else: #odd

            return vList[int(length/2-.5)]

    return vList



def rectifySignal(signal):
    if type(signal) != type([]):
        return None
    elif len(signal) == 0:
        return None
    else:
        i = 0
        for item in signal:
            if item < 0:
                signal[i] = 0
            i += 1
        return signal

def convertToBoolean(num):
    if type(num) != type(1):
        return None
    elif num >= 255 or num < 0:
        return None
    else:
        array = list(str(bin(num)))
        i = 0
        tfarray = []
        for item in array:
            if i >= 2:
                if item == '1':
                    tfarray.append(True)
                else:
                    tfarray.append(False)
            i += 1
        return tfarray

def convertToInteger(boolList):
    if type(boolList) != type([]):
        return None
    elif len(boolList) == 0:
        return None
    else:
        for item in boolList:
            if item != True and item != False or (type(item) == type(1) or type(item) == type(1.0)):
                return None
        length = len(boolList)
        total = 0
        for item in boolList:
            length -= 1
            if item == True:
                total += pow(2,length)
        return total

def switchNames(nameList):
    if type(nameList) != type([]):
        return None
    elif len(nameList) == 0:
        return None
    else:
        i = 0
        name = []
        for item in nameList:
            name = " ".join(item.split(',')).split()
            nameList[i] = name[1] + ' ' + name[0]
            i += 1
        return nameList


def getWeightAverage(data):
    if type(data) != type([]):
        return None
    elif len(data) == 0:
        return None
    else:
        Sum = 0
        for item in data:
            item = item.split()
            Sum += float(item[2])
        return Sum / len(data)



if __name__ == '__main__':
    test = checkTypes([3.14, -11.9, "Today", 121, "Tomorrow", 2.71])
    print(test)
    test = normalizeVector([0,1,2,3,4])
    print(test)
    test = findMedian([1,2,3,4])
    print(test)
    test = rectifySignal([1.0, .81, .31, -.31, -.81, -1.0, .81])
    print(test)
    test = convertToBoolean(135)
    print(test)
    test = convertToInteger([True, False])
    print(test)
    test = switchNames(['Jackson, Michael M', 'Trump, Donald', 'Bush, George W'])
    print(test)
    test = getWeightAverage(["Michael Jackson: 195.5 lb", "Donald Trump: 211.7 lb", "George Bush: 207.3 lb", "Sherlock Holmes: 221.9 lb"])
    print(test)