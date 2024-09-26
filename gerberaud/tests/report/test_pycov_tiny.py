from gerberaud.report import PyCoverageTinyReport


class TestPyCoverageTiny:
    def setup_method(self):
        self.report = PyCoverageTinyReport("a")

    def test_to_markdown(self):
        pass
