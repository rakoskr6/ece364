import sys
import unittest

try:
    from regExPractical import *
except ImportError:
    print("Unable to import 'regExPractical'. Create an Empty Python file with that name.")

try:
    from timeDuration import *
except ImportError:
    print("Unable to import 'timeDuration'. Create an Empty Python file with that name.")

try:
    from timeManager import *
except ImportError:
    print("Unable to import 'timeManager'. Create an Empty Python file with that name.")


class PracticalTestCases(unittest.TestCase):

    def test_validityChecks(self):

        with self.subTest(key="Use of Split()"):
            with open("regExPractical.py", "r") as pyFile:
                sourceCode = pyFile.read()

            self.assertFalse(".split(" in sourceCode)

        with self.subTest(key="Python Version"):
            currentVersion = sys.version_info
            self.assertGreaterEqual(currentVersion, (3, 4))

    def test_regEx_getAttributes(self):

        with self.subTest(key="XML 1"):

            xml = '<person   name="Irene Adler" gender="female"  age="35" />'
            expectedValue = [("age", "35"), ("gender", "female"), ("name", "Irene Adler")]
            actualValue = getAttributes(xml)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="XML 2"):

            xml = '<student course="Software Engineering Tools" major="Computer Engineering" gpa="3.5" />'
            expectedValue = [("course", "Software Engineering Tools"), ("gpa", "3.5"), ("major", "Computer Engineering")]
            actualValue = getAttributes(xml)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="XML 3"):

            xml = '<book   author="Peter O\'Toole" title="End of Times"  price="$19.99" />'
            expectedValue = [("author", "Peter O'Toole"), ("price", "$19.99"), ("title", "End of Times")]
            actualValue = getAttributes(xml)

            self.assertEqual(expectedValue, actualValue)

    def test_regEx_getAddressParts(self):

        with self.subTest(key="Valid Address 1"):

            url = "https://www.paypal.com/Customer1Area/Pay2"
            expectedValue = "www.paypal.com", "Customer1Area", "Pay2"
            actualValue = getAddressParts(url)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Valid Address 2"):

            url = "http://www3.google.com.cn/search/music"
            expectedValue = "www3.google.com.cn", "search", "music"
            actualValue = getAddressParts(url)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Underscore in Controller"):

            url = "http://www.purdue.edu/About_Us/History"
            actualValue = getAddressParts(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="Less Parts"):

            url = "https://purdue.syncplicity.com/AboutUs"
            actualValue = getAddressParts(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="More Parts"):

            url = "http://www.yahoo.com/AboutUs/Vision/Leadership"
            actualValue = getAddressParts(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="Wrong Protocol"):

            url = "ftp://files.microsoft.com/Download/New"
            actualValue = getAddressParts(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="Dot in Controller"):

            url = "http://www.cnn.com/First.New/Articles"
            actualValue = getAddressParts(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="Dot in Action"):

            url = "http://www.cnn.com/News/On.Tuesday"
            actualValue = getAddressParts(url)

            self.assertIsNone(actualValue)

    def test_regEx_getOptions(self):

        with self.subTest(key="Group 1"):

            commandline = "myScript.bash -v  -i 2   -p  /local/bin/somefolder"
            expectedValue = [("i", "2"), ("p", "/local/bin/somefolder")]
            actualValue = getOptions(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 2"):

            commandline = "program.py -k -D 44 -j full  -t  allArea"
            expectedValue = [("j", "full"), ("t", "allArea")]
            actualValue = getOptions(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 3"):

            commandline = "checkMap.pl  -g gcc5  -K optimize -f skip -c include:new.c -w -a"
            expectedValue = [("c", "include:new.c"), ("f", "skip"), ("g", "gcc5")]
            actualValue = getOptions(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 4"):

            commandline = "tryCode.sh -X repeat  u 3.1  -h local/bin/python3.5  -s -a -z combine"
            expectedValue = [("h", "local/bin/python3.5"), ("z", "combine")]
            actualValue = getOptions(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 5"):

            commandline = "run.exe -a -b -d -g -w OK"
            expectedValue = [("w", "OK")]
            actualValue = getOptions(commandline)

            self.assertEqual(expectedValue, actualValue)

    def test_regEx_getNumber(self):

        with self.subTest(key="Good Number 1"):

            s = "The Avogadro constant, 6.022140857e+23, is the number of constituent particles in one mole."
            expectedValue = "6.022140857e+23"
            actualValue = getNumber(s)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Number 2"):

            s = "The mass of the proton equals 1.6726219E-27kg."
            expectedValue = "1.6726219E-27"
            actualValue = getNumber(s)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Number 3"):

            s = "The charge of the electron, +1.60217662e-19 coulombs, is a very small number."
            expectedValue = "+1.60217662e-19"
            actualValue = getNumber(s)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Bad Number 1"):

            s = "A sample number to test is 23e-1 for match verification."
            actualValue = getNumber(s)

            self.assertIsNone(actualValue)

        with self.subTest(key="Bad Number 2"):

            s = "The number 43.234 is not written in proper notation."
            actualValue = getNumber(s)

            self.assertIsNone(actualValue)

    def test_modules_getTotalDuration(self):

        with self.subTest(key="Experiment13"):

            ex = "Experiment13"
            totalDuration = getTotalDuration(ex)

            expectedValue = 23, 41, 25
            actualValue = totalDuration.hours, totalDuration.minutes, totalDuration.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Experiment09"):

            ex = "Experiment09"
            totalDuration = getTotalDuration(ex)

            expectedValue = 26, 50, 42
            actualValue = totalDuration.hours, totalDuration.minutes, totalDuration.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Experiment07"):

            ex = "Experiment07"
            totalDuration = getTotalDuration(ex)

            expectedValue = 23, 19, 4
            actualValue = totalDuration.hours, totalDuration.minutes, totalDuration.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Experiment17"):

            ex = "Experiment17"
            totalDuration = getTotalDuration(ex)

            expectedValue = 24, 45, 2
            actualValue = totalDuration.hours, totalDuration.minutes, totalDuration.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Experiment00"):

            ex = "Experiment00"
            totalDuration = getTotalDuration(ex)

            expectedValue = 25, 12, 50
            actualValue = totalDuration.hours, totalDuration.minutes, totalDuration.seconds

            self.assertEqual(expectedValue, actualValue)

    def test_modules_rankExperiments(self):

        with self.subTest(key="14"):

            expectedValue = ["Experiment14"]
            actualValue = rankExperiments("Experiment14")

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="07, 13"):

            expectedValue = ["Experiment13", "Experiment07"]
            actualValue = rankExperiments("Experiment07", "Experiment13")

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="00, 09, 17"):

            expectedValue = ["Experiment09", "Experiment00", "Experiment17"]
            actualValue = rankExperiments("Experiment00", "Experiment09", "Experiment17")

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="01, 02, 03, 04, 05"):

            expectedValue = ['Experiment03', 'Experiment04', 'Experiment01', 'Experiment02', 'Experiment05']
            actualValue = rankExperiments("Experiment01", "Experiment02", "Experiment03", "Experiment04", "Experiment05")

            self.assertEqual(expectedValue, actualValue)

    def test_duration_initializer(self):

        with self.subTest(key="Normal"):

            d = Duration(3, 2, 20)
            self.assertIsNotNone(d)

        with self.subTest(key="AttributeCheck"):

            d = Duration(hours=20, seconds=188)

            self.assertTrue(hasattr(d, "hours") and hasattr(d, "minutes") and hasattr(d, "seconds"))

        with self.subTest(key="LargeSeconds"):

            d = Duration(3, 14, 188)
            expectedValue = 3, 17, 8
            actualValue = d.hours, d.minutes, d.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="LargeMinutes"):

            d = Duration(1, 92, 30)
            expectedValue = 2, 32, 30
            actualValue = d.hours, d.minutes, d.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="LargeIntegers"):

            d = Duration(103, 148, 397)
            expectedValue = 105, 34, 37
            actualValue = d.hours, d.minutes, d.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="WrongType"):

            self.assertRaises(TypeError, Duration, hours=2, minutes=3.5, seconds=10)

        with self.subTest(key="WrongValue"):

            self.assertRaises(ValueError, Duration, hours=0, minutes=15, seconds=-1)


    def test_duration_stringRepresentation(self):

        with self.subTest(key="String1"):

            expectedValue = "00:02:03"
            actualValue = str(Duration(minutes=2, seconds=3))

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="String2"):

            expectedValue = "101:00:00"
            actualValue = str(Duration(hours=101))

            self.assertEqual(expectedValue, actualValue)

    def test_duration_getTotalSeconds(self):

        with self.subTest(key="Seconds1"):

            expectedValue = 85285
            actualValue = Duration(hours=23, minutes=41, seconds=25).getTotalSeconds()

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Seconds2"):

            expectedValue = 96642
            actualValue = Duration(hours=26, minutes=50, seconds=42).getTotalSeconds()

            self.assertEqual(expectedValue, actualValue)

    def test_duration_addition(self):

        d1 = Duration(5, 59, 23)
        d2 = Duration(3, 12, 45)

        total = d1 + d2

        with self.subTest(key="Normal"):

            expectedValue = 9, 12, 8
            actualValue = total.hours, total.minutes, total.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertTrue(total is not d1 and total is not d2)

        with self.subTest(key="WrongType"):

            self.assertRaises(TypeError, lambda x, y: x + y, d1, 3.14)

    def test_duration_multiplication(self):

        d = Duration(11, 13, 50)

        with self.subTest(key="Normal1"):

            scaled = d * 3
            expectedValue = 33, 41, 30
            actualValue = scaled.hours, scaled.minutes, scaled.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Normal1"):

            scaled = 5 * d
            expectedValue = 56, 9, 10
            actualValue = scaled.hours, scaled.minutes, scaled.seconds

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            scaled = d * 2
            self.assertTrue(scaled is not d)

        with self.subTest(key="WrongType"):

            self.assertRaises(TypeError, lambda x, y: x * y, d, 3.14)

        with self.subTest(key="WrongValue"):

            self.assertRaises(ValueError, lambda x, y: x * y, d, 0)

if __name__ == '__main__':
    unittest.main()
