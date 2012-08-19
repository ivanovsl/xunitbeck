from WasRun import WasRun
from TestCase import TestCase

class BeckTestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetUp(self):
        self.test.run()
        assert self.test.WasSetUp

    def testRunning(self):
        self.test.run()
        assert self.test.WasRun

BeckTestCaseTest("testRunning").run()
BeckTestCaseTest("testSetUp").run()
