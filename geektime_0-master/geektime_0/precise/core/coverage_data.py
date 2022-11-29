from pydantic import BaseModel

from geektime_0.precise.core.code_line import CodeLine


class CoverageData(BaseModel):
    lines: list[CodeLine] = []

    def parse(self, path):
        ...
