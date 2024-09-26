__all__ = ["PyCoverageData"]


class PyCoverageData:

    def __init__(self):
        pass

    @classmethod
    def from_json(cls, input: str) -> "PyCoverageData":
        pass

    @classmethod
    def from_xml(cls, input: str) -> "PyCoverageData":
        pass

    @classmethod
    def from_toml(cls, input: str) -> "PyCoverageData":
        pass

    @classmethod
    def from_coverage_file(cls, filepath: str) -> "PyCoverageData":
        pass
