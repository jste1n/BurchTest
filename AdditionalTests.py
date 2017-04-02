import unittest
from bruch.Bruch import *


class AdditionalTests(unittest.TestCase):
    """
    5 weitere test
    steinwender
    """
    def setUp(self):
        self.b = Bruch(10, 20)
        self.b2 = Bruch(50, 25)
        pass

    def tearDown(self):
        del self.b, self.b2
        pass

    def testVal(self):
        """
        calculates the fraction to a real number
        """
        assert (float(self.b) == 0.5)

    def testInvert(self):
        """
        inverts the number
        """
        b3 = ~self.b
        assert (float(b3) == 2)

    def testNegate(self):
        """
        negation of a number
        """
        b3 = Bruch(-65, 93)
        assert (-b3 == Bruch(65, 93))

    def testSmaller(self):
        """
        tests if first number is smaller than second one
        """
        assert (self.b < self.b2)

    def testToString(self):
        """
        converts Bruch to a string
        """
        b3 = Bruch(2, 3)
        assert ("(2/3)" == str(b3))
