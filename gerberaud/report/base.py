from abc import ABC, abstractmethod
from typing import TypeVar, Generic


__all__ = ["ReportBase"]

T = TypeVar("T")


class ReportBase(ABC, Generic[T]):
    content: T

    @abstractmethod
    def to_markdown(self) -> str: ...
