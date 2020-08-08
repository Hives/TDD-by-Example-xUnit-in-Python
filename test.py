#! /usr/bin/env python

from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert(test.log == "set_up test_method tear_down ")

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert(result.summary() == "1 run, 0 failed")


TestCaseTest("test_template_method").run()
TestCaseTest("test_result").run()
