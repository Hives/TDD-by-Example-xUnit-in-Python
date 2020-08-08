from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert (test.log == "set_up test_method tear_down ")

    def test_result(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert (self.result.summary() == "1 run, 0 failed")

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert (self.result.summary() == "1 run, 1 failed")

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert (self.result.summary() == "1 run, 1 failed")

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(self.result)
        assert (self.result.summary() == "2 run, 1 failed")
