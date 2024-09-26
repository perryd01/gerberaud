from .base import ReportBase
from gerberaud.convert import PyCoverageData
from gerberaud.format import MarkdownFormatter


class PyCoverageTinyReport(ReportBase[PyCoverageData]):
    labels = ["Name", "Statements", "Miss", "Cover"]

    def __init__(self, input: PyCoverageData) -> None:
        self.content = input

    def to_markdown(self) -> str:
        v = " ".join(
            [
                MarkdownFormatter.h3("PyCoverage report"),
                MarkdownFormatter.table(labels=self.labels, rows=[]),
            ]
        )

        return v
