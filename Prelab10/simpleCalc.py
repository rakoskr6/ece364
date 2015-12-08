#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-11-09 17:10:32 -0500 (Mon, 09 Nov 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Prelab10/simpleCalc.py $
#      $Revision: 83211 $
#
#########################

import glob
import string
import re
import copy
import math
from pprint import pprint as pp
# Import PySide classes
from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *


class ConsumerApp(QMainWindow, Ui_Dialog):

    def __init__(self, parent=None):

        super(ConsumerApp, self).__init__(parent)
        self.setupUi(self)


        self.pushButton_0.clicked.connect(self.click0)
        self.pushButton_1.clicked.connect(self.click1)
        self.pushButton_2.clicked.connect(self.click2)
        self.pushButton_3.clicked.connect(self.click3)
        self.pushButton_4.clicked.connect(self.click4)
        self.pushButton_5.clicked.connect(self.click5)
        self.pushButton_6.clicked.connect(self.click6)
        self.pushButton_7.clicked.connect(self.click7)
        self.pushButton_8.clicked.connect(self.click8)
        self.pushButton_9.clicked.connect(self.click9)
        self.pushButton_period.clicked.connect(self.clickPer)

        self.pushButton_add.clicked.connect(self.clickAdd)
        self.pushButton_mul.clicked.connect(self.clickMul)
        self.pushButton_min.clicked.connect(self.clickSub)
        self.pushButton_div.clicked.connect(self.clickDiv)

        self.pushButton_equal.clicked.connect(self.clickEquals)
        self.pushButton_clear.clicked.connect(self.clickClear)
        self.pushButton_clear.clicked.connect(self.outputValue)

        self.checkBox.stateChanged.connect(self.outputValue)
        self.spinBox.valueChanged.connect(self.outputValue)



        self.display = ''
        self.value1txt = ''
        self.value2txt = ''
        self.operator = ''
        self.value1 = 0
        self.value2 = 0
        self.itemNum = 1
        self.previous = 1
        self.result = 0.0

        self.valuetxt = ''
        self.nextOperator = ''



    def click0(self):
        self.newInput('0')

    def click1(self):
        self.newInput('1')

    def click2(self):
        self.newInput('2')

    def click3(self):
        self.newInput('3')

    def click4(self):
        self.newInput('4')

    def click5(self):
        self.newInput('5')

    def click6(self):
        self.newInput('6')

    def click7(self):
        self.newInput('7')

    def click8(self):
        self.newInput('8')

    def click9(self):
        self.newInput('9')

    def clickPer(self):
        self.newInput('.')

    def clickAdd(self):
        self.newInput('+')
    def clickSub(self):
        self.newInput('-')
    def clickMul(self):
        self.newInput('*')
    def clickDiv(self):
        self.newInput('/')

    def clickEquals(self):
        self.newInput('=')
    def clickClear(self):
        self.newInput('C')


    def newInput(self,item):
        if item == 'C':
            self.display = ''
            self.valuetxt = ''
            self.nextOperator = ''
            self.result = 0.0

        elif item in '+-*/':
            self.computeValue(item)
            self.display = str(self.result)

        elif item == '=':
            self.computeValue('')
            self.display = str(self.result)

        else:
            self.valuetxt += item
            self.display = self.valuetxt


        self.outputValue()
        #print("valuetxt=" + self.valuetxt + " result=" + str(self.result) + " next operator=" + self.nextOperator)



    def computeValue(self,item):
        if self.valuetxt != '':
            if self.nextOperator == '':
                self.result = float(self.valuetxt)
            elif self.nextOperator == '+':
                self.result = float(self.valuetxt) + self.result
            elif self.nextOperator == '-':
                self.result = self.result - float(self.valuetxt)
            elif self.nextOperator == '*':
                self.result = float(self.valuetxt) * self.result
            elif self.nextOperator == '/':
                self.result = self.result / float(self.valuetxt)

        self.nextOperator = item
        self.valuetxt = ''





    def outputValue(self):
        value = self.spinBox.value()
        if value > 5:
            self.spinBox.setValue(5)
            value = 5
        commas = self.checkBox.checkState()
        disp = ''

        #print(value)
        if commas:
            if self.display != '':
                if '.' not in self.display:
                    i = len(str(self.display))
                    for char in str(self.display):
                        if i % 3 == 0:
                            disp += ','
                        disp += char
                        i -= 1
                    if disp[0] == ',':
                        disp = disp[1:]
                    if len(disp) > 15:
                        disp = disp[0:15] + '---'
                else:
                    disp2 = self.display.split('.')
                    i = len(str(disp2[0]))
                    for char in disp2[0]:
                        if i % 3 == 0:
                            disp += ','
                        disp += char
                        i -= 1
                    disp += '.'
                    disp += disp2[1]
                    if disp[0] == ',':
                        disp = disp[1:]
                    if len(disp) > 15:
                        disp = disp[0:15] + '---'

        else:
            disp = self.display
            if len(disp) > 12:
                disp = disp[0:12] + '---'

        if '.' in disp:
            disp2 = disp.split('.')

            if value == 0:
                disp = disp2[0]
            else:
                disp = disp2[0] + '.' + disp2[1][0:value]


        self.textBrowser.clear()
        self.textBrowser.append(disp)








if __name__ == "__main__":
    currentApp = QApplication([])
    currentForm = ConsumerApp()

    currentForm.show()
    currentApp.exec_()

















































































































































