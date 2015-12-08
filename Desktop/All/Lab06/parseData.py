#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-10-06 17:14:16 -0400 (Tue, 06 Oct 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab06/parseData.py $
#      $Revision: 82600 $
#
#########################

import glob
import string
import re


def getData():
    file = "UserData.txt"
    info = []
    allinfo = []
    with open(file,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            #print(line)
            info = []
            Name = re.match(r"(?P<last>[a-zA-Z]*), (?P<first>[a-zA-Z]*)|[a-zA-Z ]*",line)

            if not Name:
                info.append('')
            else:
                if re.findall(r",",Name.group(0)):
                    info.append(Name.group("first") + ' ' + Name.group("last"))
                else:
                    info.append(Name.group(0))

            #Email = re.match(r"(?P<garbage>[a-zA-Z, ]*)",line)
            Email = re.match(Name.group(0) + r"[, ]*(?P<email>[a-zA-Z0-9._-]*@[a-zA-Z0-9._-]*)",line)
            if Email:
                info.append(Email.group("email"))
            else:
                info.append('')


            Number = re.search(r"(?P<area>\d\d\d)(\) |-|)(?P<first>\d\d\d)(-|)(?P<last>\d\d\d\d)",line)
            if Number:
                info.append('(' + Number.group("area") + ') ' + Number.group("first") + '-' + Number.group("last"))
            else:
                info.append('')

            City = re.search(r"[a-zA-Z ]*$",line)

            info.append(City.group(0))
            allinfo.append(info)

    return allinfo


def getInvalidUsers():
    allinfo = getData()
    num = 0
    invalid = []

    for item in allinfo:
        for item2 in item:
            if item2 != '':
                num += 1
        if num == 1:
            invalid.append(item[0])
        num = 0
    invalid.sort()
    return invalid


def getUsersWithEmails():
    allinfo = getData()
    num = 0
    emails = []
    usre = ()

    for item in allinfo:
        if item[1] != '' and item[2] == '' and item[3] == '':
            usre = (item[0], item[1])
            emails.append(usre)
        num = 0
    emails.sort()
    return emails


def getUsersWithPhones():
    allinfo = getData()
    num = 0
    phones = []
    usre = ()

    for item in allinfo:
        if item[1] == '' and item[2] != '' and item[3] == '':
            usre = (item[0], item[2])
            phones.append(usre)
        num = 0
    phones.sort()
    return phones



def getUsersWithStates():
    allinfo = getData()
    num = 0
    states = []
    usre = ()

    for item in allinfo:
        if item[1] == '' and item[2] == '' and item[3] != '':
            usre = (item[0], item[3])
            states.append(usre)
        num = 0
    states.sort()
    return states




def getUsersWithEmailsAndPhones():
    allinfo = getData()
    num = 0
    emailsPhones = []
    usre = ()

    for item in allinfo:
        if item[1] != '' and item[2] != '' and item[3] == '':
            usre = (item[0], item[1], item[2])
            emailsPhones.append(usre)
        num = 0
    emailsPhones.sort()
    return emailsPhones


def getUsersWithEmailsAndStates():
    allinfo = getData()
    num = 0
    emailsStates = []
    usre = ()

    for item in allinfo:
        if item[1] != '' and item[2] == '' and item[3] != '':
            usre = (item[0], item[1], item[3])
            emailsStates.append(usre)
        num = 0
    emailsStates.sort()
    return emailsStates


def getUsersWithPhonesAndStates():
    allinfo = getData()
    num = 0
    phoneStates = []
    usre = ()

    for item in allinfo:
        if item[1] == '' and item[2] != '' and item[3] != '':
            usre = (item[0], item[2], item[3])
            phoneStates.append(usre)
        num = 0
    phoneStates.sort()
    return phoneStates

def getValidUsers():
    allinfo = getData()
    num = 0
    valid = []
    usre = ()

    for item in allinfo:
        if item[1] != '' and item[2] != '' and item[3] != '':
            usre = (item[0], item[1], item[2], item[3])
            valid.append(usre)
        num = 0
    valid.sort()
    return valid




if __name__ == '__main__':

    #test = openFile("bad1.sud")
    #print(test)

    test = getUsersWithEmails()
    print(test)

    # print()
    # print('-----------------------------')
    # print()
