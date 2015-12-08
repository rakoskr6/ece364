import os
import unittest
from PySide.QtTest import *
from PySide.QtCore import *
from EntryApplication import *

singletonApplication = None
singletonForm = None

class EntryApplicationTestSuite(unittest.TestCase):

    def setUp(self):
        """
        Creates the QApplication singleton instance, if not present.
        """
        global singletonApplication, singletonForm

        if singletonApplication is None:
            singletonApplication = QApplication(sys.argv)
            singletonForm = EntryApplication()

        self.app = singletonApplication
        self.form = singletonForm

        # Define a list of text widgets to refer to them all when need.
        self.textWidgets = [self.form.txtFirstName, self.form.txtLastName, self.form.txtAddress,
                            self.form.txtCity, self.form.txtState, self.form.txtZip, self.form.txtEmail]

    def tearDown(self):
        """
        Remove the running application from the self instance.
        """
        del self.app
        del self.form

        # Clean up the file.
        if os.path.exists("target.xml"):
            os.remove("target.xml")

    def test_ClearForm(self):

        formCleared = True

        # Populate all entries.
        QTest.keyClicks(self.form.txtFirstName, "Sherlock")
        QTest.keyClicks(self.form.txtLastName, "Holmes")
        QTest.keyClicks(self.form.txtAddress, "1223 End St.")
        QTest.keyClicks(self.form.txtCity, "West Lafayette")
        QTest.keyClicks(self.form.txtState, "IN")
        QTest.keyClicks(self.form.txtZip, "47906")

        # Click the button.
        QTest.mouseClick(self.form.btnClear, Qt.LeftButton)

        # Read the form.
        for widget in self.textWidgets:
            formCleared &= widget.text() == ""

        formCleared &= self.form.lblError.text() == ""
        formCleared &= self.form.btnLoad.isEnabled()
        formCleared &= not self.form.btnSave.isEnabled()

        self.assertEqual(formCleared, True)

    def test_LoadValidData(self):

        dataCorrect = True

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_1.xml")

        # Check values.
        dataCorrect &= self.form.txtFirstName.text() == "George"
        dataCorrect &= self.form.txtLastName.text() == "Clooney"
        dataCorrect &= self.form.txtAddress.text() == "414 Second St."
        dataCorrect &= self.form.txtCity.text() == "Some City"
        dataCorrect &= self.form.txtState.text() == "CA"
        dataCorrect &= self.form.txtZip.text() == "10001"
        dataCorrect &= self.form.txtEmail.text() == "clooney@nowhere.com"

        # Check the buttons.
        dataCorrect &= self.form.lblError.text() == ""
        dataCorrect &= self.form.btnSave.isEnabled()
        dataCorrect &= not self.form.btnLoad.isEnabled()

        self.assertEqual(dataCorrect, True)

    def test_SaveValidDataDirect(self):

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_1.xml")

        # Save without modification.
        QTest.mouseClick(self.form.btnSave, Qt.LeftButton)

        with open("test_case_1.xml", "r") as xml:
            source = xml.read()

        with open("target.xml", "r") as xml:
            target = xml.read()

        self.assertEqual(source, target)


    def test_SaveValidDataModified(self):

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_1.xml")

        self.form.txtFirstName.clear()
        QTest.keyClicks(self.form.txtFirstName, "Amal")

        self.form.txtLastName.clear()
        QTest.keyClicks(self.form.txtLastName, "Alamuddin")

        self.form.txtAddress.clear()
        QTest.keyClicks(self.form.txtAddress, "909 Second St.")

        self.form.txtCity.clear()
        QTest.keyClicks(self.form.txtCity, "Irvine")

        self.form.txtState.clear()
        QTest.keyClicks(self.form.txtState, "TX")

        self.form.txtZip.clear()
        QTest.keyClicks(self.form.txtZip, "56489")

        self.form.txtEmail.clear()
        QTest.keyClicks(self.form.txtEmail, "amal@hereAndThere.com")

        QTest.mouseClick(self.form.btnSave, Qt.LeftButton)

        with open("test_case_1_Mod.xml", "r") as xml:
            source = xml.read()

        with open("target.xml", "r") as xml:
            target = xml.read()

        self.assertEqual(source, target)

    def test_SaveWithEmptyEntries(self):

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_2.xml")

        # Save without modification.
        QTest.mouseClick(self.form.btnSave, Qt.LeftButton)

        errorShown = self.form.lblError.text() != ""
        fileSaved = os.path.exists("target.xml")
        print(errorShown)
        print(fileSaved)
        self.assertEqual(errorShown and not fileSaved, True)

    def test_SaveWithEmptyEntriesPartialFixed(self):

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_2.xml")

        QTest.keyClicks(self.form.txtLastName, "Jackson")

        # Try to save.
        QTest.mouseClick(self.form.btnSave, Qt.LeftButton)

        errorShown = self.form.lblError.text() != ""
        fileSaved = os.path.exists("target.xml")

        self.assertEqual(errorShown and not fileSaved, True)

    def test_SaveWithEmptyEntriesFixed(self):

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_2.xml")

        QTest.keyClicks(self.form.txtLastName, "Jackson")
        QTest.keyClicks(self.form.txtCity, "Los Angeles")

        # Try to save.
        QTest.mouseClick(self.form.btnSave, Qt.LeftButton)

        errorShown = self.form.lblError.text() == ""

        with open("test_case_2_Mod.xml", "r") as xml:
            source = xml.read()

        with open("target.xml", "r") as xml:
            target = xml.read()

        self.assertTrue(errorShown)
        self.assertEqual(source, target)

    def test_SaveWithInvalidEntriesStateFixed(self):

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_3.xml")

        self.form.txtState.clear()
        QTest.keyClicks(self.form.txtState, "NY")

        # Try to save.
        QTest.mouseClick(self.form.btnSave, Qt.LeftButton)

        errorShown = self.form.lblError.text() != ""
        fileSaved = os.path.exists("target.xml")

        self.assertEqual(errorShown and not fileSaved, True)

    def test_SaveWithInvalidEntriesStateAndZipFixed(self):

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_3.xml")

        self.form.txtState.clear()
        QTest.keyClicks(self.form.txtState, "NY")

        self.form.txtZip.clear()
        QTest.keyClicks(self.form.txtState, "20201")

        # Try to save.
        QTest.mouseClick(self.form.btnSave, Qt.LeftButton)

        errorShown = self.form.lblError.text() != ""
        fileSaved = os.path.exists("target.xml")

        self.assertEqual(errorShown and not fileSaved, True)

    def test_SaveWithInvalidEntriesAllFixed(self):

        # Load the xml file.
        self.form.loadFromXmlFile("test_case_3.xml")

        self.form.txtState.clear()
        QTest.keyClicks(self.form.txtState, "NY")

        self.form.txtZip.clear()
        QTest.keyClicks(self.form.txtZip, "20201")

        self.form.txtEmail.clear()
        QTest.keyClicks(self.form.txtEmail, "someone@famous.com")

        # Try to save.
        QTest.mouseClick(self.form.btnSave, Qt.LeftButton)

        errorShown = self.form.lblError.text() == ""

        with open("test_case_3_Mod.xml", "r") as xml:
            source = xml.read()

        with open("target.xml", "r") as xml:
            target = xml.read()

        self.assertTrue(errorShown)
        self.assertEqual(source, target)

if __name__ == '__main__':
    unittest.main()
