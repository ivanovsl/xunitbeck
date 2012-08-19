
from TestCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.WasRun = None
        TestCase.__init__(self, name)
    def testMethod(self):
        self.WasRun = 1
        self.log += "testMethod "
    def setUp(self):
        self.WasSetUp = 1
        self.WasRun = 1
        self.log = "setUp "
    def tearDown(self):
        self.log += "tearDown "


