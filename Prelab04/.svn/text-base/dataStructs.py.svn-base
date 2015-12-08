#!/usr/local/bin/python3.4

import glob
import string
from pprint import pprint as pp

def getWordFrequency():
    files = glob.glob('files/*')

    freq = {}
    for file in files:
        with open(file,'r') as myFile:
            lines = myFile.readline()
            words = lines.split()
            for i in range(len(words)):
                for character in string.punctuation:
                    words[i] = words[i].replace(character,"")

            for word in words:
                if freq.get(word,0) == 0:
                    freq[word] = 1
                else:
                    freq[word] += 1

    return freq


def getWordFrequencyFile(file_open):
    files = [file_open]

    freq = {}
    for file in files:
        with open(file,'r') as myFile:
            lines = myFile.readline()
            words = lines.split()
            for i in range(len(words)):
                for character in string.punctuation:
                    words[i] = words[i].replace(character,"")

            for word in words:
                if freq.get(word,0) == 0:
                    freq[word] = 1
                else:
                    freq[word] += 1

    return freq



def getDuplicates():
    files = glob.glob('files/*')
    file_content = set()
    file_match = {}
    duplicate = {}

    for file in files:
        with open(file,'r') as myFile:
            content = myFile.readline()

            if content in file_content:
                file_match[content].append(file)
            else:
                file_content.add(content)
                file_match[content] = [file]

    for item in file_content:
        equivalent = file_match[item]
        equivalent = sorted(equivalent)

        unique_words = len(getWordFrequencyFile(equivalent[0]))

        i = 0
        for item2 in equivalent:
            equivalent[i] = item2[6:-4]
            i += 1



        if len(equivalent) > 1:
            duplicate[equivalent[0]] = (unique_words,equivalent)
    return duplicate




def getPurchaseReport():
    files = glob.glob('purchases/*')
    itemlist = []
    prices = {}
    purchases = []
    costs = []
    costsdict = {}
    x = 0


    for file in files:
        if file == 'purchases/Item List.txt':
            with open(file,'r') as myFile:
                lines = myFile.readlines()
            for line in lines:
                itemlist.append(line.split())

            i = 0
            for item in itemlist:

                if i > 1:
                    itemlist[i] = [item[0],item[1].replace('$','')] #possibly not needed
                    prices[item[0]] = item[1].replace('$','')

                i += 1
        else:
            purchases = []
            with open(file,'r') as myFile:
                lines = myFile.readlines()
            for line in lines:
                purchases.append(line.split())

            cost = 0.0
            i = 0
            for purchase in purchases:
                if i > 1:
                    #cost = 999
                    cost += float(purchase[1]) * float(prices[purchase[0]])

                i += 1


            costs.append([x,cost])
            cost = int(100 * cost) / 100
            costsdict[x] = cost
            x += 1

    return costsdict




def getTotalSold():
    files = glob.glob('purchases/*')
    itemlist = []
    prices = {}
    x = 0


    for file in files:
        if file == 'purchases/Item List.txt':
            with open(file,'r') as myFile:
                lines = myFile.readlines()
            for line in lines:
                itemlist.append(line.split())

            i = 0
            for item in itemlist:

                if i > 1:
                    itemlist[i] = [item[0],item[1].replace('$','')] #possibly not needed
                    prices[item[0]] = item[1].replace('$','')

                i += 1
            itemcount = prices

            for item in itemcount:
                itemcount[item] = 0
        else:
            purchases = []
            with open(file,'r') as myFile:
                lines = myFile.readlines()
            for line in lines:
                purchases.append(line.split())


            i = 0
            for purchase in purchases:
                if i > 1:
                    itemcount[purchase[0]] += int(purchase[1])

                i += 1






    return itemcount


if __name__ == '__main__':

    test = getWordFrequency()
    print(test)
    print()
    print('-----------------------------')
    print()

    test = getDuplicates()
    print(test)
    # print()
    # print('-----------------------------')
    # print()
    #
    # test = getPurchaseReport()
    # print(test)
    # print()
    # print('-----------------------------')
    # print()
    #
    # test = getTotalSold()
    # print(test)
