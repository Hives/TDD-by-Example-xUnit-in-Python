from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.log = ""

    def set_up(self):
        self.log += "set_up "

    def tear_down(self):
        self.log += "tear_down "

    def test_method(self):
        self.log += "test_method "
