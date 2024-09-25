from .base import ReportBase

__all__ = ["RawReport"]


class RawReport(ReportBase[str]):

    def __init__(self, text: str) -> None:
        self.content = text

    def to_markdown(self) -> str:
        return self.content
