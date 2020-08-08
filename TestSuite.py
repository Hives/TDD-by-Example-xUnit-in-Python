#! /usr/bin/env python

from TestCaseTest import TestCaseTest

print(TestCaseTest("test_template_method").run().summary())
print(TestCaseTest("test_result").run().summary())
print(TestCaseTest("test_failed_result").run().summary())
print(TestCaseTest("test_failed_result_formatting").run().summary())
