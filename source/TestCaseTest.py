from WasRun import WasRun
from TestCase import TestCase

class BeckTestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log

BeckTestCaseTest("testTemplateMethod").run()