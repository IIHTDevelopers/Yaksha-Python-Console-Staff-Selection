import unittest
import sys
sys.path.append("..")
from mainclass import MainClass
from boundary import OutOfBoundaryMarksError
from test.TestUtils import TestUtils
class BoundaryTest(unittest.TestCase):
    def test_negative_marks(self):
        test_obj = TestUtils()
        try:
            MainClass.calculate_result("Venu,-80,98,90")
            test_obj.yakshaAssert("TestNegativeMarks", False, "boundary")
            print("TestNegativeMarks = Failed")
        except (ValueError,OutOfBoundaryMarksError):
            test_obj.yakshaAssert("TestNegativeMarks", True, "boundary")
            print("TestNegativeMarks = Passed")

    def test_marks_boundary(self):
        test_obj = TestUtils()
        try:
            MainClass.calculate_result("Venu,192,98,90")
            test_obj.yakshaAssert("TestMarksBoundary", False, "boundary")
            print("TestMarksBoundary = Failed")
        except (ValueError,OutOfBoundaryMarksError):
            test_obj.yakshaAssert("TestMarksBoundary", True, "boundary")
            print("TestMarksBoundary = Passed")
