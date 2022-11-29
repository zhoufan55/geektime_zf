import json

from geektime_0.precise.core.code_diff import CodeDiff
from geektime_0.precise.core.coverage_data import CoverageData
from geektime_0.precise.core.test_case import TestCase

import yaml

from pydantic import BaseModel


class CaseCoverage(BaseModel):
    data: dict[str, CoverageData] = {}

    def save(self, case: TestCase, coverage_data: CoverageData):
        self.data[str(case)] = coverage_data

    def find_testcases_by_diff(self, diff: CodeDiff) -> list[str]:

        result = []
        for testcase, coverage in self.data.items():
            for line in coverage.lines:
                for diff_line in diff.data:
                    if line == diff_line:
                        result.append(testcase)
        return result

    def report(self):
        pass

    def dump(self, path):
        if path.split('.')[-1] == 'json':
            with open(path, 'w') as f:
                json.dump(self, f)

        if path.split('.')[-1] == 'yaml':
            with open(path, 'w') as f:
                yaml.dump(self, f)

    def load(self, path: str):
        if path.split('.')[-1] == 'json':
            with open(path, 'r') as f:
                self.data = json.load(f).data

        if path.split('.')[-1] == 'yaml':
            with open(path, 'r') as f:
                self.data = yaml.unsafe_load(f).data
