#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-11-10 17:15:41 -0500 (Tue, 10 Nov 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab10/EntryApplication.py $
#      $Revision: 83331 $
#
#########################


import sys
import re
from PySide.QtGui import *

from EntryForm import *

class EntryApplication(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)
        self.btnClear.clicked.connect(self.clear)
        self.btnSave.clicked.connect(self.validate)
        self.btnLoad.clicked.connect(self.loadData)

        self.txtAddress.textChanged.connect(self.dataEntered)
        self.txtLastName.textChanged.connect(self.dataEntered)
        self.txtFirstName.textChanged.connect(self.dataEntered)
        self.txtZip.textChanged.connect(self.dataEntered)
        self.txtEmail.textChanged.connect(self.dataEntered)
        self.txtState.textChanged.connect(self.dataEntered)
        self.txtCity.textChanged.connect(self.dataEntered)


    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """
        with open(filePath,'r') as myFile:
            lines = myFile.readlines()

            #i = 1
            for line in lines:
                #if i > 2 and i < 9:

                line = line.strip()
                Match = re.search(r"<FirstName>([\w]+)</FirstName>",line)
                if Match:
                    self.txtFirstName.setText(Match.group(1))

                Match = re.search(r"<LastName>([\w]+)</LastName>",line)
                if Match:
                    self.txtLastName.setText(Match.group(1))

                Match = re.search(r"<Address>([\w\d .]+)</Address>",line)
                if Match:
                    self.txtAddress.setText(Match.group(1))

                Match = re.search(r"<City>([\w\d .]+)</City>",line)
                if Match:
                    self.txtCity.setText(Match.group(1))

                Match = re.search(r"<State>([\w]+)</State>",line)
                if Match:
                    self.txtState.setText(Match.group(1))

                Match = re.search(r"<ZIP>([\d]+)</ZIP>",line)
                if Match:
                    self.txtZip.setText(Match.group(1))

                Match = re.search(r"<Email>([\w\d.-@]+)</Email>",line)
                if Match:
                    self.txtEmail.setText(Match.group(1))

                #i += 1

        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)

        #pass

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadFromXmlFile(filePath)


    def clear(self):
        self.txtAddress.clear()
        self.txtCity.clear()
        self.txtEmail.clear()
        self.txtFirstName.clear()
        self.txtLastName.clear()
        self.txtState.clear()
        self.txtZip.clear()
        self.btnLoad.setEnabled(True)
        self.btnSave.setEnabled(False)
        self.lblError.setText("")

    def dataEntered(self):
        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)

    def validate(self):
        first = self.txtFirstName.text()
        last = self.txtLastName.text()
        address = self.txtAddress.text()
        city = self.txtCity.text()
        state = self.txtState.text()
        zip = self.txtZip.text()
        email = self.txtEmail.text()

        self.lblError.setText("")
        errorState = False

        all = [first,last,address,city,state,zip,email]
        for item in all:
            if item == '':
                self.lblError.setText("Error: Must fill in all fields")

                errorState = True
        if state not in self.states:
            self.lblError.setText("Error: Must enter valid state")
            errorState = True

        if not re.match(r"[0-9][0-9][0-9][0-9][0-9]",zip) or len(zip) != 5:
            self.lblError.setText("Error: Must enter valid ZIP Code")
            errorState = True
        if not re.match(r"\w+@\w+\.\w+",email):
            self.lblError.setText("Error: Email is not valid!")
            errorState = True

        if not errorState:
            line = '<?xml version="1.0" encoding="UTF-8"?>\n'
            line += "<user>\n"
            line += "\t<FirstName>"
            line += first
            line += "</FirstName>\n"

            line += "\t<LastName>"
            line += last
            line += "</LastName>\n"

            line += "\t<Address>"
            line += address
            line += "</Address>\n"

            line += "\t<City>"
            line += city
            line += "</City>\n"

            line += "\t<State>"
            line += state
            line += "</State>\n"

            line += "\t<ZIP>"
            line += zip
            line += "</ZIP>\n"

            line += "\t<Email>"
            line += email
            line += "</Email>\n"

            line += "</user>\n"

            with open("target.xml",'w') as myFile:
                myFile.writelines(line)
                #print(line)
            self.clear()





if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()
