import unittest
from mainclass import MainClass
from boundary import OutOfBoundaryMarksError
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_sufficient_details(self):
        test_obj = TestUtils()
        try:
            MainClass.calculate_result("Venu,92,98")
            test_obj.yakshaAssert("TestSufficientDetails", False, "exception")
            print("TestSufficientDetails = Failed")
        except IndexError:
            test_obj.yakshaAssert("TestSufficientDetails", True, "exception")
            print("TestSufficientDetails = Passed")

    def test_data_format_at_name(self):
        test_obj = TestUtils()
        try:
            MainClass.calculate_result("80,92xyz,98,90")
            test_obj.yakshaAssert("TestDataFormatAtName", False, "exception")
            print("TestDataFormatAtName = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestDataFormatAtName", True, "exception")
            print("TestDataFormatAtName = Passed")

    def test_data_format_at_marks(self):
        test_obj = TestUtils()
        try:
            MainClass.calculate_result("Venu,92xyz,98,90")
            test_obj.yakshaAssert("TestDataFormatAtMarks", False, "exception")
            print("TestDataFormatAtMarks = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestDataFormatAtMarks", True, "exception")
            print("TestDataFormatAtMarks = Passed")
    def test_marks_boundary_exception(self):
        test_obj = TestUtils()
        try:
            MainClass.calculate_result("Venu,192,98,90")
            test_obj.yakshaAssert("TestMarksBoundaryException", False, "exception")
            print("TestMarksBoundaryException = Failed")
        except (ValueError,OutOfBoundaryMarksError):
            test_obj.yakshaAssert("TestMarksBoundaryException", True, "exception")
            print("TestMarksBoundaryException = Passed")

    def test_negative_marks_exception(self):
        test_obj = TestUtils()
        try:
            MainClass.calculate_result("Venu,-80,98,90")
            test_obj.yakshaAssert("TestNegativeMarksException", False, "exception")
            print("TestNegativeMarksException = Failed")
        except (ValueError,OutOfBoundaryMarksError):
            test_obj.yakshaAssert("TestNegativeMarksException", True, "exception")
            print("TestNegativeMarksException = Passed")
