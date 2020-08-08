#! /usr/bin/env python

from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert(test.log == "set_up test_method ")


TestCaseTest("test_template_method").run()
