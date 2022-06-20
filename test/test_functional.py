import unittest
from mainclass import MainClass
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_is_candidate_qualified(self):
        obj=MainClass.calculate_result("Venu,92,98,96")
        test_obj = TestUtils()
        if type(obj)!=type(None):
            test_obj.yakshaAssert("TestIsCandidateQualified", True, "functional")
            print("TestIsCandidateQualified = Passed")
        else:
            test_obj.yakshaAssert("TestIsCandidateQualified", False, "functional")
            print("TestIsCandidateQualified = Failed")

    def test_is_candidate_fail(self):
        obj=MainClass.calculate_result("Ravan,42,38,96")
        test_obj = TestUtils()
        if type(obj)==type(None):
            test_obj.yakshaAssert("TestIsCandidateFail", True, "functional")
            print("TestIsCandidateFail = Passed")
        else:
            test_obj.yakshaAssert("TestIsCandidateFail", False, "functional")
            print("TestIsCandidateFail = Failed")

    def test_is_candidate_pass(self):
        obj=MainClass.calculate_result("Ravan,52,55,58")
        test_obj = TestUtils()
        if type(obj)==type(None):
            test_obj.yakshaAssert("TestIsCandidatePass", True, "functional")
            print("TestIsCandidatePass = Passed")
        else:
            test_obj.yakshaAssert("TestIsCandidatePass", False, "functional")
            print("TestIsCandidatePass = Failed")
