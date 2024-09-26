from typing import TypeVar

T = TypeVar("T")


class MarkdownFormatter:

    @staticmethod
    def __heading(level: int, text: str) -> str:
        return f"{'#' * level} {text}\n\n"

    @staticmethod
    def h1(text: str) -> str:
        return MarkdownFormatter.__heading(level=1, text=text)

    @staticmethod
    def h2(text: str) -> str:
        return MarkdownFormatter.__heading(level=2, text=text)

    @staticmethod
    def h3(text: str) -> str:
        return MarkdownFormatter.__heading(level=3, text=text)

    @staticmethod
    def h4(text: str) -> str:
        return MarkdownFormatter.__heading(level=4, text=text)

    @staticmethod
    def link(text: str, link: str) -> str:
        return f"[{text}]({link})"

    @staticmethod
    def code(lang: str, code: str) -> str:
        return f"```{lang}\n{code}\n```\n\n"

    @staticmethod
    def table(labels: list[str], rows: list[dict]) -> str:
        col_num = len(labels)
        if col_num == 0 and len(rows) == 0:
            return ""

        if any(len(row) != col_num for row in rows):
            raise ValueError("Table column dimension mismatch")

        return "".join([
            MarkdownFormatter.table_head(labels=labels),
            MarkdownFormatter.table_body(rows=rows)
        ])

    @staticmethod
    def table_head(labels: list[str]) -> str:
        col_num = len(labels)
        top = f"| {" | ".join(labels)} |\n"
        bottom = f"| {" | ".join(MarkdownFormatter._repeat(
            val="---", times=col_num))} |\n"
        return top + bottom

    # TODO: ensure same order
    @staticmethod
    def table_body(rows: list[dict]) -> str:
        def make_row(row: dict):
            row_values = list(row.values())
            return f"| {" | ".join(row_values)} |\n"

        return "".join(list(map(make_row, rows))) + "\n"

    @staticmethod
    def _repeat(val: T, times: int) -> list[T]:
        return [val] * times
