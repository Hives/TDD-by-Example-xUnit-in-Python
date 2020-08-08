#! /usr/bin/env python

from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def test_set_up(self):
        self.test.run()
        assert self.test.wasSetUp


TestCaseTest("test_running").run()
TestCaseTest("test_set_up").run()
