import unittest
from bruch.Bruch import *
class AdditionalTests(unittest.TestCase):
    def setUp(self):
        self.b = Bruch(10,20)
        self.b2 = Bruch(50,25)
        pass

    def tearDown(self):
        del self.b, self.b2
        pass

    def testVal(self):
        assert(float(self.b)==0.5)

    def testInvert(self):
        b3 = ~self.b
        assert(float(b3)==2)

    def testNegate(self):
        b3 = Bruch(-65, 93)
        assert(-b3 == Bruch(65, 93))

    def testSmaller(self):
        assert(self.b<self.b2)

    def testToString(self):
        b3=Bruch(2,3)
        assert("(2/3)"==str(b3))

