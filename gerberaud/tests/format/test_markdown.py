from gerberaud.format import MarkdownFormatter


class TestMarkdownFormatter:

    def test_h1(self):
        assert MarkdownFormatter.h1("boo") == "# boo\n\n"

    pass
