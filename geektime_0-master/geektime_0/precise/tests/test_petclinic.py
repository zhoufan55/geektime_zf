import inspect
import os
import subprocess
import threading

import requests

from geektime_0.precise.core.case_coverage import CaseCoverage
from geektime_0.precise.core.coverage_agent import CoverageAgent
from geektime_0.precise.core.coverage_data import CoverageData
from geektime_0.precise.jacoco.jacoco_coverage_agent import JacocoCoverageAgent
from geektime_0.precise.jacoco.jacoco_coverage_data import JacocoCoverageData

agent = JacocoCoverageAgent(
    home='/Users/seveniruby/ke/shift_left/jacoco/latest',
    project='/Users/seveniruby/projects/spring-petclinic'
)
case_coverage = CaseCoverage()


class TestPetclinic:
    def setup(self, method):
        agent.clear()

    def teardown(self, method):
        # dump覆盖率
        path = agent.collect()
        # 解析覆盖率
        coverage_data = JacocoCoverageData()
        coverage_data.parse(path)
        print(coverage_data.dict())
        # 存储用例与case对应关系
        case_coverage.save(method.__name__, coverage_data)

    def teardown_class(self):
        print(case_coverage.dict())
        case_coverage.dump('case_coverage.yaml')

    def test_null(self):
        r = requests.get(
            'http://127.0.0.1:8080/owners',
            params={'firstName': None},
            headers={'testcase': 'test_null'}
        )
        assert r.status_code == 200

    def test_single(self):
        r = requests.get(
            'http://127.0.0.1:8080/owners',
            params={'lastName': 'black'}
        )
        assert r.status_code == 200

    def test_multi(self):
        r = requests.get(
            'http://127.0.0.1:8080/owners',
            params={'lastName': 'davis'}
        )
        assert r.status_code == 200
