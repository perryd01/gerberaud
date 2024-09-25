from gerberaud.report import RawReport


class TestRawReport:

    def setup_method(self):
        self.report = RawReport("# Title")

    def test_to_markdown(self):
        assert self.report.to_markdown() == "# Title"
