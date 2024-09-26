import pytest
from gerberaud.format import MarkdownFormatter


class TestMarkdownFormatter:

    def test_h1(self):
        assert MarkdownFormatter.h1("boo") == "# boo\n\n"

    def test_h2(self):
        assert MarkdownFormatter.h2("boo") == "## boo\n\n"

    def test_h3(self):
        assert MarkdownFormatter.h3("boo") == "### boo\n\n"

    def test_h4(self):
        assert MarkdownFormatter.h4("boo") == "#### boo\n\n"

    def test_link(self):
        assert (
            MarkdownFormatter.link("example", "https://google.com")
            == "[example](https://google.com)"
        )

    def test_code(self):
        code = "import a\n\nb = a"
        expected = """```python
import a

b = a
```

"""
        assert MarkdownFormatter.code("python", code) == expected

    def test_table(self):
        labels = ["foo", "bar"]
        rows: list[dict] = [{"foo": "a", "bar": "b"}, {"foo": "c", "bar": "d"}]
        expected = "| foo | bar |\n| --- | --- |\n" + "| a | b |\n| c | d |\n\n"
        assert MarkdownFormatter.table(labels=labels, rows=rows) == expected

    def test_table_empty(self):
        labels = []
        rows: list[dict] = []
        assert MarkdownFormatter.table(labels=labels, rows=rows) == ""

    def test_table_dimension_mismatch(self):
        labels = ["foo"]
        rows: list[dict] = [{"foo": "a", "bar": "b"}, {"foo": "c", "bar": "d"}]

        with pytest.raises(ValueError):
            assert MarkdownFormatter.table(labels=labels, rows=rows)

    def test_table_head(self):
        labels = ["foo", "bar"]
        expected = "| foo | bar |\n| --- | --- |\n"

        assert MarkdownFormatter.table_head(labels=labels) == expected

    def test_table_body(self):
        rows: list[dict] = [{"foo": "a", "bar": "b"}, {"foo": "c", "bar": "d"}]
        expected = "| a | b |\n| c | d |\n\n"

        assert MarkdownFormatter.table_body(rows=rows) == expected
        pass

    def test_repeat(self):
        expected: list[str] = ["---", "---", "---"]

        assert MarkdownFormatter._repeat(val="---", times=3) == expected
