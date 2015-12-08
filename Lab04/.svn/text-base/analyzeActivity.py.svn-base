#!/usr/local/bin/python3.4

import glob
import string
from pprint import pprint as pp

def getUserPermissions():
    file = 'Permissions.txt'
    i = 0
    permissions = {}

    with open(file,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            words = line.split()

            if i > 1:
                if permissions.get(words[0],0) == 0:
                    temp = set()
                    temp.add(words[2])
                    permissions[words[0]] = temp
                else:
                    permissions[words[0]].add(words[2])
            i += 1



    return permissions


def getUserNameFromID():
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



    return names



def getControllerPermissions():
    file = 'Permissions.txt'
    i = 0
    permissions = {}
    namelookup = getUserNameFromID()

    with open(file,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            words = line.split()

            if i > 1:
                if permissions.get(words[2],0) == 0:
                    temp = set()
                    temp.add(namelookup[words[0]])
                    permissions[words[2]] = temp
                else:
                    permissions[words[2]].add(namelookup[words[0]])
            i += 1

    return permissions


def getControllerActions():
    file = 'ActivityLog.txt'

    actions = {}

    with open(file,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            words = line.split()
            words = words[2].split('/')

            if actions.get(words[3],0) == 0:
                temp = set()
                temp.add(words[4])
                actions[words[3]] = temp
            else:
                actions[words[3]].add(words[4])

    return actions


def parseLogFile():
    file = 'ActivityLog.txt'
    user_permissions = getUserPermissions()
    actions = []

    with open(file,'r') as myFile:
        lines = myFile.readlines()
        for line in lines:
            words = line.split()
            words2 = words[2].split('/')

            if words2[3] in user_permissions[words[0]]:
                status = True
            else:
                status = False

            actions.append((words[0],words[2],words2[3],words2[4],status))

    return actions


def canGrantAccess(userID, url):
    split_url = url.split('/')
    controller = split_url[3]
    user_permissions = getUserPermissions()

    if user_permissions.get(userID,0) == 0:
        return False
    elif controller in user_permissions[userID]:
            return True
    else:
        return False



def checkUserActivity(userID):
    log_file = parseLogFile()
    accessed_urls = []

    for item in log_file:
        if item[0] == userID:
            accessed_urls.append((item[1],item[4]))
    return accessed_urls


def getActivityByUser():
    full_activity = {}
    final_activity = {}
    log_file = parseLogFile()
    name_lookup = getUserNameFromID()


    for item in log_file:
        name = name_lookup[item[0]]
        if full_activity.get(name,0) == 0:

            if item[4] == True:
                full_activity[name] = [1,0]
            else:
                full_activity[name] = [0,1]
        else:
            if item[4] == True:
                full_activity[name][0] += 1
            else:
                full_activity[name][1] += 1

        for item in full_activity:
            temp = []
            final_activity[item] = (full_activity[item][0],full_activity[item][1])

    return final_activity




def getActivityByController():
    full_activity = {}
    final_activity = {}
    log_file = parseLogFile()


    for item in log_file:
        name = item[2]
        if full_activity.get(name,0) == 0:

            if item[4] == True:
                full_activity[name] = [1,0]
            else:
                full_activity[name] = [0,1]
        else:
            if item[4] == True:
                full_activity[name][0] += 1
            else:
                full_activity[name][1] += 1

        for item in full_activity:
            temp = []
            final_activity[item] = (full_activity[item][0],full_activity[item][1])

    return final_activity





if __name__ == '__main__':

    test = getUserPermissions()
    print(test)



    test = getControllerPermissions()
    print(test)


    test = getControllerActions()
    print(test)


    test = parseLogFile()
    print(test)


    test = canGrantAccess('bhall', 'http://www.purdue.com/Forums/Page2')
    print(test)


    test = checkUserActivity('bhall')
    print(test)


    test = getActivityByUser()
    print(test)


    test = getActivityByController()
    print(test)

    # print()
    # print('-----------------------------')
    # print()

