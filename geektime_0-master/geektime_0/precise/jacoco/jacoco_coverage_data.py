import xml.etree.ElementTree as et

from pydantic import BaseModel

from geektime_0.precise.core.code_line import CodeLine
from geektime_0.precise.core.coverage_data import CoverageData


class JacocoCoverageData(CoverageData):

    def parse(self, path):
        root = et.parse(path)
        res = []
        for package in root.findall('./package'):
            package_name = package.get('name')
            for sourcefile in package.findall('./sourcefile'):
                sourcefile_name = sourcefile.get('name')
                for line in sourcefile.findall('./line'):
                    line_num = int(line.get('nr'))
                    covered = int(line.get('ci')) > 0

                    if covered:
                        code_line = CodeLine(line_num=line_num, source_file=sourcefile_name, package=package_name)
                        res.append(code_line)
        self.lines = res
