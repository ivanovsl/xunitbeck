from WasRun import WasRun
from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite

class BeckTestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult()
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "setUp testMethod tearDown " == test.log
    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "1 run. 0 failed" == self.result.summary()
    def testFailedResult(self):
        test = WasRun("wasBrokenMethod")
        test.run(self.result)
        assert "1 run. 1 failed" == self.result.summary()
    def testFailedResultFormatted(self):
        self.result.testStarted()
        self.result.testFailed()
        assert "1 run. 1 failed" == self.result.summary()
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("wasBrokenMethod"))
        suite.run(self.result)
        assert "2 run. 1 failed" == self.result.summary()

suite = TestSuite()
suite.add(BeckTestCaseTest("testTemplateMethod"))
suite.add(BeckTestCaseTest("testResult"))
suite.add(BeckTestCaseTest("testFailedResult"))
suite.add(BeckTestCaseTest("testFailedResultFormatted"))
suite.add(BeckTestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print result.summary()