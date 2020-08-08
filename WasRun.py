from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.wasRun = None
        self.wasSetUp = None

    def set_up(self):
        self.wasSetUp = 1

    def test_method(self):
        self.wasRun = 1
