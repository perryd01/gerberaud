__all__ = ["MarkdownFormatter"]


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
