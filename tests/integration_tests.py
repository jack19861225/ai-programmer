from main.function import Function, Requirement
from main.programgenerator2 import Parameter

__author__ = 'david'

import unittest
from main import programmer



class programmerTest(unittest.TestCase):

    def testSimpleReq(self):
        requirements = []
        function = Function("foo", [Parameter("x", int)], int)
        function.add_requirement(Requirement((5,), 5))
        programmer.write(function)
        self.failUnless(function.execute("5") == 5)
        print(function.body_text)

    def testTwoReq(self):
        requirements = []
        function = Function("foo", [Parameter("x", int)], int)
        function.add_requirement(Requirement((5,), 5))
        function.add_requirement(Requirement((6,), 6))
        programmer.write(function)
        self.failUnless(function.execute("5") == 5)
        self.failUnless(function.execute("6") == 6)
        print(function.body_text)

    def testDiffReqAndAsserts(self):
        requirements = []
        function = Function("foo", [Parameter("x", int)], int)
        function.add_requirement(5,6)
        function.add_requirement(6,7)
        function.add_requirement(7,8)
        programmer.write(function)
        self.failUnless(function.execute("4") == 5)
        self.failUnless(function.execute("5") == 6)
        print(function.body_text)

def main():
    unittest.main()

if __name__ == '__main__':
    main()