from WasRun import WasRun
from TestCase import TestCase

class BeckTestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run. 0 failed" == result.summary()
    def testFailedResult(self):
        test = WasRun("wasBrokenMethod")
        result = test.run()
        assert "1 run. 1 failed" == result.summary()

BeckTestCaseTest("testTemplateMethod").run()
BeckTestCaseTest("testResult").run()
BeckTestCaseTest("testFailedResult").run()