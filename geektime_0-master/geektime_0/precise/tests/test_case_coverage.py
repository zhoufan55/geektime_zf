from geektime_0.precise.core.case_coverage import CaseCoverage
from geektime_0.precise.core.code_diff import CodeDiff
from geektime_0.precise.core.code_line import CodeLine
from geektime_0.precise.core.coverage_agent import CoverageAgent
from geektime_0.precise.core.coverage_data import CoverageData
from geektime_0.precise.core.test_case import TestCase
from geektime_0.precise.jacoco.jacoco_coverage_agent import JacocoCoverageAgent

case_coverage_data_path = 'case_coverage.yaml'

code_line1 = CodeLine(source_file='1.java', line_num=1)
code_line2 = CodeLine(source_file='1.java', line_num=2)
code_line3 = CodeLine(source_file='1.java', line_num=3)


def test_save():
    testcase = "demo"
    # testcase setup
    agent = CoverageAgent()
    agent.clear()
    # testcase start
    # pytest ..
    # testcase teardown
    coverage_path = agent.collect()
    coverage_data = CoverageData()
    coverage_data.parse(coverage_path)
    case_coverage = CaseCoverage()
    case_coverage.save(testcase, coverage_data)
    case_coverage.report()
    case_coverage.dump(case_coverage_data_path)


def test_save_jacoco():
    testcase = "demo"
    # testcase setup
    agent = JacocoCoverageAgent(
        home='/Users/seveniruby/ke/shift_left/jacoco/latest',
        project='/Users/seveniruby/projects/spring-petclinic',
        host='127.0.0.1',
        port=6300
    )
    agent.clear()

    # testcase start
    # pytest ..
    # testcase teardown
    coverage_path = agent.collect('/tmp/jacoco')
    coverage_data = CoverageData()
    coverage_data.parse(coverage_path)
    case_coverage = CaseCoverage()
    case_coverage.save(testcase, coverage_data)
    case_coverage.report()
    case_coverage.dump(case_coverage_data_path)


def test_find_diff():
    old = "main"
    new = 'dev'
    code_diff = CodeDiff()
    code_diff.load(old, new)
    case_coverage = CaseCoverage()
    case_coverage.load(case_coverage_data_path)
    testcases = case_coverage.find_testcases_by_diff(code_diff)
    print(testcases)


def test_find():
    case_coverage = CaseCoverage()
    case_coverage.load(case_coverage_data_path)

    testcase = TestCase(name='single')
    code_line1 = CodeLine(source_file='1.java', line_num=1)
    code_line2 = CodeLine(source_file='1.java', line_num=2)
    code_line3 = CodeLine(source_file='1.java', line_num=3)
    coverage_lines = [
        code_line1,
        code_line2
    ]

    diff_lines = [
        code_line2
    ]
    code_diff = CodeDiff()
    code_diff.data = diff_lines

    coverage_data = CoverageData()
    coverage_data.lines = coverage_lines

    case_coverage.save(testcase, coverage_data)
    r = case_coverage.find_testcases_by_diff(code_diff)
    assert len(r) > 0

    diff_lines = [
        code_line3
    ]
    code_diff = CodeDiff()
    code_diff.data = diff_lines

    r = case_coverage.find_testcases_by_diff(code_diff)
    assert len(r) == 0


def test_dump():
    case_coverage = CaseCoverage()
    testcase = TestCase(name='single')

    coverage_lines = [
        code_line1,
        code_line2
    ]

    coverage_data = CoverageData()
    coverage_data.lines = coverage_lines

    case_coverage.save(testcase, coverage_data)
    case_coverage.dump('case_coverage.yaml')


def test_load():
    case_coverage = CaseCoverage()
    case_coverage.load('case_coverage.yaml')
    print(case_coverage.dict())

    code_diff = CodeDiff()
    code_diff.data = [code_line3]
    r = case_coverage.find_testcases_by_diff(code_diff)
    assert len(r) == 0

    code_diff.data = [code_line2]
    r = case_coverage.find_testcases_by_diff(code_diff)
    assert len(r) == 1

    code_diff.data = [code_line1]
    r = case_coverage.find_testcases_by_diff(code_diff)
    assert len(r) == 1
