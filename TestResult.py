class TestResult:
    def __init__(self):
        self.runCount = 0

    def test_started(self):
        self.runCount += 1

    def summary(self):
        return "%d run, 0 failed" % self.runCount
