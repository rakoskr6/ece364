#!/usr/local/bin/python3.4

def addNumbers(num):
    Sum = 0
    while (num >0):
        Sum = Sum + num
        num = num - 1
    return Sum

def addMultiplesOf(num):
    Sum = 0
    OrigNum = num
    while (num <= 1000):
        Sum = num + Sum
        num = num + OrigNum
    return Sum

def getNumberFrequency(num):
    pistring = 'The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1'
    pistring = pistring.replace(" ","")

    frequency = pistring.count(str(num))

    return frequency

def getDigitalSum(num):
    array = list(str(num))
    sum = 0
    for number in array:
        sum += int(number)
    return sum


def getSequenceWithoutDigit(num):
    strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982",

"943020914707361894793269276244518656023955905370512897816345542332011497599489",

"627842432748378803270141867695262118097500640514975588965029300486760520801049",

"153788541390942453169171998762894127722112946456829486028149318156024967788794",

"981377721622935943781100444806079767242927624951078415344642915084276452000204",

"276947069804177583220909702029165734725158290463091035903784297757265172087724",

"474095226716630600546971638794317119687348468873818665675127929857501636341131"]
    fullstring = "".join(strList)
    newlist=fullstring.split(str(num))
    finalstring = max(newlist,key=len)
    return finalstring

def capitalizeMe(string):
    list = string.split()
    newlist = []
    for eachstring in list:
        newlist.append(eachstring[:-1].capitalize()+eachstring[-1].upper())
    newlist = " ".join(newlist)
    return newlist




if __name__ == '__main__':
    test = addNumbers(100)
    print('addNumbers: {}'.format(test))
    test = addMultiplesOf(1)
    print('addMultiples: {}'.format(test))
    test = getNumberFrequency(141592)
    print('getNumberFrequency: {}'.format(test))
    test = getDigitalSum(12345)
    print('getDigitalSum: {}'.format(test))
    test = getSequenceWithoutDigit(12)
    print('getSequenceWithoutDigit: {}'.format(test))
    test = capitalizeMe('lorem ipsum dolor a sit amet eu')
    print('capitilizeMe: {}'.format(test))