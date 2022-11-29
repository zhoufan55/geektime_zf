from dataclasses import dataclass

from pydantic import BaseModel


class CodeLine(BaseModel):
    source_file: str = None
    package: str = None
    clazz: str = None
    method: str = None
    line_num: int = None
